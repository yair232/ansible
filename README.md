AWS Infrastructure Automation with Ansible and Jenkins
This project automates AWS infrastructure management using Ansible playbooks and Jenkins pipelines. It includes provisioning EC2 instances, configuring them, and managing containers.

Playbooks
1. Install Python, Pip, and Boto3
This playbook installs essential dependencies like Python, pip, and boto3 to enable AWS interactions.

2. EC2 Instance Setup
This playbook creates an EC2 instance on AWS and generates an inventory file with the new instance's IP address.

3. Instance Configuration and Container Setup
Once the EC2 instance is ready, this playbook installs the required software on the instance and runs a container on it.

Docker Automation
The pipeline also includes a parallel stage that builds a Docker image and pushes it to Docker Hub.

Jenkins Pipeline
The Jenkins pipeline runs these playbooks and orchestrates the infrastructure setup, including Docker image creation and deployment.

