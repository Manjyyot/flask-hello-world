pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = 'docker-hub-cred' // Use the credentials ID you created
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
                    // Using bash to ensure virtual environment is set up properly
                    sh '/bin/bash -c "python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }

        stage('Docker Login') {
            steps {
                script {
                    // Use Docker Hub credentials from Jenkins credentials manager
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        // Log into Docker Hub
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t iammanjyyot/my-flask-hello-world:latest .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker image to Docker Hub
                    sh 'docker push iammanjyyot/my-flask-hello-world:latest'
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    // Add your deployment steps here, like SSH to your EC2 and pulling the Docker image
                    echo 'Deploying to production...'
                }
            }
        }
    }

    post {
        always {
            // Clean workspace after job is done
            cleanWs()
        }
    }
}
