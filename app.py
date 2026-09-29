from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Shanif M",
    "title": "Cloud DevOps Engineer",
    "location": "Kannur, Kerala",
    "email": "shanifm2002@gmail.com",
    "phone": "+91 7902756448",
    "linkedin": "#",  # put your LinkedIn URL here
    "github": "#",    # put your GitHub URL here
    "photo": "photo.jpg",  # save your photo as static/photo.jpg
    "summary": (
        "Cloud DevOps Engineer with hands-on project experience designing GitOps-based "
        "CI/CD pipelines on AWS EKS using Terraform, Docker, Kubernetes, GitHub Actions "
        "and ArgoCD, plus working knowledge of Microsoft Azure. Skilled in Linux "
        "administration, Bash scripting, networking, and monitoring with Prometheus, "
        "Grafana and AWS CloudWatch."
    ),
    "experience": [
        {
            "role": "Software Developer Intern",
            "company": "Experion Technologies",
            "period": "Aug 2025 – Oct 2025",
            "points": [
                "Built and integrated UI components with REST APIs; used Git/GitHub for version control and collaboration.",
                "Automated recurring workflows using Microsoft Power Automate, reducing manual effort.",
            ],
        }
    ],
    "projects": [
        {
            "name": "End-to-End GitOps CI/CD Pipeline on AWS (EKS)",
            "stack": "AWS, Terraform, Docker, Kubernetes, GitHub Actions, ArgoCD, Prometheus, Grafana",
            "points": [
                "Designed a GitOps pipeline on AWS EKS for automated, repeatable deployments from commit to production.",
                "Provisioned VPC, EKS and IAM with Terraform modules; containerized apps with Docker and stored images in ECR.",
                "Built GitHub Actions build/test/deploy workflows integrated with ArgoCD auto-sync.",
                "Implemented Prometheus/Grafana monitoring with real-time metrics and rollback support.",
            ],
        },
        {
            "name": "End-to-End CI/CD Pipeline with Jenkins and Kubernetes",
            "stack": "Jenkins, Maven, SonarQube, Docker, Kubernetes, Nexus, Trivy, Prometheus, Grafana",
            "points": [
                "Built an automated Jenkins pipeline, replacing manual build-and-deploy steps.",
                "Integrated Maven and SonarQube for continuous testing and code quality checks.",
                "Built Docker images, scanned with Trivy, stored artifacts in Nexus, and deployed on Kubernetes.",
                "Implemented Prometheus/Grafana dashboards for system visibility.",
            ],
        },
    ],
    "skills": {
        "AWS": "EC2, S3, RDS, VPC, IAM, Lambda, ECS, EKS, ECR, CloudWatch, CloudTrail, Route 53, Auto Scaling, CloudFront, API Gateway, DynamoDB, SNS",
        "Azure": "Virtual Machines, Blob Storage, Azure AD, Virtual Networks, Azure DevOps, App Services",
        "DevOps & CI/CD": "Terraform, Ansible, Docker, Kubernetes, Git, GitHub, GitHub Actions, Jenkins, ArgoCD, Helm",
        "Linux": "File systems, permissions, processes, services, user management, log analysis, Bash scripting",
        "Monitoring": "Prometheus, Grafana, CloudWatch, CloudTrail, AWS X-Ray",
        "Networking & Security": "DNS, HTTP/HTTPS, TCP/IP, VPC, Subnets, Security Groups, CIDR, IAM, ALB/NLB, Firewalls, OSI model",
        "Database": "MySQL, SQL queries, JOINs, backup & restore",
        "Operating systems": "Ubuntu, Windows 10, Windows 11",
    },
    "certifications": [
        {
            "name": "AWS DevOps Training — Besoft, Bangalore",
            "period": "Nov 2025 – Sep 2026",
            "detail": "Hands-on training in CI/CD pipelines, infrastructure automation and cloud deployment.",
        }
    ],
    "education": [
        {
            "degree": "Master of Computer Applications (MCA)",
            "school": "Krupanidhi College of Management, Bangalore — Bangalore North University",
            "period": "2023 – 2025",
        },
        {
            "degree": "Bachelor of Computer Applications (BCA)",
            "school": "Wadihuda Institute of Research and Advanced Studies, Kannur — Kannur University",
            "period": "2020 – 2023",
        },
    ],
}


@app.route("/")
def index():
    return render_template("index.html", p=PROFILE)


if __name__ == "__main__":
    app.run(debug=True)
