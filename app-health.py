from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>SecureHealth Portal</title>
    </head>
    <body style="background:#f0f4f8;font-family:Arial;margin:0;padding:0">
        <div style="background:#1a5276;color:white;padding:20px 40px;display:flex;align-items:center;gap:15px">
            <span style="font-size:2rem">🏥</span>
            <div>
                <h1 style="margin:0;font-size:1.5rem">SecureHealth Patient Portal</h1>
                <p style="margin:0;font-size:0.85rem;opacity:0.8">Protected by DevSecOps Pipeline</p>
            </div>
        </div>
        <div style="padding:40px;max-width:900px;margin:auto">
            <div style="background:white;border-radius:12px;padding:25px;margin-bottom:20px;border-left:5px solid #27ae60">
                <h2 style="color:#27ae60;margin:0 0 10px">✅ System Status: Secure</h2>
                <p style="color:#555;margin:0">All security checks passed. Deployment approved.</p>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;margin-bottom:20px">
                <div style="background:white;border-radius:12px;padding:20px;text-align:center">
                    <div style="font-size:2rem">🔍</div>
                    <h3 style="color:#1a5276;margin:10px 0 5px">Trivy Scan</h3>
                    <p style="color:#27ae60;font-weight:bold;margin:0">PASSED</p>
                    <p style="color:#888;font-size:0.8rem">No critical vulnerabilities</p>
                </div>
                <div style="background:white;border-radius:12px;padding:20px;text-align:center">
                    <div style="font-size:2rem">🔐</div>
                    <h3 style="color:#1a5276;margin:10px 0 5px">RBAC</h3>
                    <p style="color:#27ae60;font-weight:bold;margin:0">ENABLED</p>
                    <p style="color:#888;font-size:0.8rem">Access control active</p>
                </div>
                <div style="background:white;border-radius:12px;padding:20px;text-align:center">
                    <div style="font-size:2rem">🛡️</div>
                    <h3 style="color:#1a5276;margin:10px 0 5px">HIPAA</h3>
                    <p style="color:#27ae60;font-weight:bold;margin:0">COMPLIANT</p>
                    <p style="color:#888;font-size:0.8rem">Patient data protected</p>
                </div>
            </div>
            <div style="background:white;border-radius:12px;padding:25px">
                <h3 style="color:#1a5276;margin:0 0 15px">🔒 Security Pipeline Stages</h3>
                <div style="display:flex;flex-direction:column;gap:10px">
                    <div style="display:flex;align-items:center;gap:10px;padding:10px;background:#f9f9f9;border-radius:8px">
                        <span style="color:#27ae60;font-size:1.2rem">✅</span>
                        <span>Docker Image Built</span>
                    </div>
                    <div style="display:flex;align-items:center;gap:10px;padding:10px;background:#f9f9f9;border-radius:8px">
                        <span style="color:#27ae60;font-size:1.2rem">✅</span>
                        <span>Trivy Vulnerability Scan — No Critical Issues</span>
                    </div>
                    <div style="display:flex;align-items:center;gap:10px;padding:10px;background:#f9f9f9;border-radius:8px">
                        <span style="color:#27ae60;font-size:1.2rem">✅</span>
                        <span>RBAC Applied — Role Based Access Control Active</span>
                    </div>
                    <div style="display:flex;align-items:center;gap:10px;padding:10px;background:#f9f9f9;border-radius:8px">
                        <span style="color:#27ae60;font-size:1.2rem">✅</span>
                        <span>Deployed to Kubernetes Successfully</span>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)