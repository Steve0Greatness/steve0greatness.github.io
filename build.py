from Renderers import RenderTemplate, RenderMarkdown
from sys import argv
from shutil import rmtree as DeleteDirectory
from os import mkdir as CreateDirectory, listdir as ListDirectory, unlink as DeleteFile
from os.path import isfile as IsFile, exists as PathExists
from distutils.dir_util import copy_tree as CopyDirectory
from datetime import datetime

GITHUB_BUILD_DIR = "docs" # Separate because this site is built with an action that won't work if they aren't
LOCAL_BUILD_DIR = "build"

BUILD_DIRECTORY = GITHUB_BUILD_DIR if len(argv) > 1 and argv[1] == "gh-pages-deploy" else LOCAL_BUILD_DIR

PAGES = {
    "index.html": "index.html",
    "blog-list.html": "blog/index.html",
    "blog-feed.rss": "blog/feed.rss",
    "link-tree.html": "link-tree.html",
    "404.html": "404.html"
}

def WipeFinalDir():
    if not PathExists(BUILD_DIRECTORY):
        CreateDirectory(BUILD_DIRECTORY)
    for item in ListDirectory(BUILD_DIRECTORY):
        path = BUILD_DIRECTORY + "/" + item
        if IsFile(path):
            DeleteFile(path)
            continue
        DeleteDirectory(path)

def PostSortHelper(Post):
    return datetime.strptime(Post["date"], "%Y %b %d")

def GetBlogList():
    PostSlugs = ListDirectory("blog-posts")
    Posts = []
    for slug in PostSlugs:
        with open("blog-posts/" + slug, encoding="utf-8") as MDFile:
            PostHTML = RenderMarkdown(MDFile.read())
            Item = PostHTML.metadata
            Item["content"] = PostHTML
            Item["pathname"] = slug.replace(".md", ".html")
            Posts.append(Item)
    PostsByDate = sorted(Posts, key=PostSortHelper, reverse=True)
    return PostsByDate

PostList = GetBlogList()

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
            RenderedHTML = RenderTemplate("blog-post.html", Title=Title, PostDate=PostDate, Content=PostHTML, PostPath=PostPath, PlaintextPath=PlaintextPath)
        with open(BUILD_DIRECTORY + "/blog/" + PostPath, "w", encoding="utf-8") as PostPlaintext:
            PostPlaintext.write(RenderedHTML)
        with open(BUILD_DIRECTORY + "/blog/" + PlaintextPath, "w", encoding="utf-8") as PostPlaintext:
            PostPlaintext.write(PostMD)

def RenderPage(PageInput: str, ContentDest: str, **kwargs):
    with open(BUILD_DIRECTORY + "/" + ContentDest, "w", encoding="utf-8") as DestLocation:
        DestLocation.write(RenderTemplate(PageInput, **kwargs))

if __name__ == "__main__":
    print("Wiping directory")
    WipeFinalDir()
    print("Creating blog holder")
    CreateDirectory(BUILD_DIRECTORY + "/blog")
    print("Rendering posts")
    RenderPosts()
    print("Copying static directory")
    CopyDirectory("static", BUILD_DIRECTORY)

    print("Building pages")
    for file, path in PAGES.items():
        RenderPage(file, path, PostList=PostList)

    pass