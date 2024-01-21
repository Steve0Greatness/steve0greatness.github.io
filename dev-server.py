from build import main as BuildStaticSite
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run("0.0.0.0", 9000)