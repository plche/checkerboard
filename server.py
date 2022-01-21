from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def draw():
    return render_template("index.html", cols=8, rows=8, clr1="#ff0000", clr2="#000000")

@app.route("/<int:rows>")
def drawr(rows):
    return render_template("index.html", cols=8, rows=rows, clr1="#ff0000", clr2="#000000")

@app.route("/<int:cols>/<int:rows>")
def drawrc(cols, rows):
    return render_template("index.html", cols=cols, rows=rows, clr1="#ff0000", clr2="#000000")

@app.route("/<int:cols>/<int:rows>/<string:clr1>/<string:clr2>")
def drawrccc(cols, rows, clr1, clr2):
    return render_template("index.html", cols=cols, rows=rows, clr1=clr1, clr2=clr2)

if __name__ == "__main__":
    app.run(debug=True)