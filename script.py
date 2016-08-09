from flask import Flask, render_template, request, url_for, redirect
import logging
import requests


app = Flask(__name__)


class SpaceHandler(logging.Handler):

    def __init__(self, url, *args, **kwargs):
        self.url = url

    def emit(self, record):
        requests.post(self.url, data=record)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        text = request.form['text']
        with open('1.txt', 'w', encoding='utf-8') as f:
            f.write(text)
            f.close()
        return redirect(url_for('result', text=text))


@app.route('/result/<text>', methods=['GET', 'POST'])
def result(text):
    return render_template("result.html", text=text)


if __name__ == "__main__":

    app.run(debug=True)