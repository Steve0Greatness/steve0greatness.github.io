from build import main as BuildStaticSite, PostList
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def Index():
    return """<a href="/build">Rebuild site</a>"""

@app.route("/blog-list")
def Writer():
    BlogListHTML = "<br/>".join(("<a href=\"/edit/%s\">%s</a>" % (post["origin"], post["title"]) for post in PostList))
    return """<a href="/new-post">+</a><hr/>%(listing)s""" % { "listing": BlogListHTML }

@app.route("/edit/<post>")
def Editor(post: str):
    BlogListDict = { PostObj["origin"]: PostObj for PostObj in PostList }
    if post not in BlogListDict:
        return redirect("/")
    return """"""

@app.route("/new-post")
def NewPost():
    return """"""

@app.route("/build")
def Builder():
    BuildStaticSite()
    return redirect("/")

if __name__ == "__main__":
    app.run("0.0.0.0", 9000, debug=True)