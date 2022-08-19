from flask import Flask, render_template, request
from requests import get

server = Flask(__name__)


@server.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        word = request.form["word"]
        response = get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 404:
            return response.json()
        else:
            meanings = response.json()[0]["meanings"]
            meanings_minimal = list()
            for i in range(0, len(meanings)):
                meanings_minimal.append(
                    meanings[i]['definitions'][0]['definition'])
            return render_template("result.djhtml", meanings_min=meanings_minimal)
    return render_template("home.djhtml", title="Search Word")


if __name__ == "__main__":
    server.run(debug=True)
