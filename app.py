from flask import Flask, render_template

app = Flask(__name__)

# POSTS MOCK
posts= [
    {
        "titulo": "Post 1",
        "texto":"Meu primeiro post"
    },
    {
        "titulo": "Post 2",
        "texto":"Meu segundo post"
    }
]

@app.route('/')
def hello():
    return render_template("estrutura.html", entradas =posts)


@app.route('/pudim')
def pudim():
    return "General Kenobi!"