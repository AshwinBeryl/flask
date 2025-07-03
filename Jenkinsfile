pipeline {
    agent any
    
    triggers {
        githubPush()
    }

    stages {
        stage('Git Clone') {
            steps {
                withCredentials([string(credentialsId: 'AshwinGitHubPAT', variable: 'gitpass')]){
                    sh '''
                    echo "Agent Info:"
                    whoami
                    hostname -i
                    pwd
                    if [ -d "flask" ]; then
                      echo "flask dir does exist"
                      echo "Cleaning the repo"
                      rm -rf flask/
                      echo "Repo cleaned successfully"
                    fi
                    echo "Cloning the repo"
                    git clone https://"${gitpass}"@github.com/AshwinBeryl/flask.git
                    echo "Repo cloned - master branch"
                    '''
                }
            }
        }
        stage('Image Build') {
            steps {
                sh '''
                echo "Building Docker Image"
                cd flask
                echo jenkins | sudo -S docker build -t flask-app .
                echo "Docker Image built successfully"
                '''
            }
        }
        stage('Restart Flask Server') {
            steps {
                sh '''
                echo jenkins | sudo -S docker run -d -p 5000:5000 flask-app:latest
                '''
                echo 'Server Restarted'
            }
        }
    }
}
