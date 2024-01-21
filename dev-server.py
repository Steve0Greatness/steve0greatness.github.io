from build import main as BuildStaticSite
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def Index():
    return """<a href="/build">Rebuild site</a>"""

@app.route("/build")
def Builder():
    BuildStaticSite()
    return redirect("/")

if __name__ == "__main__":
    app.run("0.0.0.0", 9000, debug=True)