from flask import Flask, request, render_template, send_file
import hashlib, subprocess

TIMEOUT = 60
PDF_MIMETYPE = "application/pdf"

app = Flask(__name__)
cmd = 'pandoc -F pandoc-crossref /app/report.md -o /app/report.pdf --pdf-engine lualatex -V luatexjapresetoptions=ipa -N'.split(' ')

def exec(code):
    # save code to file
    filename = 'report.md'
    with open(filename, mode='w') as f:
        f.write(code)

    # run code
    result = ''
    try:
        process = subprocess.run(
                cmd,
                capture_output=True,
                encoding='utf-8',
                timeout=TIMEOUT)

        result = process.stdout
    except subprocess.TimeoutExpired as e:
        result = 'Timed out'

    return result


@app.route("/hello", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form["code"]
        result = exec(code)
        
        filename = "report.pdf"

        return send_file(filename, as_attachment = True, \
            attachment_filename = filename, \
            mimetype = PDF_MIMETYPE)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    # サーバ立ち上げ
    app.run(
        host="0.0.0.0",
        port=5000)
