pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/hussainturii/linear-api.git'
                sh 'docker compose down'
                sh 'docker compose up -d'
            }
        }
    }
    post {
        always {
            script {
                sh "git config --global --add safe.directory ${env.WORKSPACE}"
                def committer = sh(
                    script: "git log -1 --pretty=format:'%ae'",
                    returnStdout: true
                ).trim()
                emailext(
                    to: committer,
                    subject: "Build #${env.BUILD_NUMBER}",
                    body: "Build Status: ${currentBuild.currentResult}"
                )
            }
        }
    }
}
