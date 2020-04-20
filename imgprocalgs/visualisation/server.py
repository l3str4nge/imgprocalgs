""" Flask application definition for algorithm visualisation"""

import threading
import webbrowser
import os
from flask import Flask

from imgprocalgs.visualisation.views import TemplateView


class App:
    """"
    Application reprentation

    Simple usage in this project:

    1. Run one of available algorithm with visualisation option
    2. Put following code:
    >>> app = App()
    >>> app.register_route(path="/", **{})
    >>> app.run_server('host', 8000, open_website=True or False)
    """

    DEFAULT_BROWSER = 'windows-default'
    STATIC_FOLDER = os.path.join(os.path.abspath(os.curdir), 'data')
    STATIC_URL = "/data"

    def __init__(self):
        self.app = Flask(__name__, static_folder=self.STATIC_FOLDER, static_url_path=self.STATIC_URL)
        self.routes = []

    def run_server(self, host: str, port: int, open_webiste=False):
        if open_webiste:
            threading.Timer(0.25, self.open_website, [f"http://{host}:{port}"]).start()

        self.app.run(host, port)

    def open_website(self, url):
        webbrowser.get(using=self.DEFAULT_BROWSER).open(url)

    def register_route(self, path: str, template_name: str, **kwargs):
        route = TemplateView(template_name, **kwargs)
        self.app.route(path)(route.as_view)


if __name__ == '__main__':
    app = App()
    app.register_route("/", template_name='main_page.html', title="Main title2", header="Main header")
    app.run_server("127.0.0.1", 8000, open_webiste=True)
