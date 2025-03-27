

1 of 2,236
Fwd:
Inbox

PREETHA V J 717823I140 <717823i140@kce.ac.in>
Attachments
9:06 PM (2 minutes ago)
to 717823i132, me



---------- Forwarded message ---------
From: MONIKA S 717823I227 <717823i227@kce.ac.in>
Date: Sat, Mar 22, 2025 at 7:05 PM
Subject: Fwd:
To: <717823i140@kce.ac.in>




---------- Forwarded message ---------
From: MONIKA S 717823I227 <717823i227@kce.ac.in>
Date: Sat, Mar 22, 2025 at 2:35 PM
Subject: Fwd:
To: <717823i141@kce.ac.in>




---------- Forwarded message ---------
From: DHARRSHANA S 717823I109 <717823i109@kce.ac.in>
Date: Sat, Mar 22, 2025 at 2:23 PM
Subject:
To: <717823i227@kce.ac.in>




 One attachment
  •  Scanned by Gmail
pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/your-username/your-repo.git'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building the project...'
                // Example: sh './gradlew build' or 'mvn clean install'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests...'
                // Example: sh './gradlew test' or 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploying application...'
                // Example: sh './deploy.sh'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check logs for details.'
        }
    }
}
