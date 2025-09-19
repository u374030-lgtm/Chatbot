from flask import Flask, render_template, request
from faq_bot import faq_bot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        user_input = request.form["question"]
        answer = faq_bot(user_input)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
