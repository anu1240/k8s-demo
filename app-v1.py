from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <body style="background:#1a73e8;color:white;font-family:Arial;text-align:center;padding:100px">
    <h1>🔵 Version 1 — BLUE</h1>
    <p>Current Live Version</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)