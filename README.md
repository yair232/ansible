# AWS Infrastructure Automation with Ansible and Jenkins

## Overview

This guide walks you through setting up an AWS EC2 instance with Docker, Jenkins, and Ansible. You'll also configure a CI/CD pipeline that automatically builds Docker images and deploys updates whenever changes are made to your repository.

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

### 3. Configure Jenkins

#### Access Jenkins:

Once the EC2 instance is running, open your browser and navigate to http://<your_instance_public_ip>:8080. Complete the Jenkins initial setup and reach the main dashboard.

#### Create a New Pipeline:


