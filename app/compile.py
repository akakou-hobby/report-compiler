import tempfile
import subprocess
import shutil
import threading

TIMEOUT = 60


class ReportCompiler:
    def __init__(self):
        self.txt_fp = tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".md")

        self.pdf_fp = tempfile.TemporaryDirectory()
        self.pdf_path = self.pdf_fp.name + '/report.pdf'
        self.cmd = f'pandoc -F pandoc-crossref {self.txt_fp.name} -o {self.pdf_path} --pdf-engine lualatex -V luatexjapresetoptions=ipa -N'

    def compile(self, code):
        self.txt_fp.write(code)
        self.txt_fp.flush()

        err = ''
        output = ''

        try:
            print('compile start...')
            print(f'cmd: {self.cmd}')
            process = subprocess.run(
                self.cmd.split(' '),
                capture_output=True,
                encoding='utf-8',
                timeout=TIMEOUT)

            print('compile end...')
            output = process.stdout + '\n'
            err = process.stderr + '\n'

        except subprocess.TimeoutExpired as e:
            err += 'Timed out'

        except Exception as e:
            err += f'{e}'

        msg = f'Output: {output}\nError: {err}\n'

        return msg

    def finalize(self, dest_dir):
        shutil.copy(self.pdf_path, dest_dir)

        # self.txt_fp.close()
        # self.pdf_fp.close()


class AsyncReportCompiler(ReportCompiler):
    def async_compile(self, code):
        self.thread = threading.Thread(
            target=self._async_compile, args=(code,))
        self.thread.start()

    def _async_compile(self, code):
        self.result = self.compile(code)

    def await_compile(self):
        self.thread.join()
        return self.result
