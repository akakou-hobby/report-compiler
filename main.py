from app.api import Api
import webview

DEBUG = False


def main():
    api = Api()
    window = webview.create_window('Reports', 'templates/index.html',
                                   js_api=api, min_size=(600, 450))
    api.window = window

    webview.start(http_server=False, debug=DEBUG)


if __name__ == '__main__':
    main()
