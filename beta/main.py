from flask import Flask, request

app = Flask(__name__)
name = "Rielly H. Young | Software Developer"


def generate_head():
    return """<head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>RHY</title>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
                <style>
                    body {
                        background-color: #ebdbb2;
                        font-style: normal;
                        font-family: Menlo,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New,monospace,serif;
                    }
                    .container {
                        width: 85%;
                        margin: 10 auto;
                        padding: 30px;
                        background-color: #ffffff;
                    }
                    .project {
                        width: 85%;
                        margin: 50 auto;
                        padding: 30px;
                        background-color: #ffffff;
                    }
                    .nav {
                        padding: 10px 0;
                        margin-bottom: 20px;
                    }
                    .nav-title {
                        color: #fabd2f;
                        margin: 0;
                    }
                    .nav ul {
                        list-style-type: none;
                        padding: 0;
                        margin: 0;
                    }
                    .nav ul li {
                        display: inline;
                        margin-right: 10px;
                    }
                    .nav ul li a {
                        color: #83a598;
                        text-decoration: none;
                    }
                    .nav ul li a:hover {
                        text-decoration: underline;
                    }

                    }
                </style>
            </head>"""


def generate_header(name):
    head = generate_head()
    return (
        f"""{head}
        <header class = "nav">
            <h1>{name}</h1>
            <nav>
                <a href="/">Home</a> | 
                <a href="/blog">Blog</a> |
                <a href="/projects">Projects</a> |
                <a href="/links">Links</a> |
                <a href="/contact">Contact</a>
            </nav>
        </header>
        """
    )


def generate_contact_form():
    return f"""
        <form action="/submit_contact" method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    """


@app.route("/")
def index():
    header = generate_header(name)
    return f"""{header}
            <div class="container">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus commodo urna sit amet turpis consequat, eget efficitur velit dapibus.</p>
                <p>Phasellus et nisi ut quam fermentum vehicula. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin ultrices euismod dui, vel ultrices massa vestibulum ac.</p>
                <p>Donec eget efficitur metus. Maecenas aliquet sapien id efficitur suscipit. In hac habitasse platea dictumst. Duis at sodales enim. Sed non placerat lacus.</p>
                <p>Suspendisse et ante vel mauris viverra vehicula. Integer auctor odio in quam dictum, vel fermentum sapien condimentum.</p>
                <p>Curabitur ut leo varius, ultricies ligula non, vestibulum ligula. Maecenas consequat, turpis eget dapibus aliquam, ligula magna sagittis justo, sed faucibus sem orci vel odio.</p>
            </div>"""


@app.route("/blog")
def blog_page():
    header = generate_header(name)
    return f"{header}<ul><li>Blog one</li><li>Blog two</li><li>Blog etc</li></ul>"


@app.route("/links")
def links_page():
    header = generate_header(name)
    return f"{header}<ul><li><a href='https://www.github.com/deepwaterpaladin'>Github</a></li><li><a href='https://www.twitter.com/riellyyoung'>Twitter</a></li></ul>"


@app.route("/contact")
def contact_page():
    header = generate_header(name)
    form = generate_contact_form()
    return f"{header}{form}"


@app.route("/projects")
def projects_page():
    header = generate_header(name)
    return f"""{header}
            <div class="project">
                <h2>Tweeting your way to Parliament: Quantitative Analysis of Twitter use in the 2022 Ontario Provincial Election (June, 2022)</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus commodo urna sit amet turpis consequat, eget efficitur velit dapibus.</p>
                <p>Phasellus et nisi ut quam fermentum vehicula. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin ultrices euismod dui, vel ultrices massa vestibulum ac.</p>
                <p>Donec eget efficitur metus. Maecenas aliquet sapien id efficitur suscipit. In hac habitasse platea dictumst. Duis at sodales enim. Sed non placerat lacus.</p>
                
            </div>
            <div class="project">
                <h2>One-Time-Pad Encryption Application (May 2022)</h2>
                <p>A one-time-pad is a type of encryption that is used to hide the contents of a message. Each letter in the encrypted phrase has a corresponding "one-time-pad" number. </p>
                <p>This number is then used to decrypt the message. Each one-time-pad number is a random number, and thus is impossible to guess and is theoretically impossible to crack by brute force. One-time-pads are used to hide messages in email, chat, and other online communication.</p>
                <p>The sample application uses TKinter for a simplified GUI. Source code can be found <a href="https://github.com/deepwaterpaladin/encryption_application">here</a>.</p>
            </div>
            """


@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    header = generate_header(name)
    req_name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    # Handle form submission (e.g., send email, save to database, etc.)
    print(f"Contact form submission received from {req_name}")
    return f"""{header}Thank you, {req_name}, for your message. We will get back to you soon!"""


if __name__ == "__main__":
    app.run(debug=True)
