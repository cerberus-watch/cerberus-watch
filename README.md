# Project Cerberus Watch

A multi-headed digital sentinel for OSINT, security, and safety.

![Cerberus Logo](assets/images/cerberus_logo.png)

## 🔍 Overview

Project Cerberus is a modular security and intelligence platform designed to operate locally/off-grid with a focus on OSINT, security monitoring, and safety tools. The system is built with a "multi-headed" architecture, where each "head" specializes in different aspects of security and intelligence gathering.

## 🐉 Cerberus Heads

Each head of Cerberus represents a specialized subsystem:

- **Aegis**: Core infrastructure and LLM integration
- **Recon**: OSINT and reconnaissance capabilities
- **Wraith**: Stealth monitoring and tracking
- **Oren**: Threat intelligence and analysis
- **Mavrakis**: Social engineering and persona management
- **Chroma**: Visual analysis and media processing

## 🏗️ Repository Structure

```
cerberus-watch/
├── heads/              # Specialized subsystems
│   ├── aegis/          # Core infrastructure and LLM integration
│   ├── recon/          # OSINT and reconnaissance
│   ├── wraith/         # Stealth monitoring and tracking
│   ├── oren/           # Threat intelligence and analysis
│   ├── mavrakis/       # Social engineering and persona management
│   └── chroma/         # Visual analysis and media processing
├── agents/             # AI agent configurations
├── hardware/           # Hardware setup and configurations
├── assets/             # UI assets, images, and resources
│   ├── images/
│   ├── icons/
│   ├── fonts/
│   ├── css/
│   └── js/
└── docs/               # Documentation
```

## 🚀 Running with Docker

This project is containerized using Docker and managed with Docker Compose. This is the recommended way to run the application for both development and production.

### Prerequisites
- Docker Engine
- Docker Compose

### Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/cerberus-watch.git
   cd cerberus-watch
   ```

2. **Build and run the services:**
   ```bash
   docker compose up --build
   ```
   This command will build the Docker image and start the **Athena** service. You can access the Athena UI by navigating to **http://localhost:8000** in your web browser.

> **Note on Docker Hub Rate Limits:**
> The initial build process may fail with a `429 Too Many Requests` error. This is due to Docker Hub's pull rate limits for anonymous users. To resolve this, simply authenticate with your Docker Hub account by running `docker login` in your terminal and then re-run the `docker compose up` command.

## 🔒 Security Features

- **Local-First**: Designed to run entirely on your own hardware
- **Off-Grid Capable**: Can operate without internet connectivity
- **Modular Design**: Use only the components you need
- **Themes**: Choose between "Hacker Mode" and "Nosy Neighbor Mode"

## 🛠️ Development Stack

- **Backend**: FastAPI
- **Frontend**: React
- **LLM Integration**: Ollama (LLaMA 3), GPT4All, LangChain
- **Hosting**: Docker, docker-compose, multi-stage builds
- **Mobile Support**: Termux on Android

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.