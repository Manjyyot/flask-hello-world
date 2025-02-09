# Flask Hello World API
 
This project demonstrates the basics of building a simple API using Flask. It includes endpoints that return a static "Hello, World!" message as well as personalized greetings, along with automated testing using `pytest`.
 
## Key Features
 
- **Static Greeting**: A simple "Hello, World!" message.
- **Dynamic Greeting**: Personalized greetings with user input (e.g., `/hello/John` returns "Hello, John!").
- **Automated Testing**: Tests for verifying endpoint functionality using `pytest`.
 
## Requirements
 
- **Python**: Version 3.6 or higher
- **Flask**: Version 2.0 or higher
- **pytest**: Version 6.0 or higher
 
## Installation
 
1. **Clone the repository**:
   ```bash
   git clone https://github.com/manjyyot/flask-hello-world-api.git
   cd flask-hello-world-api
## Installation
 
2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate  # Windows

3. Install dependencies:
  
   ```bash
   pip install -r requirements.txt

## Running the Application:

4. **Start the Flask server**:

    ```sh
    flask run
    Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the API in action.

5. ## **API Endpoints**:

- **GET /**  
  Returns `"Hello, World!"`

- **GET /hello**  
  Returns `"Hello!"`

- **GET /hello/{name}**  
  Returns a personalized greeting.


## **Running Tests**:

5. To run tests, use:
    ```bash
    pytest

## **Deployment** (v1.0.0)

### AWS EC2  
Follow the steps to deploy on **AWS EC2**:  
1. Set up an EC2 instance.  
2. Install necessary dependencies.  
3. Run the Flask app.

### Docker  
Build and run the Docker container with:

    ```bash
    docker build -t flask-hello-world-api .
    docker run -p 5000:5000 flask-hello-world-api

## **Jenkins Pipeline for Continuous Integration and Deployment** (v1.0.0)

This project includes a **Jenkins pipeline** for continuous integration and deployment using **Docker**.  
The pipeline automates the following tasks:
- Setting up the Python environment.
- Building and pushing the Docker image to Docker Hub.
- Deploying the application to production.

---

## **Pipeline Overview**

The **Jenkins pipeline** is defined in the 
  
    ```bash
    pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = 'docker-hub-cred'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    sh '/bin/bash -c "python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }

        stage('Docker Login') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t iammanjyyot/my-flask-hello-world:latest .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push iammanjyyot/my-flask-hello-world:latest'
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    echo 'Deploying to production...'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            emailext(
                subject: "Build #${BUILD_NUMBER} - SUCCESS",
                body: "The build was successful! Check the details: ${BUILD_URL}",
                to: "manjyotsinghchaudhary@gmail.com"
            )
        }
        failure {
            emailext(
                subject: "Build #${BUILD_NUMBER} - FAILURE",
                body: "The build failed. Check the console output for details: ${BUILD_URL}",
                to: "manjyotsinghchaudhary@gmail.com"
            )
        }
    }
    }
