# Serverless Visitor Counter API (Backend)

The serverless backend infrastructure powering the dynamic visitor counter for my resume. Built with **AWS SAM (Infrastructure as Code)** and fully automated via **GitHub Actions CI/CD**.

---

## 🚀 Architectural Overview

* **API Gateway**: Exposes an HTTP REST endpoint with CORS enabled for frontend communication.
* **AWS Lambda (Python 3.11)**: Extracts `page` query parameters (`?page=id`) from the event request and updates DynamoDB atomically.
* **Amazon DynamoDB**: Key-Value NoSQL database storing visitor counts using `page_id` as the partition key.
* **AWS SAM**: Manages Infrastructure as Code (IaC) and defines IAM policies using `DynamoDBCrudPolicy` for strict least-privilege security.

---

## 🛠 Tech Stack

* **Infrastructure as Code:** AWS Serverless Application Model (SAM) / CloudFormation
* **Runtime:** Python 3.11 (boto3)
* **CI/CD:** GitHub Actions (Automated `sam build` and headless `sam deploy`)
* **Security:** AWS IAM, GitHub Repository Secrets

---

## 🔄 Automated CI/CD Workflow

Deployments are fully automated using GitHub Actions (`.github/workflows/deploy.yml`). 

Whenever code is pushed to the `main` branch:
1. GitHub Actions sets up Python and the AWS SAM CLI.
2. Authenticates using AWS IAM credentials stored in **GitHub Repository Secrets**.
3. Executes `sam build` and deploys non-interactively using `--no-confirm-changeset`.

---

## 📁 Repository Structure

```text
visitor-counter-backend/
├── .github/
│   └── workflows/
│       └── deploy.yml      # CI/CD deployment workflow
├── src/
│   └── app.py              # Lambda function code
├── template.yaml           # AWS SAM Infrastructure specification
└── samconfig.toml          # Deployment configuration
```

---

## 🔗 Related Links

* **Live Resume:** [https://main.d1jq9lgeqew9vu.amplifyapp.com/](https://main.d1jq9lgeqew9vu.amplifyapp.com/) *(Replace with your live URL)*
* **Frontend Repository:** [Link to Frontend Repo](https://github.com/sophjvlia/visitor-counter-frontend)
