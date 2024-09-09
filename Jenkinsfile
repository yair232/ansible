pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/yair232/ansible.git'
            }
        }
        stage('Run Pre-Installation Playbook') {
            steps {
                script {
                    sh '''
                    # Run the playbook to set up the environment
                    ansible-playbook pre-playbook.yaml
                    '''
                }
            }
        }

        stage('Build Docker Image and Run Playbook in Parallel') {
            parallel {
                stage('Build and Push Docker Image') {
                    steps {
                        script {
                            // Build your Docker image
                            sh 'docker build -t yair23/nginx-docker .'
                            docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
                                def customImage = docker.image('yair23/nginx-docker')
                                customImage.push('latest')
                            }
                        }
                    }
                }

                stage('Run First Playbook') {
                    steps {
                        script {
                            def output = sh(script: '''
                            # Use bash explicitly to handle the source command
                            bash -c "source ~/myenv/bin/activate && ansible-playbook firs-playbook.yaml"
                            ''', returnStdout: true).trim()
                            env.EC2_IP = output
                            echo "EC2 IP Address: ${env.EC2_IP}"
                        }
                    }
                }
            }
        }

        stage('Wait for 30 Seconds') {
            steps {
                script {
                    // Wait for 100 seconds
                    sleep(time: 100, unit: 'SECONDS')
                    echo "Waited for 100 seconds"
                }
            }
        }

        stage('Run Second Playbook') {
            steps {
                sh '''
                # Use bash explicitly to handle the source command
                bash -c "source ~/myenv/bin/activate && ansible-playbook 2-playbook.yaml"
                '''
            }
        }
    }

    post {
        always {
            // Clean up workspace if needed
            cleanWs()
        }
    }
}
