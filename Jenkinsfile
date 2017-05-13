/*
Jenkins pipeline for testing an Ansible role.
Required software on the agent:
- Python 2.7.
- Tox.
- Vagrant.
- Virtualbox.
*/
pipeline {
    agent any
    environment {
        VBOX_HWVIRTEX       = off
    }
    stages {
        stage('install') {
            steps {
                sh 'git submodule update --init --recursive'
            }
        }
        stage('test') {
            steps {
                parallel (
                    'pre-commit': {
                        sh 'tox -e pre-commit'
                    }
                    'molecule': {
                        sh 'tox'
                    }
                )
            }
        }
    }
    post {
        success {
            sh 'tox -e import'
        }
    }
}
