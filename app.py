from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """Renders the main page of the website."""
    return render_template('index.html')

@app.route("/galeri")
def galeri():
    """Renders the gallery page of the website."""
    return render_template('galeri.html')

if __name__ == "__main__":
    app.run(debug=False)