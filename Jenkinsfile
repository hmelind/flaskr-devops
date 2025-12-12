pipeline {
    agent any
    
    environment {
        GITHUB_REPO = 'https://github.com/hmelind/flaskr-devops.git'
        BRANCH = 'main'
        COMPOSE = "docker-compose"
    }
    
    stages {
        stage('Checkout'){
            steps {
                git branch: env.BRANCH, url: env.GITHUB_REPO
            }
        }
        
        stage('Build images') {
            steps {
                sh '${env.COMPOSE} build'
            }
        }
        
        stage('Init DB') {
            steps {
                sh '${env.COMPOSE} run --rm web flask --app flaskr init-db'
            }
        }
        
        stage('Run tests') {
            steps {
                sh '${env.COMPOSE} run --rm flaskr pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh '${env.COMPOSE} up -d'
            }
        }
    }
    
    post {
        always {
            sh 'docker-compose down'
        }
        success {
            echo 'SUCCESS'
        }
        failure {
            echo 'FAILURE'
        }
    }
}

