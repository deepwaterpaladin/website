from flask import Flask, request, render_template

application = Flask(__name__)
name = "Rielly H. Young | Software Developer"


def generate_head():
    return """<head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Rielly H. Young</title>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
                <style>
                    body {
                        background-color: #ebdbb2;
                        font-style: normal;
                        font-family: Menlo,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New,monospace,serif;
                    }
                    .container {
                        width: 85%;
                        margin: auto;
                        padding: 30px;
                        background-color: #ffffff;
                    }
                    .project {
                        width: 85%;
                        margin: auto;
                        padding: 30px;
                        background-color: #ffffff;
                    }
                    .block{
                        background-color: #ebdbb2;
                    }
                    .nav {
                        padding: 10px 0;
                        margin: 15px;
                    }
                    .nav-title {
                        color: hsl(0, 0%, 0%);
                        margin: 15px;
                    }
                    .nav ul {
                        list-style-type: none;
                        padding: 0;
                        margin: 0;
                    }
                    .nav ul li {
                        display: inline;
                        margin-right: 9px;
                    }
                    .nav ul li a {
                        color: hwb(211 30% 18%);
                        text-decoration: none;
                    }
                    .nav ul li a:hover {
                        text-decoration: underline;
                    }
                    table {
                        border-collapse: collapse;
                        width: 100%;
                    }

                    th, td {
                        border: 1px solid #dddddd;
                        text-align: left;
                        padding: 8px;
                    }

                    th {
                        background-color: #f2f2f2;
                    }
                    .form {
                        width: 96%;
                        margin: auto;
                    }
                </style>
            </head>"""


def generate_header(name):
    head = generate_head()
    return (
        f"""{head}
        <header class = "nav">
            <h1 class="nav-title">Rielly H. Young  | Software Developer</h1>
        <nav class="nav">
            <ul>
                <li><a href="/">Home</a> | </li>
                <li><a href="/blog">Blog</a> |</li>
                <li><a href="/projects">Projects</a> |</li>
                <li><a href="/links">Links</a> |</li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
        </header>
        """
    )


def generate_contact_form():
    return f"""
        <form action="/submit_contact" method="post" class="form">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    """

@application.route("/")
def index():
    return render_template('index.html')

@application.route("/blog")
def wip_redirect():
    return render_template('wip.html')

# @application.route("/blog")
# def blog_page():
#     return render_template('blog.html')

@application.route("/links")
def links_page():
    return render_template('links.html')

@application.route("/cv")
def cv_page():
    return render_template('cv.html')


@application.route("/projects")
def projects_page():
    return render_template('projects.html')


@application.route("/submit_contact", methods=["POST"])
def submit_contact():
    header = generate_header(name)
    req_name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    # Handle form submission (e.g., send email, save to database, etc.)
    print(f"Contact form submission received from {req_name}")
    return f"""{header}Thank you, {req_name}, for your message. We will get back to you soon!"""


if __name__ == "__main__":
    application.run(debug=True)
