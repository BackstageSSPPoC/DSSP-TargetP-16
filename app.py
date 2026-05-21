from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Python Web App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding-top: 100px;
                }

                .container {
                    background: white;
                    width: 500px;
                    margin: auto;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
                }

                h1 {
                    color: #2c3e50;
                }

                p {
                    font-size: 20px;
                    color: #27ae60;
                }
            </style>
        </head>

        <body>
            <div class="container">
                <h1>Hello GSPANN From DSSP Portal</h1>
                <p>Pipeline Test Successful</p>
            </div>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "UP"
    }

if __name__ == "__main__":
    print("[LOG] Flask App Started")
    app.run(host="0.0.0.0", port=5000)
