# 1. Base Image: Start with a lightweight official Python runtime
FROM python:3.11-slim
# 2. Working Directory: Set the default folder inside the container where commands will run
WORKDIR /Multi-Container-Application
# 3. Copy Files: Copy all files from our local directory into the container's /app directory
COPY . .
# 4. Dependencies: Run pip inside the container to install Flask
RUN pip install flask redis
# 5. Port Document: Document the port the containerized app listens on
EXPOSE 5003
# 6. Execution Command: Tell the container what command to run when it boots up
CMD ["python", "Multi_Container.py"]
