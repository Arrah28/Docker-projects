from flask import Flask, render_template_string
import redis

app = Flask(__name__)

# Helper function to connect to the Redis container via Docker DNS
def get_redis_client():
    try:
        # Pass assword parameter to match docker-compose configuration
        client = redis.Redis(
            host='redis', 
            port=6379, 
            password='my-secret-pw', 
            socket_connect_timeout=2
        )
        client.ping()
        return client
    except Exception:
        return None

# An enhanced, professional dashboard updated for Flask-Redis Multi-Container Project
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask & Redis Multi-Container Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; color: #333; margin: 0; padding: 30px; }
        .container { max-width: 850px; margin: auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 6px 20px rgba(0,0,0,0.08); }
        h1 { color: #0db7ed; text-align: center; margin-top: 0; }
        .badge-container { text-align: center; margin-bottom: 25px; }
        .badge { background: #0db7ed; color: white; padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: bold; letter-spacing: 1px; text-transform: uppercase; display: inline-block; margin: 4px; }
        .redis-badge { background: #dc382c; }
        .card { background: #f8fafc; padding: 20px; border-left: 5px solid #0db7ed; margin: 20px 0; border-radius: 6px; border: 1px solid #e2e8f0; border-left-width: 5px; }
        .redis-card { border-left-color: #dc382c; background: #fff5f5; text-align: center; }
        .counter-number { font-size: 36px; font-weight: bold; color: #dc382c; margin: 10px 0; }
        h3 { margin-top: 0; color: #1e293b; }
        ul { padding-left: 20px; margin-bottom: 0; }
        li { margin-bottom: 8px; }
        code { background: #e2e8f0; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px; color: #d97706; }
        .nav-links { text-align: center; margin-top: 15px; }
        .nav-links a { color: #0db7ed; text-decoration: none; font-weight: bold; margin: 0 10px; }
        .nav-links a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Flask & Redis Multi-Container Dashboard</h1>
        <div class="badge-container">
            <span class="badge">APP: RUNNING LIVE IN DOCKER</span>
            <span class="badge redis-badge">DB: CONNECTED TO REDIS</span>
        </div>
        
        <p style="text-align: center; color: #64748b;">{{ message }}</p>

        <div class="nav-links">
            <a href="/">Home Route (/)</a> | <a href="/count">Visit Counter Route (/count)</a>
        </div>

        {% if show_counter %}
        <!-- Redis Counter Card -->
        <div class="card redis-card">
            <h3>🔴 Live Redis Visit Counter</h3>
            <p>This counter value is stored persistently inside your Redis container memory cache:</p>
            <div class="counter-number">{{ count }}</div>
            <p><small>Refresh this page to watch the hit count increment instantly!</small></p>
        </div>
        {% endif %}

        <div class="card">
            <h3>1. Multi-Container Orchestration (Docker Compose)</h3>
            <p><strong>Service Linking:</strong> The Flask application container communicates directly with the Redis container via internal Docker network DNS using host <code>redis</code>.</p>
            <p><strong>Isolated Services:</strong> Both containers run from separate dedicated Dockerfiles managed concurrently through a single configuration stack.</p>
        </div>

        <div class="card">
            <h3>2. Key Project Architecture Highlights</h3>
            <ul>
                <li><strong>Flask Web Application:</strong> Exposes route <code>/</code> for a welcome view and route <code>/count</code> for stateful Redis tracking.</li>
                <li><strong>Redis Key-Value Database:</strong> Acts as an in-memory database keeping state across container requests.</li>
                <li><strong>Port Mapping:</strong> Traffic routes smoothly from your host browser into port <code>5003</code> inside the isolated Flask container sandbox.</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_PAGE, 
        message="Welcome to your multi-container Flask application! Navigate to the counter route to test live Redis integration.",
        show_counter=False
    )

@app.route('/count')
def count():
    r = get_redis_client()
    visit_count = 0

    if r:
        try:
            # Increment the visit count key in Redis
            visit_count = r.incr('visits')
        except Exception as e:
            visit_count = f"Error incrementing key: {e}"
    else:
        visit_count = "Redis Connection Failed"

    return render_template_string(
        HTML_PAGE, 
        message="Live connection established! Your visit count is successfully incrementing and reading from the Redis database container.",
        show_counter=True,
        count=visit_count
    )

if __name__ == '__main__':
    # host='0.0.0.0' allows external Docker bridge networking to reach this app!
    app.run(host='0.0.0.0', port=5003)
