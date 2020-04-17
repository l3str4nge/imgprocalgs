import threading
import webbrowser

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


def run_server(host: str, port: int):
    app.run(host, port)


def open_website(url):
    webbrowser.get(using='windows-default').open(url)


if __name__ == '__main__':
    _host, _port = "127.0.0.1", 8000
    threading.Timer(0.25, open_website, [f"http://{_host}:{_port}"]).start()
    run_server(_host, _port)
