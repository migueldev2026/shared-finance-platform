from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "shared-finance-platform"
    }


if __name__ == "__main__":
    app.run(debug=True)