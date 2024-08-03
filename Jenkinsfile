pipeline {
    agent {
        docker {
            image 'python:3.8'  // Use an image that includes Python
            args '-u root:root'
        }
    }

    environment {
        PYTHON_VERSION = '3.8'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    sh "python${PYTHON_VERSION} -m venv ${VENV_DIR}"
                    sh '''
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Flask App') {
            steps {
                script {
                    sh '''
                    source ${VENV_DIR}/bin/activate
                    flask run --port=5000 &
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    source ${VENV_DIR}/bin/activate
                    pytest --html=report.html
                    '''
                }
            }
        }

      

        stage('Email Report') {
            steps {
                script {
                    emailext(
                        to: 'test.adam011@gmail.com',
                        subject: "API Test Report for ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                        body: "Please find the API test report attached.",
                    )
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
