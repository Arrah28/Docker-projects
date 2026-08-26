from flask import Flask, render_template_string
import MySQLdb

app = Flask(__name__)

# An enhanced, professional dashboard explaining Docker, VM vs Container, and Multi-Container Networking
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker & MySQL Learning Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; color: #333; margin: 0; padding: 30px; }
        .container { max-width: 850px; margin: auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 6px 20px rgba(0,0,0,0.08); }
        h1 { color: #0db7ed; text-align: center; margin-top: 0; }
        .badge-container { text-align: center; margin-bottom: 25px; }
        .badge { background: #0db7ed; color: white; padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: bold; letter-spacing: 1px; text-transform: uppercase; }
        .db-badge { background: #28a745; }
        .card { background: #f8fafc; padding: 20px; border-left: 5px solid #0db7ed; margin: 20px 0; border-radius: 6px; border: 1px solid #e2e8f0; border-left-width: 5px; }
        .db-card { border-left-color: #28a745; background: #f0fdf4; }
        h3 { margin-top: 0; color: #1e293b; }
        ul { padding-left: 20px; margin-bottom: 0; }
        li { margin-bottom: 8px; }
        code { background: #e2e8f0; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px; color: #d97706; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Multi-Container Architecture Dashboard</h1>
        <div class="badge-container">
            <span class="badge">APP: RUNNING LIVE IN DOCKER</span>
            <span class="badge db-badge">DB: CONNECTED VIA BRIDGE NETWORK</span>
        </div>
        
        <p style="text-align: center; color: #64748b;">If you see this page, your Flask application container has successfully communicated across a custom Docker bridge network to query an independent MySQL container!</p>

        <!-- New Database Connection Card -->
        <div class="card db-card">
            <h3>🗄️ Live Database Connection Status</h3>
            <p><strong>Target Host:</strong> <code>mydb</code> (Resolved via Docker custom network DNS)</p>
            <p><strong>Live MySQL Version Query:</strong> <code style="color: #16a34a; font-weight: bold;">{{ db_version }}</code></p>
        </div>

        <div class="card">
            <h3>1. Multi-Container Networking & DNS</h3>
            <p><strong>Custom Bridge Network:</strong> Both containers share <code>my-custom-network</code>.</p>
            <p><strong>Container Linking:</strong> Instead of hardcoding IP addresses, Flask uses the container name <code>host="mydb"</code> because Docker's internal DNS handles name resolution automatically.</p>
        </div>

        <div class="card">
            <h3>2. Image vs. Container Recap</h3>
            <p><strong>The Image:</strong> The static, read-only blueprint package containing Python, Flask, and system C-bindings for MySQL.</p>
            <p><strong>The Container:</strong> This active, running instance with a temporary writable layer executing right now.</p>
        </div>

        <div class="card">
            <h3>3. Why Containers Beat VMs Here</h3>
            <ul>
                <li><strong>No Guest OS:</strong> This app shares your host machine's kernel directly instead of booting a heavy virtualized operating system.</li>
                <li><strong>Process Level:</strong> To your host Mac, this Flask server is just a secure, isolated process running inside namespaces and cgroups.</li>
                <li><strong>Port Mapping:</strong> Network traffic was routed cleanly from your physical host machine into port <code>5002</code> inside the app container.</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    db_version = "Unknown"
    try:
        # Connect to MySQL container across the custom bridge network
        db = MySQLdb.connect(
            host="mydb",
            user="root",
            passwd="Arif",
            db="mysql"
        )
        cur = db.cursor()
        cur.execute("SELECT VERSION()")
        row = cur.fetchone()
        db_version = row[0]
        cur.close()
        db.close() # Always close database connections to prevent resource leaks!
    except Exception as e:
        db_version = f"Connection Error: {e}"
        
    return render_template_string(HTML_PAGE, db_version=db_version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)