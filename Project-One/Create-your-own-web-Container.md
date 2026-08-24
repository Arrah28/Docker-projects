Project One: Containerising a Flask App with Docker
A hands-on project to learn the fundamentals of Docker containerisation by packaging a custom Python Flask web dashboard into an isolated container.

Prerequisites
Python 3.x installed on your machine (python --version)
Docker Desktop installed and running
Git configured for version control
Step 1: Create the Flask Web Application
Create and navigate into a new directory for your project:
Bash
mkdir project_one_flask
cd project_one_flask
Install Flask using pip:
Bash
pip3 install flask
Create your main application file:
Bash
touch app.py
Add the following code into app.py. (Note: Using host='0.0.0.0' is crucial so the app can accept external network requests from outside the Docker container).
Python
from flask import Flask, render_template_string

app = Flask(__name__)

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
                <li><strong>No Guest OS:</strong> This app shares your host machine's kernel instead of running a heavy virtualized OS.</li>
                <li><strong>Process Level:</strong> The Flask server runs as a single isolated process inside a secure sandbox.</li>
                <li><strong>Port Mapping:</strong> Network traffic was successfully routed from the host machine into port <code>5002</code> inside the container.</li>
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
    app.run(host='0.0.0.0', port=5002)
Test the app locally before containerising:
Bash
python3 app.py
Step 2: Write the Dockerfile
Create a Dockerfile in the root of your project directory:

Bash
touch Dockerfile
Paste the following instructions into your Dockerfile:

Dockerfile
# Use lightweight official Python runtime as base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy local project files into the container working directory
COPY . .

# Install dependencies
RUN pip install flask

# Document the port the container listens on
EXPOSE 5002

# Specify the command to run the application when the container starts
CMD ["python", "app.py"]
Step 3: Build the Docker Image
Build your read-only immutable image from the Dockerfile (don't forget the . at the end representing the current directory):

Bash
docker build -t project_one_flask .
Step 4: Run and Manage the Container
Spin up a container in detached mode (-d) with port mapping (-p):
Bash
docker run -d -p 5002:5002 project_one_flask
-d: Runs the container in the background.
-p 5002:5002: Maps port 5002 on your host machine to port 5002 inside the container.
Verify active containers:
Bash
docker ps
Open in your browser:
Navigate to http://localhost:5002 to see your live containerised dashboard!
Stop the container:
Bash
docker stop <CONTAINER_ID>
Step 5: Push to GitHub via VS Code Terminal
Initialize version control, commit your changes, and push your repository to GitHub:

Bash
git init
git add .
git commit -m "Add Flask Docker learning dashboard app and Dockerfile"
git remote add origin https://github.com/Arrah28/Docker-projects.git
git branch -M main
git push -u origin main
