# AWS Infrastructure Automation with Ansible and Jenkins

## Overview

This guide walks you through setting up an AWS EC2 instance that automatically creates itself, installs necessary packages, and starts a container. The setup includes Docker, Jenkins, and Ansible, with a CI/CD pipeline configured to build Docker images and deploy updates whenever changes are made to your repository. By following these steps, you’ll streamline the deployment process, ensuring that your EC2 instance is fully configured and operational with minimal manual intervention.


## Steps to Follow

### 1. Clone or Copy the Repository

Clone this repository or copy the files to the specified location as per the repository structure. This is important because we'll set up a webhook later on to trigger automatic builds.

### 2. Create and Configure Your EC2 Instance

Launch an EC2 Instance:

Create a new EC2 instance with the Ubuntu operating system.
User Data Script:

In the EC2 instance creation wizard, paste the following bash script into the "User Data" section to automate the setup process:

```bash
#!/bin/bash
sudo apt update
sudo apt install -y ansible
sudo wget
git clone https://github.com/yair232/ansible.git
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install -y jenkins
sudo apt install -y fontconfig openjdk-17-jre
```

### 3. Configure Jenkins

#### Access Jenkins:

Once the EC2 instance is running, open your browser and navigate to http://<your_instance_public_ip>:8080. Complete the Jenkins initial setup and reach the main dashboard.

#### Create a New Pipeline:
Click on "New Item", name the pipeline, select "Pipeline", and click "OK".

#### Configure the Pipeline:

Check "GitHub hook trigger for GITScm polling".
In the "Pipeline Definition" section, select "Pipeline script from SCM".
Choose "Git" for SCM and enter your Git repository URL.
In the "Branches to build" field, change "master" to "main".

### 4.  Set Up GitHub Webhook

#### Create a Webhook:

Go to your GitHub repository, navigate to Settings > Webhooks, and click "Add webhook".
In the Payload URL field, enter http://<your_ec2_instance_public_ip>:8080/github-webhook/.
Select "application/json" for Content type.
Check "Send me everything" for the events.
Click "Add webhook" to save the webhook.

### 5.  Testing and Verification

#### Update Files:

Make some changes to your index.html file (or any other file) .

#### Trigger Build:
Commit and push your changes to GitHub. This will automatically trigger the Jenkins pipeline, which will clone the repository, build the Docker image, and deploy the container.

#### Verify Deployment:

Using Curl: Run curl http://localhost:80 on your EC2 instance to verify the deployment.

Using a Web Browser: Open your browser and go to http://<your_ec2_instance_public_ip>:80 to view the updated webpage.

## Additional Notes

Ensure that you have allowed HTTP inbound traffic and port 8080 in your EC2 instance’s security group to access Jenkins and your deployed application.

Verify that all necessary permissions are correctly configured, such as access to GitHub and Docker Hub for pushing Docker images.
