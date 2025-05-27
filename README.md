# AI-Child Standalone

AI-Child is a modular, standalone AI automation and monitoring framework, written primarily in Python. It is designed for advanced memory-augmented automation, threat detection, log analysis, and interactive controls through both web and voice interfaces.

---

## Features

- **Memory-Augmented AI:**  
  Integrates long-term memory using vector databases and LLMs for context-aware suggestions and Q&A (see `cortex_brain_llm.py`).
- **Automated Log and Threat Monitoring:**  
  Scans memory logs for suspicious activity, open ports, or threat keywords; provides alerts and voice notifications (`alert_engine.py`).
- **Autonomous Data Ingestion:**  
  Watches directories for new files and ingests code and data for further processing (`auto_ingest.py`).
- **Web Command Panel:**  
  Interactive HTML panels (see `cortex_panel.html`) for triggering scans, alerts, memory queries, and voice output.
- **REST API:**  
  Endpoints for logs, alerts, suggestions, and triggering reports (see `server.py`).
- **Voice Output:**  
  Text-to-speech engine for spoken alerts and responses.

---

## Installation

### Prerequisites

- Python 3.8+
- (Optional) Local LLM runner such as [Ollama](https://ollama.com/) for local model inference
- ChromeDB for vector database (see `cortex_brain_llm.py` for integration)
- Node.js (for some frontend/JS features, if extended)
- (Windows) Some scripts assume Windows directories (see `auto_ingest.py` and `.bat` files)

### Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/phantomxes/AI-Child.git
   cd AI-Child
   ```

2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare Directories:**
   - The application uses directories like `~/1man.army/memory` and `~/1man.army/intel_drop` in your home directory.
   - Ensure these exist and have proper permissions.

4. **(Optional) Configure environment variables:**  
   If needed, copy `.env.example` to `.env` and modify as required.

---

## Usage

### Running the Backend Server

```sh
python server.py
```

By default, this runs a Flask server on port 5000 with REST endpoints for logs, alerts, and suggestions.

### Autonomous Ingestion

```sh
python auto_ingest.py
```
Watches `~/1man.army/intel_drop` for new files and ingests them.

### Threat Monitoring

```sh
python alert_engine.py
```
Scans the memory log for dangerous ports, keywords, and triggers voice alerts.

### Memory Q&A with LLM

```sh
python cortex_brain_llm.py
```
Starts an interactive Q&A loop with the AI's memory context, using vector search and LLM responses.

### Web Command Panel

Open `cortex_panel.html` in your browser (or use the `/templates/cortex_panel.html` variant) while running the backend to interact with the system visually.

---

## REST API Endpoints

- `/api/ai/log` &mdash; Get recent memory log entries
- `/api/ai/alerts` &mdash; Get current alert flags
- `/api/ai/suggestion` &mdash; Get usage-based tactical suggestions
- `/api/trigger/report` &mdash; Trigger PDF report generation

---

## Directory Structure

```
AI-Child/
├── app/                  # (App submodules)
├── src/                  # (Source files)
├── templates/            # Web UI templates (HTML)
├── *.py                  # Main Python modules
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Contributing

Contributions and suggestions are welcome!  
Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.
