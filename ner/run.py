import flask
import pandas as pd
import warnings

app = flask.Flask(__name__)
IMDB = pd.read_csv("static/imdb.csv", nrows=1000)
DB = {}


@app.route("/", methods=["GET", "POST"])
def index():

    # data index
    current_index = int(flask.request.form.get("current_index", 0))
    first_item = flask.request.form.get("first_item", False)
    prev_item = flask.request.form.get("prev_item", False)
    prev_five_item = flask.request.form.get("prev_five_item", False)
    next_item = flask.request.form.get("next_item", False)
    next_five_item = flask.request.form.get("next_five_item", False)

    if first_item:
        current_index = 0

    if prev_five_item:
        current_index -= 5
        current_index = max([0, current_index])

    if prev_item:
        current_index -= 1
        current_index = max([0, current_index])

    if next_item:
        current_index += 1
        current_index = min([current_index, len(IMDB) - 1])

    if next_five_item:
        current_index += 5
        current_index = min([current_index, len(IMDB) - 1])

    warnings.warn(f"{DB}")
    return flask.render_template(
        "index.html", text=IMDB.iloc[current_index].text, current_index=current_index
    )


if __name__ == "__main__":
    app.run(debug=True)
