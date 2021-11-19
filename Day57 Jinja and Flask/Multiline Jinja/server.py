from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog/<idd>")
def blog(idd):
    blog_url = "https://api.npoint.io/60f451367a93defd85d2"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, id=idd)


if __name__ == "__main__":
    app.run(debug=True)
