pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'iammanjyyot/my-flask-hello-world'
        DOCKER_TAG = 'latest'
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
                    // Set up virtual environment and install dependencies
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker image to Docker Hub
                    sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                // Deploy your app to production here (this is just an example)
                echo 'Deploying to production...'
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after the job
        }
    }
}
