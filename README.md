<div align="center">
  <img src="./nexus_logo.png" alt="Nexus Orchestrator Logo" width="100%" style="max-width: 800px; border-radius: 10px; margin-bottom: 20px;">

  # Nexus // Orchestrator
  
  **Enterprise-Grade HR Automation & Agentic Workflow Engine**

  [![Status](https://img.shields.io/badge/Status-Online-009d9a?style=flat-square)](https://nexus.zyniq.solutions)
  [![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
  [![License](https://img.shields.io/badge/License-MIT-grey?style=flat-square)](LICENSE)

  <p align="center">
    <i>Seamlessly orchestrating identity provisioning, onboarding logistics, and governance workflows with AI-driven precision.</i>
  </p>
</div>

---

## 📋 Overview

**Nexus Orchestrator** is a high-performance control plane designed to bridge the gap between AI decision-making (via IBM watsonx or similar agents) and enterprise infrastructure. It serves as the central nervous system for HR operations, handling complex, multi-step processes like new hire onboarding, resource allocation, and compliance checks without human intervention.

Built with **FastAPI**, Nexus provides a real-time dashboard for monitoring agent activities, token usage, and system health, while exposing a robust set of RESTful endpoints for agentic interaction.

## ✨ Key Features

*   **⚡ Batch Onboarding Engine**: Provision identities, Slack workspaces, and email accounts for multiple candidates simultaneously with a single API call.
*   **📅 Intelligent Scheduling**: Smart calendar management that detects conflicts (e.g., "Manager busy on Monday") and autonomously suggests viable alternatives.
*   **🛡️ Governance & Approval**: Automated budget checks that route high-value requests (>$1k) to the CFO for approval, ensuring compliance.
*   **📊 Real-Time Telemetry**: Live dashboard tracking total API calls, estimated token savings, and active agent workflows.
*   **🔌 Extensible Architecture**: Modular design allowing easy integration with Mock Identity Providers, Slack API, and Google Calendar.

## 🚀 Tech Stack

*   **Backend**: Python 3.10+, FastAPI, Uvicorn
*   **Frontend**: HTML5, Vanilla CSS (IBM Carbon Design System inspired), JavaScript
*   **State Management**: In-memory ephemeral state (for demo/prototyping)
*   **Deployment**: Docker-ready, capable of running on Replit, AWS, or local environments.

## 🛠️ Installation & Setup

### Prerequisites
*   Python 3.8 or higher
*   `pip` (Python Package Manager)

### Quick Start

1.  **Clone the Repository**
    ```bash
    git clone git@github.com:khalilpreview/nexus-onboarding-agent.git
    cd nexus-onboarding-agent
    ```

2.  **Install Dependencies**
    ```bash
    pip install fastapi uvicorn
    ```

3.  **Run the Server**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8999 --reload
    ```

4.  **Access the Dashboard**
    Open your browser and navigate to: `http://localhost:8999`

## 🔌 API Documentation

Nexus exposes a Swagger UI for easy testing and integration. Once the server is running, visit:
`http://localhost:8999/docs`

### Core Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | **Control Plane Dashboard**: Visual interface for monitoring system status. |
| `GET` | `/api/stats` | **Telemetry**: Returns JSON data on calls, tokens saved, and logs. |
| `POST` | `/batch-onboard` | **Action**: Triggers the onboarding sequence for a list of candidates. |
| `POST` | `/book-lunch` | **Action**: Attempts to book a welcome lunch, handling schedule conflicts. |
| `POST` | `/request-approval` | **Action**: Submits a budget approval request to the governance engine. |

## 📸 Dashboard Preview

The Nexus Control Plane provides a futuristic, terminal-inspired interface to visualize agent actions in real-time.

*(Screenshot placeholder - Dashboard view)*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <small>Powered by Nexus Architecture • Designed for the Future of Work</small>
</div>
