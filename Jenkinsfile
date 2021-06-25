pipeline {
    agent {
        label 'test'
    }
    triggers { pollSCM('H/1 * * * *') }
    stages {
        stage('build') {
            steps {
                sh 'sudo apt install ansible'
                sh 'ansible-playbook --version'
            }
        }
    }
}
