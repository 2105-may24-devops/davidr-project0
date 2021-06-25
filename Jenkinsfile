pipeline {
    agent {
        label 'test'
    }
    triggers { pollSCM('H/1 * * * *') }
    stages {
        stage('build') {
            steps {
                sh 'ansible-playbook --version'
            }
        }
    }
}
