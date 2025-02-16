# This code is licensed under the LGPL.
# The reason for such is that it allows for the use of it
# within proprietry applications.
#
# To view a copy of the LGPL, please refer to
# https://www.gnu.org/licenses/lgpl-3.0.en.html
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

def GetCurTime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

START_TIME = GetCurTime()

DEPLOY_BUILD_DIR = {
    "gh-pages-deploy": "build",
    "gl-pages-deploy": "public",
    "cb-pages": "build",
} # Separate because this site is built with an action that won't work if they aren't
LOCAL_BUILD_DIR = "build"

PAGES_DEPLOY = argv[1] if len(argv) > 1 else None
BUILD_DIRECTORY = DEPLOY_BUILD_DIR[PAGES_DEPLOY] if PAGES_DEPLOY is not None else LOCAL_BUILD_DIR

PAGES = {
    "index.html": "index.html",
    "blog-list.html": "blog/index.html",
    "blog-feed.rss": "blog/feed.rss",
    "blog-feed.atom": "blog/feed.atom",
    "404.html": "404.html",
    "404.html": "not_found.html",
}

DISALLOWED_SITEMAP = {
    "404.html",
    "blog-feed.rss",
    "blog-feed.atom",
    "blog-list.html",
    "index.html",
    "not_found.html",
}

REDIRECTS = {
    "link-tree.html": "/list/link-tree.html", # Old location -> new location
    "extras.html": "https://steve0greatness.github.io/extras",
    "guestbook.html": "https://steve0greatness.atabook.org/",
}

SITEMAP_HREF = "https://steve0greatness.nekoweb.org/"
sitemap = [
    SITEMAP_HREF + "blog/",
    SITEMAP_HREF,
]

def EscapeHTMLForRSS(HTML: str) -> str:
    values = {
        "&": "&amp;", # & is first for a reason, do not change it's location.
        "<": "&lt;",
        ">": "&gt;", 
        "§": "&#xa7;",
    }
    RssHtml = HTML
    for old, new in values.items():
        RssHtml = RssHtml.replace(old, new)
    return RssHtml

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
    if not PAGES_DEPLOY and PathExists("drafts"):
        PostSlugs = PostSlugs + tuple( ("drafts", file) for file in ListDirectory("drafts") )
    Posts = []
    for dir, slug in PostSlugs:
        if not slug.endswith(".md"):
            continue
        print("Grabbing post list blog-posts/%s" % (slug))
        with open(dir + "/" + slug, encoding="utf-8") as MDFile:
            RawMD = MDFile.read()
            PostHTML = RenderMarkdown(RawMD)
            Item = PostHTML.metadata
            Item["content"] = PostHTML
            Item["raw-content"] = RawMD
            Item["rss-content"] = EscapeHTMLForRSS(PostHTML)
            Item["rss-post-time"] = PostDateToDateObj(Item["date"]).strftime("%a, %d %b %Y") + " 00:00:00 GMT"
            Item["atom-post-time"] = PostDateToDateObj(Item["date"]).strftime("%Y-%m-%d") + "T00:00:00Z"
            Item["opengraph-date"] = PostDateToDateObj(Item["date"]).strftime("%Y-%m-%d") 
            Item["opengraph-update"] = Item["opengraph-date"]
            Item["atom-update-time"] = Item["atom-post-time"]
            if "updated" in Item:
                Item["atom-update-time"] = PostDateToDateObj(Item["updated"]).strftime("%Y-%m-%d") + "T00:00:00Z"
                Item["opengraph-update"] = PostDateToDateObj(Item["updated"]).strftime("%Y-%m-%d")
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
        with open("lists/" + slug, encoding="utf-8") as ListYML:
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
                            OpenGraphDate=post["opengraph-date"],
                            post=post,
                            CompileTime=GetCurTime(),
                            SiteCompileTime=START_TIME,
                            ViewName="blog-post.html"
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
        "home_page_url": "https://steve0greatness.nekoweb.org",
        "feed_url": "https://steve0greatness.nekoweb.org/blog/feed.rss",
        "language": "en-US",
        "favicon": "https://steve0greatness.nekoweb.org/favicon.ico",
        "description": "A blog by a human being.",
        "authors": [
            {
                "name": "Steve0Greatness",
                "url": "https://steve0greatness.nekoweb.org"
            }
        ],
        "items": []
    }
    for post in PostList:
        CreatedJSON["items"].append({
            "id": "https://steve0greatness.nekoweb.org/blog/" + post["pathname"],
			"title": "JSON Feed version 1.1",
			"icon": "https://steve0greatness.nekoweb.org/favicon.ico",
			"content_html": post["content"],
			"date_published": post["atom-post-time"],
            "date_modified": post["atom-update-time"],
			"url": "https://steve0greatness.nekoweb.org/blog/" + post["pathname"]
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
            file.write(RenderTemplate(
                "list.html",
                Content=List["content"],
                Title=Title,
                Location=FileLocation,
                CompileTime=GetCurTime(),
                SiteCompileTime=START_TIME,
                ViewName="blog-post.html"
            ))
        ListIndex += "<li><a href=\"%s\">%s</a></li>" % (FileLocation, Title)
    ListIndex += "</ul>"
    print("Building list index")
    with open(BUILD_DIRECTORY + "/list/index.html", "w") as file:
        file.write(
            RenderTemplate(
                            "list-index.html",
                            Content=ListIndex,
                            CompileTime="",
                            SiteCompileTime="",
                            ViewName="list-index.html"
            )
        )

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
        RenderPage(
            file,
            path,
            AllowSitemap,
            PostList=PostList,
            CompileTime=GetCurTime(),
            SiteCompileTime=START_TIME,
            ViewName=file
        )
    
    print("Building redirects")
    for OldLocation, NewLocation in REDIRECTS.items():
        RenderPage("redirect.html", OldLocation, False, redirect=NewLocation, old=OldLocation)

    with open(BUILD_DIRECTORY + "/sitemap.txt", "w") as SitemapFile:
        SitemapFile.write("\n".join(sitemap))

if __name__ == "__main__":
    main()

