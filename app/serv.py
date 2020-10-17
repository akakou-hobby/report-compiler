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
    error = ''
    try:
        process = subprocess.run(
                cmd,
                capture_output=True,
                encoding='utf-8',
                timeout=TIMEOUT)

        error = process.stderr
    except subprocess.TimeoutExpired as e:
        error = 'Timed out'

    return error


@app.route("/hello", methods=['GET', 'POST'])
def index():
    code = ''
    error = ''

    if request.method == 'POST':
        code = request.form["code"]
        error = exec(code)
        
        filename = "report.pdf"

        if not error:
            return send_file(filename, as_attachment = True, \
                attachment_filename = filename, \
                mimetype = PDF_MIMETYPE)
    
    return render_template('index.html', code=code, error=error)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000)
