import webview
from .compile import AsyncReportCompiler

FILE_TYPES = ('PDF Files (*.pdf)', 'All files (*.*)')


class Api:
    def __init__(self):
        self.window = None

    def compile(self, code):
        print('start...')
        compiler = AsyncReportCompiler()

        compiler.async_compile(code)

        dest_dir = select_file_path(self.window)
        print('dest: ', dest_dir)

        msg = compiler.await_compile()
        compiler.finalize(dest_dir)
        print('end...')

        return msg


def select_file_path(window):
    dest_dir = window.create_file_dialog(
        webview.SAVE_DIALOG,
        file_types=FILE_TYPES)

    dest_dir = ''.join(dest_dir)
    return dest_dir
