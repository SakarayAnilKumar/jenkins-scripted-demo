

node {

    try {
        stage('Checkout') {
            echo 'Checking out the code from SCM...'
            checkout scm
        }
        stage('Show files'){
            echo 'Showing the files in the workspace...'
            if (isUnix()) {
                sh 'ls -l'
            } else {
                bat 'dir'
            }
        }
        stage('Install Dependencies') {
            echo 'Installing dependencies...'
            if (isUnix()) {
                sh 'pip install -r requirements.txt'
            } else {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run application') {
            echo 'Running the application...'
            pythonScript = isUnix() ? 'python3' : 'python'
            sh "${pythonScript} app.py"
        }
        stage('Test') {
            echo 'Running tests...'
            if (isUnix()) {
                sh 'pytest -v'
            } else {
                bat 'pytest -v'
            }
        }
        stage('Build Result') {
            echo 'Application built successfully.'
        }
    }
    catch (Exception e) {
        echo "Build failed: ${e.getMessage()}"
        currentBuild.result = 'FAILURE'
    }
    finally {
        echo 'Cleaning up...'
        cleanWs()
    }
}
