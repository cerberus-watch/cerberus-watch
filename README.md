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

## 🚀 Getting Started

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/cerberus-watch.git
   cd cerberus-watch
   ```

2. **Set up the core Aegis infrastructure**
   ```bash
   cd heads/aegis
   # Follow the setup instructions in the Aegis README
   ```

3. **Configure additional heads as needed**
   Each head has its own setup instructions in its respective directory.

## 🌐 Dashboard

The Cerberus dashboard provides a unified interface for interacting with all heads of the system. To access the dashboard:

1. Ensure the Aegis head is running
2. Navigate to `http://localhost:3000` in your browser
3. Log in with your credentials

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