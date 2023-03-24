pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python setup.py build'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python setup.py install'
            }
        }
    }
    post {
        always {
            junit '**/pytest.xml'
            archiveArtifacts artifacts: '**/*.tar.gz'
        }
    }
    environment {
        PYENV_ROOT = tool 'PyEnv'
    }
    tools {
        pyenv '3.11.0'
    }
    options {
        timeout(time: 1, unit: 'HOURS')
        skipDefaultCheckout()
    }
    checkout([$class: 'GitSCM', 
              branches: [[name: '*/main']], 
              userRemoteConfigs: [[url: 'https://github.com/mkaramica/testCICD.git']]])
}
