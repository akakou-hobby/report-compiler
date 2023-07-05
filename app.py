import os
import hashlib
import subprocess
import webview
import shutil

TIMEOUT = 60
PDF_MIMETYPE = "application/pdf"

TEXT = "./templates/workspace/report.md"
PDF = "./templates/workspace/report.pdf"

CMD = f'pandoc -F pandoc-crossref {TEXT} -o {PDF} --pdf-engine lualatex -V luatexjapresetoptions=ipa -N'
cmd = CMD.split(' ')

window = None


def compile(code):
    # todo: refactor
    error = ''

    with open(TEXT, mode='w') as f:
        f.write(code)

    try:
        print('compile start...')
        print(f'cmd: {CMD}')
        process = subprocess.run(
            cmd,
            capture_output=True,
            encoding='utf-8',
            timeout=TIMEOUT)

        error = process.stderr
        print('compile end...')

    except subprocess.TimeoutExpired as e:
        print('time out...')
        error = 'Timed out'

    except Exception as e:
        print('error...')
        error = str(e)

    return error


def save_file():
    global window
    file_types = ('PDF Files (*.pdf)', 'All files (*.*)')

    dest_dir = window.create_file_dialog(
        webview.SAVE_DIALOG,
        file_types=file_types)

    dest_dir = ''.join(dest_dir)

    print(f"move file: {dest_dir}")
    shutil.move(PDF, dest_dir)


class Api:
    def compile(self, code):
        print('compile ready...')

        # run code
        error = compile(code)

        if error:
            return error

        save_file()
        return ''


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Reports', 'templates/index.html',
                                   js_api=api, min_size=(600, 450))
    webview.start(http_server=False)
