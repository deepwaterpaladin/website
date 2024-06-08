from flask import Flask, render_template
import json

app = Flask(__name__)
name = "Rielly H. Young | Software Developer"
with open('./posts.json', 'r') as f:
    posts = json.load(f)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cv")
def cv():
    return render_template('cv.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/blog")
def blog():
    return render_template('blog.html', posts=posts)

@app.route('/blog/<string:post_id>')
def post(post_id):
    p = next((post for post in posts if post['id'] == post_id), None)
    if p is None:
        return render_template('404.html')
    return render_template('post.html', post=p)


if __name__ == "__main__":
    app.run()
