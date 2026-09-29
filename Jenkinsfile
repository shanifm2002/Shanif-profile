pipeline {
    agent any

    environment {
        IMAGE = "shanif2002/shanif-profile"
        TAG   = "${env.BUILD_NUMBER}"
    }

    options { timestamps(); disableConcurrentBuilds() }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Test') {
    steps {
        bat 'docker run --rm -v "%WORKSPACE%:/app" -w /app python:3.12-slim sh -c "pip install --no-cache-dir Flask gunicorn pytest flake8 && python -m flake8 app.py --max-line-length=160 && python -m pytest -q"'
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