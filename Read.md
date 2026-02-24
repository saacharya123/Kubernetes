# 🚀 CI/CD Deployment using Jenkins on AWS EC2

## 📌 Project Overview

This project demonstrates the deployment of **Frontend and Backend Flask applications** on a single Amazon EC2 instance and the implementation of a **CI/CD pipeline using Jenkins** to automate application deployment.

The goal is to achieve automated deployments where code pushed to GitHub triggers Jenkins pipelines that update and restart running applications.

---

## 🏗️ Architecture Overview

GitHub Repository → Jenkins CI/CD Pipeline → EC2 Instance → PM2 Process Manager → Flask Applications

### Components Used

* AWS EC2 (Ubuntu)
* Jenkins
* GitHub
* Flask (Frontend & Backend)
* Python Virtual Environment (venv)
* PM2 (Process Manager)

---

## ⚙️ Part 1 — Application Deployment on EC2

### 1️⃣ EC2 Provisioning

* Created an Ubuntu EC2 instance.
* Opened required ports in Security Group:

  * 22 (SSH)
  * 8080 (Jenkins)
  * 8000 (Frontend)
  * 9000 (Backend)

### 2️⃣ Install Dependencies

Installed required tools:

* Python3
* Git
* NodeJS & npm
* PM2

### 3️⃣ Clone Repository

```
git clone https://github.com/saacharya123/Kubernetes.git
```

Project Structure:

```
Kubernetes/
 ├── frontend/
 └── backend/
```

### 4️⃣ Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirement.txt
```

### 5️⃣ Run Applications using PM2

Frontend:

```
pm2 start /home/ubuntu/Kubernetes/frontend/venv/bin/python3 /home/ubuntu/Kubernetes/frontend/app.py --name frontend-app
```

Backend:

```
pm2 start /home/ubuntu/Kubernetes/frontend/venv/bin/python3 /home/ubuntu/Kubernetes/backend/app.py --name backend-app
```

---

## 🤖 Part 2 — Jenkins CI/CD Pipeline Setup

### 1️⃣ Jenkins Installation

Installed Jenkins on EC2 and accessed it via:

```
http://<EC2-Public-IP>:8080
```

Installed Plugins:

* Pipeline
* Git
* NodeJS

---

### 2️⃣ Jenkins Pipelines Created

Two pipelines were configured:

* frontend-pipeline
* backend-pipeline

---

## 📄 Frontend Jenkins Pipeline Script

```
pipeline {
    agent any
    stages {
        stage('Pull Frontend Code') {
            steps {
                sh 'sudo -u ubuntu git -C /home/ubuntu/Kubernetes/frontend pull'
            }
        }
        stage('Install Frontend Dependencies') {
            steps {
                sh '''
                sudo -u ubuntu bash -c "
                source /home/ubuntu/Kubernetes/frontend/venv/bin/activate &&
                pip install -r /home/ubuntu/Kubernetes/frontend/requirement.txt"
                '''
            }
        }
        stage('Restart Frontend App') {
            steps {
                sh 'sudo -u ubuntu pm2 restart frontend-app'
            }
        }
    }
}
```

---

## 📄 Backend Jenkins Pipeline Script

```
pipeline {
    agent any
    stages {
        stage('Pull Backend Code') {
            steps {
                sh 'sudo -u ubuntu git -C /home/ubuntu/Kubernetes/backend pull'
            }
        }
        stage('Install Backend Dependencies') {
            steps {
                sh '''
                sudo -u ubuntu bash -c "
                source /home/ubuntu/Kubernetes/frontend/venv/bin/activate &&
                pip install -r /home/ubuntu/Kubernetes/backend/requirement.txt"
                '''
            }
        }
        stage('Restart Backend App') {
            steps {
                sh 'sudo -u ubuntu pm2 restart backend-app'
            }
        }
    }
}
```

---

## 🔁 Automated Deployment using GitHub Webhook

A webhook was configured in GitHub:

Settings → Webhooks → Add Webhook

Payload URL:

```
http://<EC2-Public-IP>:8080/github-webhook/
```

Event:

```
Push Events
```

### Workflow

1. Developer pushes code to GitHub.
2. GitHub sends webhook event to Jenkins.
3. Jenkins automatically triggers pipeline.
4. Pipeline pulls latest code, installs dependencies, and restarts applications.

---

## ✅ CI/CD Pipeline Flow

```
Git Push
   ↓
GitHub Webhook
   ↓
Jenkins Pipeline Triggered
   ↓
git pull
   ↓
pip install
   ↓
pm2 restart
   ↓
Updated Application Live
```

---

## 📸 Evidence

Include screenshots of:

* Running EC2 instance
* Jenkins Pipeline Success (Stage View)
* Console Output logs
* Frontend & Backend accessible via Public IP

---

## 🎯 Conclusion

This project successfully demonstrates:

* Automated CI/CD deployment using Jenkins
* Process management using PM2
* GitHub webhook integration
* End-to-end automation from code push to application deployment
