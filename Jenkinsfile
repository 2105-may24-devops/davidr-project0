pipeline {
    agent {
        label 'ubuntu-docker'
    }
    triggers { pollSCM('H/1 * * * *') }
    stages {
        stage('build') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/python3 -m pip install -r requirements.txt
                '''
            }
        }
        stage('test') {
            steps {
                sh 'bash ./scripts/test.sh all'
            }
        }
        stage('deploy') {
            steps {
                ansiblePlaybook(
                    credentialsId: 'trainer-vm',
                    inventory: 'ansible/inventory',
                    playbook: 'ansible/install.yml',
                    disableHostKeyChecking: true)
            }
        }
    }
}
