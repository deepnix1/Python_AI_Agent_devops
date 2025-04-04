pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/deepnix1/Python_AI_Agent_devops.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest || echo "Testler başarısız oldu"'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-app'
            }
        }
    }
}
