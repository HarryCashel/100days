from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/60f451367a93defd85d2"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts,)


@app.route('/post/<int:blog_id>')
def blog(blog_id):
    blog_url = "https://api.npoint.io/60f451367a93defd85d2"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts, id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)
