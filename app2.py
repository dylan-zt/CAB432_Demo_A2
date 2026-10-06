from random import choice
from flask import Flask, jsonify, request

app = Flask(__name__)

QUESTS = {
    "creative": [
        "Write a six-word story about today.",
        "Draw a logo for an imaginary app.",
        "Invent a new holiday.",
    ],
    "coding": [
        "Add one useful feature to an existing project.",
        "Explain a programming concept without jargon.",
        "Refactor a function to make it easier to read.",
    ],
    "wellbeing": [
        "Take a five-minute screen break.",
        "Drink some water and stretch.",
        "Write down one thing that went well today.",
    ],
}


def get_quest():
    category = request.args.get("category", "random").lower()

    if category == "random":
        category = choice(list(QUESTS))

    if category not in QUESTS:
        category = "creative"

    return category, choice(QUESTS[category])


@app.route("/")
def home():
    return """
    <!doctype html>
    <html>
      <head>
        <title>Daily Quest</title>
        <style>
          body {
            font-family: sans-serif;
            max-width: 650px;
            margin: 60px auto;
            padding: 20px;
            background: #eef2ff;
            color: #172554;
          }
          .card {
            background: white;
            padding: 28px;
            border-radius: 16px;
            box-shadow: 0 8px 25px #0002;
          }
          a {
            color: white;
            background: #4f46e5;
            padding: 10px 14px;
            border-radius: 8px;
            text-decoration: none;
          }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>🌟 Daily Quest</h1>
          <p>Get a small challenge to make today more interesting.</p>
          <p><a href="/quest">Give me a quest</a></p>
          <p>Try <code>/quest?category=coding</code>.</p>
          <p>API: <code>/api/quest</code></p>
        </div>
      </body>
    </html>
    """


@app.route("/quest")
def quest():
    category, text = get_quest()
    return f"""
    <h1>🎯 {category.title()} Quest</h1>
    <p>{text}</p>
    <a href="/quest">Another quest</a>
    """


@app.route("/api/quest")
def quest_api():
    category, text = get_quest()
    return jsonify(category=category, quest=text)


@app.route("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
