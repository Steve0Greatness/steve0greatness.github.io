from Renderers import RenderTemplate, RenderMarkdown
from sys import argv
from shutil import rmtree as DeleteDirectory
from os import mkdir as CreateDirectory, listdir as ListDirectory, unlink as DeleteFile
from os.path import isfile as IsFile, exists as PathExists
from distutils.dir_util import copy_tree as CopyDirectory
from datetime import datetime
from json import dump as DumpJSON
from yaml import safe_load as LoadYML

GITHUB_BUILD_DIR = "docs" # Separate because this site is built with an action that won't work if they aren't
LOCAL_BUILD_DIR = "build"

BUILD_DIRECTORY = GITHUB_BUILD_DIR if len(argv) > 1 and argv[1] == "gh-pages-deploy" else LOCAL_BUILD_DIR

PAGES = {
    "index.html": "index.html",
    "blog-list.html": "blog/index.html",
    "blog-feed.rss": "blog/feed.rss",
    "blog-feed.atom": "blog/feed.atom",
    "404.html": "404.html"
}

DISALLOWED_SITEMAP = [
    "404.html",
    "blog-feed.rss"
]

REDIRECTS = [
    ("link-tree.html", "list/link-tree.html") # Old location -> new location
]

SITEMAP_HREF = "https://steve0greatness.github.io/"
sitemap = []

def WipeFinalDir():
    if not PathExists(BUILD_DIRECTORY):
        print("Directory didn't existing, creating it...")
        CreateDirectory(BUILD_DIRECTORY)
        return
    print("Directory exists, wiping it...")
    for item in ListDirectory(BUILD_DIRECTORY):
        path = BUILD_DIRECTORY + "/" + item
        if IsFile(path):
            DeleteFile(path)
            continue
        DeleteDirectory(path)

def PostDateToDateObj(Date):
    return datetime.strptime(Date, "%Y %b %d")

def PostSortHelper(Post):
    return PostDateToDateObj(Post["date"])

def GetBlogList():
    print("Grabbing post list")
    PostSlugs = ListDirectory("blog-posts")
    Posts = []
    for slug in PostSlugs:
        print("Grabbing post list blog-posts/%s" % (slug))
        with open("blog-posts/" + slug, encoding="utf-8") as MDFile:
            PostHTML = RenderMarkdown(MDFile.read())
            Item = PostHTML.metadata
            Item["content"] = PostHTML
            Item["rss-post-time"] = PostDateToDateObj(Item["date"]).strftime("%a, %d %b %Y") + " 00:00:00 GMT"
            Item["atom-post-time"] = PostDateToDateObj(Item["date"]).strftime("%Y-%m-%d") + "T00:00:00Z"
            Item["atom-update-time"] = Item["atom-post-time"]
            if "updated" in Item:
                Item["atom-update-time"] = PostDateToDateObj(Item["updated"]).strftime("%Y-%m-%d") + "T00:00:00Z"
            Item["pathname"] = slug.replace(".md", ".html")
            Posts.append(Item)
    PostsByDate = sorted(Posts, key=PostSortHelper, reverse=True)
    return PostsByDate

PostList = GetBlogList()

def ListParseCategory(Obj, depth):
    html = "<h%d id=\"%s\">%s</h%d>" % (2+depth, Obj["id"], Obj["title"], 2+depth)
    if "paragraph" in Obj:
        html += "<p>%s</p>" % Obj["paragraph"]
    listType = "ul"
    if "list-type" in Obj and Obj["list-type"] == "ordered":
        listType = "ol"
    html += "<%s>" % listType
    for item in Obj["list"]:
        html += "<li>" + LIST_PARSER_DICT[item["type"]](item, depth + 1) + "</li>"
    html += "</%s>" % listType
    return html

def ListParseLink(Obj, depth):
    html = "<a href=\"%s\">" % Obj["href"]
    text = Obj["text"]
    if "text-type" in Obj and Obj["text-type"] == "text/markdown":
        text = RenderMarkdown(text).replace("<p>", "").replace("</p>", "")
    html += text + "</a>"
    if "comment" in Obj:
        html += "(%s)" % Obj["comment"]
    return html

def ListParseText(Obj, depth):
    text = Obj["text"]
    # if "text-type" in Obj and Obj["text-type"] == "text/markdown":
    #     print(RenderMarkdown(text))
    #     text = RenderMarkdown(text) # this doesn't work???
    if "comment" in Obj:
        text += "(%s)" % Obj["comment"]
    return text

LIST_PARSER_DICT = {
    "category": ListParseCategory,
    "link": ListParseLink,
    "text": ListParseText,
}

def GetLists():
    ListSlugs = ListDirectory("lists")
    Lists = []
    for slug in ListSlugs:
        List = {
            "title": "",
            "content": "",
            "filename": slug
        }
        with open("lists/" + slug) as ListYML:
            ListDict = LoadYML(ListYML.read())
            List["title"] = ListDict["title"]
            if "paragraph" in ListDict:
                List["content"] += "<p>%s</p>" % ListDict["paragraph"]
            for item in ListDict["list"]:
                List["content"] += LIST_PARSER_DICT[item["type"]](item, 0)
        Lists.append(List)
    return Lists

