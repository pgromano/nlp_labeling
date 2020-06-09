import flask
import json
import pandas as pd
import warnings

app = flask.Flask(__name__)

IMDB = pd.read_csv("/Users/pablo/Datasets/IMDB Sentiment/imdb.csv", nrows=1000).iterrows()
META = [
    {'key': 'y', 'value': 'positive'},
    {'key': 'n', 'value': 'negative'},
    {'key': '?', 'value': 'unclear'},
]
OUTPUT = '/Users/pablo/TEST.jsonl'


def clean_label_post(label):
    print(label)

    output = {}
    for key, val in label.items():
        new_key = key.split('[')[-1][:-1]
        output[new_key] = val
    return output


@app.route("/", methods=["GET", "POST"])
def index():

    # data index
    label = clean_label_post(flask.request.form.to_dict())

    if len(label) > 0:
        with open(OUTPUT, 'a+') as file:
            file.write(json.dumps(label) + "\n")

    return flask.render_template(
        "index.html", 
        data_text=next(IMDB)[1].text, 
        meta=META,
        meta_len=len(META)
    )


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, use_reloader=True)
