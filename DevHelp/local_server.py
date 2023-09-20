from flask import Flask, send_file as SendFile
from os.path import exists as PathExists, join as JoinPath

app = Flask(__name__)

@app.route("/")
def Index():
    return SendFile("index.html")

@app.route("/<path:path>")
def Other(path):
    FindFile = JoinPath("..", path).replace("\\", "/")
    print(FindFile)
    if PathExists(FindFile):
        return SendFile(FindFile)
    return SendFile("../404.html"), 404

if __name__ == "__main__":
    app.run("0.0.0.0", 9000, debug=True)