def RenderPosts():
    for post in ListDirectory("blog-posts"):
        path = "blog-posts/" + post
        RenderedHTML: str
        PostMD: str
        PostPath = post.replace(".md", ".html")
        PlaintextPath = post.replace(".md", ".txt")
        with open(path, "r", encoding="utf-8") as PostContent:
            PostMD = PostContent.read()
            PostHTML = RenderMarkdown(PostMD)
            Title = PostHTML.metadata["title"]
            PostDate = PostHTML.metadata["date"]
            Revised = False
            if "updated" in PostHTML.metadata:
                Revised = PostHTML.metadata["updated"]
            RenderedHTML = RenderTemplate("blog-post.html", Revised=Revised, Title=Title, PostDate=PostDate, Content=PostHTML, PostPath=PostPath, PlaintextPath=PlaintextPath)
        print("Building blog/%s to %s/blog/%s" % (post, BUILD_DIRECTORY, PostPath))
        with open(BUILD_DIRECTORY + "/blog/" + PostPath, "w", encoding="utf-8") as PostHTMLFile:
            PostHTMLFile.write(RenderedHTML)
        print("Copying blog/%s to %s/blog/%s" % (post, BUILD_DIRECTORY, PlaintextPath))
        with open(BUILD_DIRECTORY + "/blog/" + PlaintextPath, "w", encoding="utf-8") as PostPlaintext:
            PostPlaintext.write(PostMD)
        sitemap.append(SITEMAP_HREF + "/blog/" + PostPath)

def RenderPage(PageInput: str, ContentDest: str, AllowSitemap: bool = True, **kwargs):
    print("Building views/%s to %s/%s" % (PageInput, BUILD_DIRECTORY, ContentDest))
    if AllowSitemap:
        sitemap.append(SITEMAP_HREF + ContentDest)
    with open(BUILD_DIRECTORY + "/" + ContentDest, "w", encoding="utf-8") as DestLocation:
        DestLocation.write(RenderTemplate(PageInput, **kwargs))

def CreateJSONFeed():
    CreatedJSON = {
        "version": "https://jsonfeed.org/version/1",
        "title": "Steve0Greatness' Blog",
        "home_page_url": "https://steve0greatness.github.io",
        "feed_url": "https://steve0greatness.github.io/blog/feed.rss",
        "language": "en-US",
        "favicon": "https://steve0greatness.github.io/favicon.ico",
        "description": "A blog by a human being.",
        "authors": [
            {
                "name": "Steve0Greatness",
                "url": "https://steve0greatness.github.io"
            }
        ],
        "items": []
    }
    for post in PostList:
        CreatedJSON["items"].append({
            "id": "https://steve0greatness.github.io/blog/" + post["pathname"],
			"title": "JSON Feed version 1.1",
			"icon": "https://steve0greatness.github.io/favicon.ico",
			"content_html": post["content"],
			"date_published": post["atom-post-time"],
            "date_modified": post["atom-update-time"],
			"url": "https://steve0greatness.github.io/blog/" + post["pathname"]
        })
    with open(BUILD_DIRECTORY + "/blog/feed.json", "w") as JSONFeedFile:
        DumpJSON(CreatedJSON, JSONFeedFile)

def RenderLists():
    Lists = GetLists()
    CreateDirectory(BUILD_DIRECTORY + "/list/")
    ListIndex = "<ul>"
    for List in Lists:
        FileLocation = "/list/" + List["filename"].replace(".yml", ".html")
        Title = List["title"]
        print("%s -> %s" % ("lists/" + List["filename"], BUILD_DIRECTORY + FileLocation))
        with open(BUILD_DIRECTORY + FileLocation, "w") as file:
            file.write(RenderTemplate("list.html", Content=List["content"], Title=Title, Location=FileLocation))
        ListIndex += "<li><a href=\"%s\">%s</a></li>" % (FileLocation, Title)
    ListIndex += "</ul>"
    print("Building list index")
    with open(BUILD_DIRECTORY + "/list/index.html", "w") as file:
        file.write(RenderTemplate("list-index.html", Content=ListIndex))

def main():
    print("Wiping directory")
    WipeFinalDir()
    print("Creating blog holder")
    CreateDirectory(BUILD_DIRECTORY + "/blog")
    print("Rendering posts")
    RenderPosts()
    CreateJSONFeed()
    print("Copying static directory")
    CopyDirectory("static", BUILD_DIRECTORY)
    print("Creating lists")
    RenderLists()

    print("Building pages")
    for file, path in PAGES.items():
        if file in DISALLOWED_SITEMAP:
            RenderPage(file, path, False, PostList=PostList)
            continue
        RenderPage(file, path, PostList=PostList)
    
    print("Building redirects")
    for OldLocation, NewLocation in REDIRECTS:
        RenderPage("redirect.html", OldLocation, False, redirect=NewLocation)

    with open(BUILD_DIRECTORY + "/sitemap.txt", "w") as SitemapFile:
        SitemapFile.write("\n".join(sitemap))

if __name__ == "__main__":
    main()