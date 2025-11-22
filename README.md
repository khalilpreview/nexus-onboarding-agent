<div align="center">
  <img src="./nexus_logo.png" alt="Nexus Orchestrator Logo" width="100%" style="max-width: 800px; border-radius: 10px; margin-bottom: 20px;">

  # Nexus // Orchestrator
  
  **AI Agent Skill Demonstration for IBM watsonx Orchestrate**

  [![Hackathon](https://img.shields.io/badge/Hackathon-IBM_watsonx_Orchestrate-0F62FE?style=flat-square)](https://www.ibm.com/watsonx)
  [![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-Prototype-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
  [![Status](https://img.shields.io/badge/Status-Demo-009d9a?style=flat-square)](https://nexus.zyniq.solutions)

  <p align="center">
    <i>A proof-of-concept showcasing agentic AI capabilities for HR automation workflows.</i>
  </p>
</div>

---

## 🎯 Project Purpose

This is a **demonstration project** created for the **Agentic AI Hackathon with IBM watsonx Orchestrate**. It serves as a proof-of-concept to showcase how AI agents can interact with custom tools and APIs to automate complex HR workflows.

**This is NOT production-ready software** — it's designed to illustrate the potential of agentic AI systems and demonstrate tool-calling patterns that could be integrated with IBM watsonx Orchestrate.

## 💡 The Concept

Nexus Orchestrator simulates an intelligent backend that AI agents can interact with to perform HR operations. The idea is to demonstrate:

- **Tool-Calling Capabilities**: How AI agents can invoke specific functions (batch onboarding, calendar management, device procurement)
- **Workflow Orchestration**: Chaining multiple API calls to complete complex tasks
- **Intelligent Decision-Making**: Handling conflicts, suggesting alternatives, and routing approvals
- **Real-Time Monitoring**: Visualizing agent activities through a live dashboard

## ✨ Demonstrated Capabilities

### 🤖 AI Agent Skills

*   **📦 Batch Onboarding**: Process multiple new hires in a single operation (identity creation, Slack invites, email provisioning)
*   **📅 Smart Scheduling**: Book welcome lunches with conflict detection and alternative suggestions
*   **💻 Device Procurement**: Order IT equipment with automated order tracking
*   **🛡️ Governance Routing**: Detect budget thresholds and route approval requests to appropriate stakeholders
*   **🔑 Identity Management**: Generate credentials and provision access to enterprise systems

### 📊 Monitoring Dashboard

A real-time control plane that visualizes:
- Total API calls made by agents
- Estimated token savings from batch operations
- Live log stream of agent activities
- Simulated agent conversation preview

## 🚀 Quick Start

### Prerequisites
*   Python 3.8+
*   `pip` package manager

### Installation

1.  **Clone the Repository**
    ```bash
    git clone git@github.com:khalilpreview/nexus-onboarding-agent.git
    cd nexus-onboarding-agent
    ```

2.  **Install Dependencies**
    ```bash
    pip install fastapi uvicorn
    ```

3.  **Run the Demo Server**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8999 --reload
    ```

4.  **View the Dashboard**
    Navigate to: `http://localhost:8999`

5.  **Explore the API**
    Interactive docs: `http://localhost:8999/docs`

## 🔌 API Endpoints (Agent Tools)

| Endpoint | Purpose | Example Use Case |
| :--- | :--- | :--- |
| `POST /batch-onboard` | Onboard multiple employees | "Add John, Sarah, and Mike to Engineering" |
| `POST /book-lunch` | Schedule welcome meetings | "Book lunch for the new hire on Monday" |
| `POST /order-device` | Procure IT hardware | "Order a MacBook Pro for john@company.com" |
| `POST /request-approval` | Submit budget requests | "Request approval for $5,000 training budget" |
| `GET /api/stats` | Retrieve telemetry data | Dashboard updates, monitoring |

## 🎨 Tech Stack

*   **Backend**: FastAPI (Python) - Lightweight, fast API framework
*   **Frontend**: Vanilla HTML/CSS/JS - IBM Carbon Design System inspired
*   **State**: In-memory (ephemeral) - Resets on restart
*   **Deployment**: Designed for quick demos (Replit, local, cloud)

## 🧪 Integration with IBM watsonx

This API is designed to be consumed by AI agents built with IBM watsonx Orchestrate. The OpenAPI specification (`onboarding-api.json`) can be imported directly into watsonx to enable:

1. **Natural Language → API Calls**: Users can say "Onboard 3 new engineers" and the agent translates this to `/batch-onboard`
2. **Multi-Step Workflows**: Chain operations like onboarding → device ordering → lunch scheduling
3. **Error Handling**: Agents can interpret conflict responses and suggest alternatives
4. **Token Optimization**: Batch operations reduce the number of LLM calls needed

## 📝 Hackathon Context

**Challenge**: Demonstrate how agentic AI can automate enterprise workflows  
**Solution**: A mock HR orchestration layer that showcases realistic tool-calling patterns  
**Key Innovation**: Real-time dashboard + batch operations that show token efficiency gains  

## ⚠️ Important Notes

- **Not for Production**: This is a prototype with in-memory state and no authentication
- **Mock Integrations**: Identity providers, Slack, and calendar systems are simulated
- **Educational Purpose**: Designed to inspire ideas for real-world agentic AI applications

## 🤝 Contributing

This is a hackathon project, but ideas and improvements are welcome!

1.  Fork the repository
2.  Create a feature branch
3.  Submit a pull request with your enhancements

## 📄 License

MIT License - Feel free to use this as a starting point for your own projects.

---

<div align="center">
  <small>Built for the IBM watsonx Orchestrate Agentic AI Hackathon</small><br>
  <small>Showcasing the Future of Intelligent Automation</small>
</div>
