from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <body style="background:#2e7d32;color:white;font-family:Arial;text-align:center;padding:100px">
    <h1>🟢 Version 2 — GREEN</h1>
    <p>New Deployment — Zero Downtime!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)