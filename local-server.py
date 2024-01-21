# This is a debugging server used for site development, it's not used on the actual site.

from flask import Flask, send_file as SendFile
from os.path import isfile
from pathlib import Path

FlaskOpts = {}
app = Flask(__name__, **FlaskOpts)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def SendStatic(path):
    if isfile("build/" + path):
        return SendFile(Path("build").joinpath(path))
    elif isfile(Path("build").joinpath(path, "index.html")):
        return SendFile(Path("build").joinpath(path, "index.html"))
    return SendFile("build/404.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 8000, debug=True)