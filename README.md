# Cloud-Native File Processing Platform on Google Cloud

A hands-on Google Cloud portfolio project demonstrating event-driven, serverless application development using Cloud Storage, Eventarc, Cloud Run, and Python.

---

## Project Highlights

- ✅ Built an event-driven architecture using Google Cloud
- ✅ Automated file processing with Cloud Storage and Eventarc
- ✅ Deployed a Python Flask application to Cloud Run
- ✅ Processed CloudEvents and extracted file metadata
- ✅ Integrated Cloud Logging for monitoring and troubleshooting
- 🚧 Expanding the platform with validation, AI, and Firestore

---

## Project Overview

This project documents my journey of designing and building a cloud-native file processing platform using Google Cloud.

Rather than following a tutorial, I'm approaching this like a real engineering project by documenting the planning, architecture decisions, implementation, testing, and lessons learned along the way.

The long-term goal is to build an intelligent file processing platform capable of validating uploaded files, extracting metadata, integrating with Google AI services, and storing processing results in Firestore.

---

## Why I'm Building This

One of the best ways I learn is by building real-world projects.

After spending nearly a decade working with Microsoft 365 enterprise collaboration technologies, I wanted to expand into Google Cloud by building production-style cloud-native applications.

This project helps me gain hands-on experience with:

- Google Cloud Platform (GCP)
- Event-Driven Architecture
- Serverless Computing
- Cloud Run
- Eventarc
- Cloud Storage
- IAM
- Cloud Logging
- Cloud Monitoring
- Python Development

---

## Project Goals

- Learn Google Cloud fundamentals
- Build event-driven applications
- Design serverless architectures
- Improve Python development skills
- Document engineering decisions
- Develop a portfolio project demonstrating cloud engineering skills

---

## Architecture

```text
                File Upload
                     │
                     ▼
          Cloud Storage Bucket
                     │
                     ▼
              Eventarc Trigger
                     │
                     ▼
        Cloud Run (Python Flask App)
                     │
                     ▼
          Extract File Metadata
                     │
                     ▼
              Cloud Logging
```

---

## Technologies Used

### Google Cloud

- Cloud Storage
- Eventarc
- Cloud Run
- Cloud Logging
- IAM

### Programming

- Python 3
- Flask

### Development Tools

- Visual Studio Code
- Git
- GitHub
- Google Cloud CLI

---

## Skills Demonstrated

- Google Cloud Platform
- Event-Driven Architecture
- Serverless Computing
- Cloud Run Deployments
- Cloud Storage
- Eventarc
- IAM Configuration
- Python Development
- Flask APIs
- Cloud Logging
- Git Version Control
- Troubleshooting Cloud Applications

---

## Current Status

### ✅ Sprint 1 Complete

#### Completed

- Created a Google Cloud Storage bucket
- Configured an Eventarc trigger
- Built a Python Flask application
- Deployed the application to Cloud Run
- Processed Cloud Storage upload events
- Parsed CloudEvent payloads
- Extracted:
  - Bucket name
  - Filename
  - Content type
  - File size
- Logged file metadata using Cloud Logging
- Verified successful end-to-end event processing

---

## Sprint Roadmap

### ✅ Sprint 1 — Event Processing

- Receive Cloud Storage events
- Parse CloudEvent payloads
- Extract file metadata
- Log metadata
- Deploy to Cloud Run
- Validate end-to-end functionality

### 🚧 Sprint 2 — File Validation

- Validate supported file types
- Improve error handling
- Add structured logging
- Prepare the application for AI processing

### 🔮 Sprint 3 — AI Integration

- Integrate Google Gemini
- Summarize uploaded documents
- Extract document insights
- Store results in Firestore

### 🔮 Sprint 4 — Monitoring & Analytics

- Cloud Monitoring
- Metrics
- Dashboards
- Alerting
- Error Reporting

---

## What I Learned

This project has provided hands-on experience with:

- Designing event-driven cloud architectures
- Deploying serverless applications
- Working with CloudEvents
- Configuring Eventarc triggers
- Managing IAM permissions
- Reading Cloud Logging
- Troubleshooting Cloud Run deployments
- Debugging distributed cloud applications

---

## Repository Structure

```text
cloud-native-file-processing-platform/
│
├── docs/
│   ├── architecture.md
│   ├── decisions.md
│   ├── lessons-learned.md
│   └── roadmap.md
│
├── screenshots/
│
├── main.py
├── requirements.txt
├── README.md
├── PROJECT.md
└── CHANGELOG.md
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/<your-username>/cloud-native-file-processing-platform.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Deploy to Cloud Run

```bash
gcloud run deploy file-processor --source .
```

---

## Future Enhancements

- AI-powered document processing
- Firestore integration
- Metadata storage
- File validation pipeline
- REST API endpoints
- Cloud Monitoring dashboards
- Performance metrics
- Alerting and observability
- CI/CD with GitHub Actions
- Automated testing

---

## Project Status

**Status:** 🟢 Active Development

This project is actively being expanded through multiple development sprints, with each sprint introducing new Google Cloud services and cloud engineering concepts.

---

## Author

**Daniel Montaie**

Built as a hands-on Google Cloud portfolio project to strengthen practical cloud engineering skills through real-world application development.

---

> **Note:** This repository is intentionally documented as a learning project. Each sprint captures architecture decisions, implementation details, challenges encountered, and lessons learned to demonstrate both technical growth and engineering best practices.