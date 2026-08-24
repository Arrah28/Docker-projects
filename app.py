from flask import Flask, render_template_string

app = Flask(__name__)

# A clean, single-page dashboard explaining Docker
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker Learning Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; color: #333; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        h1 { color: #0db7ed; text-align: center; }
        .badge { background: #0db7ed; color: white; padding: 5px 10px; border-radius: 4px; font-size: 12px; font-weight: bold; }
        .card { background: #eef2f7; padding: 15px; border-left: 5px solid #0db7ed; margin: 15px 0; border-radius: 4px; }
        ul { padding-left: 20px; }
        li { margin-bottom: 8px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Inside the Container Dashboard</h1>
        <p style="text-align: center;"><span class="badge">STATUS: RUNNING LIVE IN A DOCKER CONTAINER</span></p>
        
        <p>If you can read this in your browser, your Flask app has successfully been packaged, built into an image, and spun up as an isolated container!</p>

        <div class="card">
            <h3>1. Image vs. Container Recap</h3>
            <p><strong>The Image:</strong> The static, read-only blueprint package containing Python and Flask.</p>
            <p><strong>The Container:</strong> This active, running instance with a writable layer executing right now.</p>
        </div>

        <div class="card">
            <h3>2. Why Containers Beat VMs Here</h3>
            <ul>
                <li><strong>No Guest OS:</strong> This app isn't running on a heavy virtualized operating system; it shares your host machine's kernel.</li>
                <li><strong>Process Level:</strong> To your host computer, this Flask server is just a single isolated process running inside a secure sandbox.</li>
                <li><strong>Port Mapping:</strong> Network traffic was routed from your host machine into port <code>5000</code> inside this container.</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    # host='0.0.0.0' allows external Docker networking to reach this app!
    app.run(host='0.0.0.0', port=5002)