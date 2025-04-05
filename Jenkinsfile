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
                sh 'docker build -t ai-agent-app .'
            }
        }
        stage('Test') {
            steps {
                // İsteğe bağlı: Test komutlarını burada çalıştırabilirsin
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 ai-agent-app'
            }
        }
    }
}
