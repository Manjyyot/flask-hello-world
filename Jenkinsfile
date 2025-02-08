pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-flask-app:latest'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        pytest
                    '''
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        docker build -t $DOCKER_IMAGE .
                    '''
                }
            }
        }

        stage('Push Docker image') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Deploy to production') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        docker run -d $DOCKER_IMAGE
                    '''
                }
            }
        }
    }
}
