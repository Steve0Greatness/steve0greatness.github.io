from Renderers import RenderTemplate, RenderMarkdown

from shutil import rmtree as DeleteDirectory
from os import mkdir as CreateDirectory, listdir as ListDirectory, unlink as DeleteFile
from os.path import isfile as IsFile
from distutils.dir_util import copy_tree as CopyDirectory

BUILD_DIRECTORY = "build"

def WipeFinalDir():
    for item in ListDirectory(BUILD_DIRECTORY):
        path = BUILD_DIRECTORY + "/" + item
        if IsFile(path):
            DeleteFile(path)
            continue
        DeleteDirectory(path)

def GetBlogList():
    PostSlugs = ListDirectory("blog-posts")
    Posts = []
    for slug in PostSlugs:
        with open("blog-posts/" + slug) as MDFile:
            PostHTML = RenderMarkdown(MDFile.read())
            Item = PostHTML.metadata
            Item["content"] = PostHTML
            Item["pathname"] = slug.replace(".md", ".html")
            Posts.append(Item)
    return Posts

PostList = GetBlogList()

def RenderPosts():
    for post in ListDirectory("blog-posts"):
        path = "blog-posts/" + post
        RenderedHTML: str
        with open(path, "r") as PostContent:
            PostHTML = RenderMarkdown(PostContent.read())
            Title = PostHTML.metadata["title"]
            PostDate = PostHTML.metadata["date"]
            RenderedHTML = RenderTemplate("blog-post.html", Title=Title, PostDate=PostDate, Content=PostHTML)
        with open(BUILD_DIRECTORY + "/blog/" + post.replace(".md", ".html"), "w") as PostLocation:
            PostLocation.write(RenderedHTML)

def RenderPage(PageInput: str, ContentDest: str, **kwargs):
    with open(BUILD_DIRECTORY + "/" + ContentDest, "w") as DestLocation:
        DestLocation.write(RenderTemplate(PageInput, **kwargs))

if __name__ == "__main__":
    WipeFinalDir()
    CreateDirectory(BUILD_DIRECTORY + "/blog")
    RenderPosts()
    CopyDirectory("static", BUILD_DIRECTORY + "/static")

    RenderPage("index.html", "index.html", PostList=PostList)
    RenderPage("blog-list.html", "/blog/index.html", PostList=PostList)
    RenderPage("blog-feed.rss", "/blog/feed.rss", PostList=PostList)
    RenderPage("404.html", "/404.html")

    pass