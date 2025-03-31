# Flask CI/CD Project

This project demonstrates setting up a Flask application with GitHub Actions for a CI/CD pipeline. It automates the process of building, testing, and pushing a Docker image to Docker Hub.

## Features

- **Flask Web Application**: A simple Python-based web application using Flask.
- **GitHub Actions for CI/CD**: Automates building, testing, and deployment.
- **Docker Integration**: The application is containerized using Docker.
- **Automated Testing**: Ensures the application is tested before deployment.
- **Continuous Deployment**: Pushes the Docker image to Docker Hub for easy deployment.

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.x**: Required to run the Flask application.
- **pip**: Python package manager to install dependencies.
- **Virtualenv** (optional but recommended): To create an isolated Python environment.
- **Docker**: Required to build and push Docker images.
- **GitHub Repository**: A remote repository to host the code and GitHub Actions workflow.
- **Docker Hub Account**: To store and manage the containerized application.

## Setup Instructions

Follow these steps to set up the project:

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd flask-cicd
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Docker Setup

To containerize the application, follow these steps:

1. **Build the Docker image:**
    ```bash
    docker build -t <your-dockerhub-username>/flask-cicd .
    ```

2. **Run the container:**
    ```bash
    docker run -p 5000:5000 <your-dockerhub-username>/flask-cicd
    ```

3. **Push the image to Docker Hub:**
    ```bash
    docker login
    docker push <your-dockerhub-username>/flask-cicd
    ```

## CI/CD Pipeline with GitHub Actions

This project includes a GitHub Actions workflow (`.github/workflows/flas-app.yml`) that automates the following:

1. **Code Checkout**: Clones the repository.
2. **Set Up Python Environment**: Installs Python and dependencies.
3. **Run Unit Tests**: Executes automated tests to ensure application stability.
4. **Build Docker Image**: Creates a Docker image of the application.
5. **Push to Docker Hub**: Publishes the built image to Docker Hub.

### GitHub Actions Workflow Example

Here is a sample GitHub Actions workflow configuration:

```yaml
name: Flask CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2
      
      - name: Set Up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Tests
        run: |
          python -m unittest discover tests

      - name: Set Up Docker Buildx
        uses: docker/setup-buildx-action@v1

      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and Push Docker Image
        uses: docker/build-push-action@v2
        with:
          push: true
          tags: <your-dockerhub-username>/practice:latest
```

## Environment Variables

Ensure the following environment variables are set up in GitHub Secrets:

- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password.

## Future Improvements

- **Deployment to Kubernetes**: Automate deployment to a Kubernetes cluster.
- **CI/CD for Multiple Environments**: Implement staging and production pipelines.
- **Enhanced Testing**: Add integration and end-to-end tests.


By following this guide, you can successfully set up a Flask-based CI/CD pipeline using GitHub Actions and Docker. 🚀

