pipeline {
    agent {
        label 'test'
    }
    triggers { pollSCM('H/1 * * * *') }
    stages {
        stage('build') {
            steps {
                sh 'apt install ansible'
                sh 'ansible-playbook --version'
            }
        }
    }
}
