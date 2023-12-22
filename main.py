from Renderers import RenderTemplate, RenderMarkdown

from shutil import rmtree as DeleteDirectory
from os import mkdir as CreateDirectory, listdir as ListDirectory, unlink as DeleteFile
from os.path import isfile as IsFile
from distutils.dir_util import copy_tree as CopyDirectory

def WipeDocsDir():
    for item in ListDirectory("docs"):
        path = "docs/" + item
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
        with open("docs/blog/" + post.replace(".md", ".html"), "w") as PostLocation:
            PostLocation.write(RenderedHTML)

def RenderPage(PageInput: str, ContentDest: str, **kwargs):
    with open("docs/" + ContentDest, "w") as DestLocation:
        DestLocation.write(RenderTemplate(PageInput, **kwargs))

if __name__ == "__main__":
    WipeDocsDir()
    CreateDirectory("docs/blog")
    RenderPosts()
    CopyDirectory("static", "docs/static")

    RenderPage("index.html", "index.html", PostList=PostList)
    RenderPage("index.html", "index.html", PostList=PostList)

    pass