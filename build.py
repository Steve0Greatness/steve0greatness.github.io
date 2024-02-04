from Renderers import RenderTemplate, RenderMarkdown
from sys import argv
from shutil import rmtree as DeleteDirectory
from os import mkdir as CreateDirectory, listdir as ListDirectory, unlink as DeleteFile
from os.path import isfile as IsFile, exists as PathExists
from distutils.dir_util import copy_tree as CopyDirectory
from datetime import datetime
from json import dump as DumpJSON
from yaml import safe_load as LoadYML
from re import sub as RegReplace
from typing import Literal

GITHUB_BUILD_DIR = "build" # Separate because this site is built with an action that won't work if they aren't
LOCAL_BUILD_DIR = "build"

IS_GH_ACTIONS = len(argv) > 1 and argv[1] == "gh-pages-deploy"
BUILD_DIRECTORY = GITHUB_BUILD_DIR if IS_GH_ACTIONS else LOCAL_BUILD_DIR


PAGES = {
    "index.html": "index.html",
    "blog-list.html": "blog/index.html",
    "blog-feed.rss": "blog/feed.rss",
    "blog-feed.atom": "blog/feed.atom",
    "404.html": "404.html",
}

DISALLOWED_SITEMAP = {
    "404.html",
    "blog-feed.rss",
    "blog-feed.atom",
    "blog-list.html",
    "index.html",
}

REDIRECTS = {
    "link-tree.html": "list/link-tree.html", # Old location -> new location
}

SITEMAP_HREF = "https://steve0greatness.github.io/"
sitemap = [
    SITEMAP_HREF + "blog/",
    SITEMAP_HREF,
]

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
    PostSlugs: tuple[tuple[Literal["blog-posts", "drafts"], str], ...] = tuple( ("blog-posts", file) for file in ListDirectory("blog-posts") )
    if not IS_GH_ACTIONS and PathExists("drafts"):
        PostSlugs = PostSlugs + tuple( ("drafts", file) for file in ListDirectory("drafts") )
    Posts = []
    for dir, slug in PostSlugs:
        print("Grabbing post list blog-posts/%s" % (slug))
        with open(dir + "/" + slug, encoding="utf-8") as MDFile:
            RawMD = MDFile.read()
            PostHTML = RenderMarkdown(RawMD)
            Item = PostHTML.metadata
            Item["content"] = PostHTML
            Item["raw-content"] = RawMD
            Item["rss-content"] = PostHTML.replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;")
            Item["atom-content"] = RegReplace("</(?=.*)", "</xhtml:", RegReplace("<(?=[^\/].*)", "<xhtml:", PostHTML))
            Item["rss-post-time"] = PostDateToDateObj(Item["date"]).strftime("%a, %d %b %Y") + " 00:00:00 GMT"
            Item["atom-post-time"] = PostDateToDateObj(Item["date"]).strftime("%Y-%m-%d") + "T00:00:00Z"
            Item["atom-update-time"] = Item["atom-post-time"]
            if "updated" in Item:
                Item["atom-update-time"] = PostDateToDateObj(Item["updated"]).strftime("%Y-%m-%d") + "T00:00:00Z"
            Item["pathname"] = slug.replace(".md", ".html")
            Item["plaintext"] = slug.replace(".md", ".txt")
            Item["origin"] = slug
            Item["is-draft"] = dir == "drafts"
            Posts.append(Item)
    PostsByDate = sorted(Posts, key=PostSortHelper, reverse=True)
    return PostsByDate

PostList = []


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
            List["content"] += "<ul>"
            for item in ListDict["list"]:
                List["content"] += "<li>" + LIST_PARSER_DICT[item["type"]](item, 0) + "</li>"
            List["content"] += "</ul>"
        Lists.append(List)
        sitemap.append(SITEMAP_HREF + "list/" + slug)
    sitemap.append(SITEMAP_HREF + "list/")
    return Lists

def RenderPosts():
    global PostList
    for post in PostList:
        Revised = post["updated"] if "updated" in post else False
        RenderedHTML = RenderTemplate(
                                        "blog-post.html",
                                        Revised=Revised,
                                        Title=post["title"],
                                        PostDate=post["date"],
                                        Content=post["content"],
                                        PostPath=post["pathname"],
                                        PlaintextPath=post["plaintext"],
                                        IsDraft=post["is-draft"],
                                    )
        print("Building blog-posts/%s to %s/blog/%s" % (post["origin"], BUILD_DIRECTORY, post["pathname"]))
        with open(BUILD_DIRECTORY + "/blog/" + post["pathname"], "w", encoding="utf-8") as PostHTMLFile:
            PostHTMLFile.write(RenderedHTML)
        print("Copying blog-posts/%s to %s/blog/%s" % (post["origin"], BUILD_DIRECTORY, post["plaintext"]))
        with open(BUILD_DIRECTORY + "/blog/" + post["plaintext"], "w", encoding="utf-8") as PostHTMLFile:
            PostHTMLFile.write(post["raw-content"])
        sitemap.append(SITEMAP_HREF + "blog/" + post["pathname"])

def RenderPage(PageInput: str, ContentDest: str, AllowSitemap: bool = True, **kwargs):
    print("Building views/%s to %s/%s" % (PageInput, BUILD_DIRECTORY, ContentDest))
    if AllowSitemap:
        sitemap.append(SITEMAP_HREF + ContentDest)
    with open(BUILD_DIRECTORY + "/" + ContentDest, "w", encoding="utf-8") as DestLocation:
        DestLocation.write(RenderTemplate(PageInput, **kwargs))

def CreateJSONFeed():
    global PostList
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
    global PostList
    PostList = GetBlogList()
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
        AllowSitemap = file not in DISALLOWED_SITEMAP
        RenderPage(file, path, AllowSitemap, PostList=PostList)
    
    print("Building redirects")
    for OldLocation, NewLocation in REDIRECTS.items():
        RenderPage("redirect.html", OldLocation, False, redirect=NewLocation, old=OldLocation)

    with open(BUILD_DIRECTORY + "/sitemap.txt", "w") as SitemapFile:
        SitemapFile.write("\n".join(sitemap))

if __name__ == "__main__":
    main()