from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/hello", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form["name"]
        return f"Hello, {name}"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    # サーバ立ち上げ
    app.run(
        host="0.0.0.0",
        port=5000)
