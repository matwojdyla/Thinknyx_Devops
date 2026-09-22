from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello and Welcome to the Thinknyx Devops Associate Program!"

@app.route("/services")
def service():
    return "Version 1 work in progress."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)