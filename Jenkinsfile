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
