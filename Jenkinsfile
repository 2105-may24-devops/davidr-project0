pipeline {
    agent {
        label 'ubuntu-docker'
    }
    triggers { pollSCM('H/1 * * * *') }
    stages {
        stage('build') {
            steps {
                sh 'echo Just taking up space'
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
