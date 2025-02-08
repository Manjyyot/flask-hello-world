pipeline {
    agent any

    environment {
        FLASK_APP = 'main.py'
        FLASK_RUN_HOST = '0.0.0.0'
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
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    sh 'source venv/bin/activate && pytest'
                }
            }
        }

        stage('Build Docker image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    sh 'docker build -t your-image-name .'
                }
            }
        }

        stage('Push Docker image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    sh 'docker tag your-image-name your-repository/your-image-name:latest'
                    sh 'docker push your-repository/your-image-name:latest'
                }
            }
        }

        stage('Deploy to production') {
            when {
                branch 'main'
            }
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 your-repository/your-image-name:latest'
                }
            }
        }
    }
}
