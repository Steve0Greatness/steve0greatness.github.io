from flask import Flask, send_file as SendFile
from os.path import exists as PathExists, join as JoinPath, isfile
from os import getcwd

app = Flask(__name__)

@app.route("/")
def Index():
    return SendFile("../index.html")

@app.route("/<path:path>")
def Other(path):
    FindFile = JoinPath(getcwd(), path).replace("\\", "/")
    if not isfile(FindFile):
        return SendFile(JoinPath(FindFile, "index.html").replace("\\", "/"))
    elif PathExists(FindFile):
        return SendFile(FindFile)
    return SendFile("../404.html"), 404

if __name__ == "__main__":
    app.run("0.0.0.0", 9000, debug=True)