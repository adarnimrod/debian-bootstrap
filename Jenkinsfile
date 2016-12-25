pipeline {
    agent any
    stages {
        stage('install') {
            steps {
                sh 'pip install -r tests/requirements.txt'
                sh 'ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles'
                sh 'molecule dependency'
            }
        }
        stage('test') {
            steps {
                sh 'pre-commit run --all-files'
            }
        }
    }
}
