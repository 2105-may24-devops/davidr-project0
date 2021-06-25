pipeline {
    agent any
    triggers { pollSCM('H/1 * * * *') }
    stages {
        stage('build') {
            steps {
                sh 'echo New Code'
            }
        }
    }
}