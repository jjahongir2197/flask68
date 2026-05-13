from flask import Flask, send_file

app = Flask(__name__)

@app.route("/download")
def download():

    return send_file(
        "sample.txt",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)
