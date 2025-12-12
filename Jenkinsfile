pipeline {
    agent any
    
    environment {
        GITHUB_REPO = 'https://github.com/hmelind/flaskr-devops.git'
        BRANCH = 'main'
    }
    
    stages {
        stage('Checkout'){
            steps {
                git branch: env.BRANCH, url: env.GITHUB_REPO
            }
        }
        
        stage('Build images') {
            steps {
                sh 'docker compose build'
            }
        }
        
        stage('Init DB') {
            steps {
                sh 'docker compose run --rm web flask --app flaskr init-db'
            }
        }
        
        stage('Run tests') {
            steps {
                sh 'docker compose run --rm flaskr pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d'
            }
        }
    }
    
    post {
        always {
            sh 'docker compose down'
        }
        success {
            echo 'SUCCESS'
        }
        failure {
            echo 'FAILURE'
        }
    }
}

