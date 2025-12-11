pipeline {
    agent any
    
    environment {
        GITHUB_REPO = 'https://github.com/hmelind/flaskr-devops.git'
        BRANCH = 'main'
    }
    
    stages {
        stage('Checkout'){
            steps {
                git branch: env.BRANCH url: env.GITHUB_REPO
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install --no-cache-dir -e .'
                sh 'pip install pytest coverage'
            }
        }
        
        stage('Lint') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 .'
            }
        }
        
        stage('Tests') {
            steps {
                sh 'pip install \'.[test]\''
                sh 'pytest'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Buiding the application...'
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/**/*', fingerprint: true
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
        
        stage('Cleanup') {
            steps {
                deleteDir()
            }
        }
    }
    
    post {
        success {
            echo 'SUCCESS'
        }
        failure {
            echo 'FAILURE'
        }
    }
}

