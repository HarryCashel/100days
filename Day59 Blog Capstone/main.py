from flask import Flask, render_template, request
import requests

app = Flask(__name__)

blog_posts = requests.get("https://api.npoint.io/07418da7883f0f7ed143").json()


@app.route("/index.html")
@app.route("/")
def home():
    return render_template("index.html", all_posts=blog_posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"



@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    requested_post = None
    for blog in blog_posts:
        if blog["id"] == blog_id:
            requested_post = blog
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
