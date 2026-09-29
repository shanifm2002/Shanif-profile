pipeline {
    agent any

    environment {
        IMAGE = "YOUR_DOCKERHUB_USERNAME/shanif-profile"
        TAG   = "${env.BUILD_NUMBER}"
    }

    options { timestamps(); disableConcurrentBuilds() }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Test') {
            steps {
                bat '''
                    python -m venv venv
                    venv\\Scripts\\python -m pip install --no-cache-dir Flask gunicorn pytest flake8
                    venv\\Scripts\\python -m flake8 app.py --max-line-length=120
                    venv\\Scripts\\python -m pytest -q
                '''
            }
        }

        stage('Build image') {
            steps { bat 'docker build -t %IMAGE%:%TAG% -t %IMAGE%:latest .' }
        }

        stage('Trivy scan') {
            steps {
                bat 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image --severity CRITICAL --exit-code 1 --ignore-unfixed %IMAGE%:%TAG%'
            }
        }

        stage('Push to Docker Hub') {
            when { branch 'main' }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'DH_USER',
                                                  passwordVariable: 'DH_PASS')]) {
                    bat '''
                        echo %DH_PASS%| docker login -u %DH_USER% --password-stdin
                        docker push %IMAGE%:%TAG%
                        docker push %IMAGE%:latest
                    '''
                }
            }
        }
    }

    post {
        always { bat 'docker logout' }
    }
}