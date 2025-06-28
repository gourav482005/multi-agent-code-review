# 🧠 Multi-Agent Code Review with Ollama (LLaMA 3)

This project is a local AI-based code review system using LLaMA 3 via Ollama.

## ⚙️ How It Works
- Scans Python files in a folder.
- Sends each file's content to a local LLaMA 3 model.
- Returns detailed reviews (e.g., security, quality, optimization).

## 🤖 Agents Included
- Security Agent
- Code Quality Agent
- Optimization Agent *(Extendable)*

## 🛠️ Setup Instructions
1. Download and install Ollama from [https://ollama.com](https://ollama.com)
2. Run in terminal:
   ```bash
   ollama run llama3
