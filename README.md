# 📦 Flask CI/CD Project

This project demonstrates setting up a Flask application with a complete CI/CD pipeline using GitHub Actions. It automates the process of building, containerizing, and deploying the application from GitHub to a live EC2 instance.

---

## 🚀 Features

- **Flask Web Application**: A simple Python-based web application.
- **GitHub Actions for CI/CD**: Automates testing and deployment.
- **Docker Integration**: The app is containerized for consistency across environments.
- **Continuous Integration**: Pushes Docker images to Docker Hub.
- **Continuous Deployment**: Automatically deploys the Docker image to an EC2 server via SSH.

---

## ⚙️ Prerequisites

- **Python 3.x**  
- **pip**  
- **Docker**  
- **GitHub Repository**  
- **Docker Hub Account**  
- **AWS EC2 Instance** with Docker installed  
- **SSH Access** to the EC2 instance

---

## 🔧 Setup Instructions

### Local Development

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd flask-cicd
    ```

2. **(Optional) Set up virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application locally:**
    ```bash
    flask run
    ```
    The app runs at `http://127.0.0.1:5000`.

---

## 🐳 Docker Setup

```bash
# Build the image
docker build -t <your-dockerhub-username>/flask-cicd .

# Run the container
docker run -p 5000:5000 <your-dockerhub-username>/flask-cicd

# Push to Docker Hub
docker login
docker push <your-dockerhub-username>/flask-cicd
