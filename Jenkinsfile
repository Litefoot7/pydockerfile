pipeline {
    agent any

    environment {
        IMAGE_NAME = "pydockerfile-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER -f dockerfile .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker tag $IMAGE_NAME:$BUILD_NUMBER $DOCKER_USER/$IMAGE_NAME:$BUILD_NUMBER
                        docker push $DOCKER_USER/$IMAGE_NAME:$BUILD_NUMBER
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Add your test commands here, e.g. pytest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed — check logs above.'
        }
    }
}
