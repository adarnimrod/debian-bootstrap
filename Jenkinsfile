pipeline {
    agent any
    stages {
        stage('install') {
            steps {
                sh 'virtualenv example'
                sh '. example/bin/activate && pip install -r tests/requirements.txt'
                sh '. example/bin/activate && ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles'
                sh '. example/bin/activate && molecule dependency'
            }
        }
        stage('test') {
            steps {
                sh '. example/bin/activate && pre-commit run --all-files'
            }
        }
    }
}
