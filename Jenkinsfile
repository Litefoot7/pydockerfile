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
        withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_TOKEN')]) {
            sh '''
                rm -f ~/.docker/config.json
                echo "$DOCKER_TOKEN" | docker login -u litefoot7 --password-stdin
                docker tag $IMAGE_NAME:$BUILD_NUMBER litefoot7/$IMAGE_NAME:$BUILD_NUMBER
                docker push litefoot7/$IMAGE_NAME:$BUILD_NUMBER
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
