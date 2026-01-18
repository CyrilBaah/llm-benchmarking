# LLM Benchmarking Dashboard 🚀

A Streamlit application for real-time comparison of Large Language Models (LLMs) across key performance metrics: **latency**, **token usage**, and **throughput**.

Currently supports:
- **Google Gemini 2.5 Flash** (via Google GenAI SDK)
- **Groq Llama 3.1 8B Instant** (via Groq SDK)

## Installation

### Prerequisites
- Python 3.11 or higher
- API keys for the models you want to test

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/CyrilBaah/llm-benchmarking.git
cd llm-benchmarking
```

2. **Create a virtual environment**
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install streamlit google-genai groq pandas plotly
```

## Configuration

### API Keys Setup

Create a `.streamlit/secrets.toml` file in your project directory:

```toml
GEMINI_API_KEY = "your-google-gemini-api-key"
GROQ_API_KEY = "your-groq-api-key"
```

**⚠️ Important**: Never commit this file to version control. Add it to `.gitignore`.

### Getting API Keys

**Google Gemini API**:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy to your `secrets.toml`

**Groq API**:
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up and generate an API key
3. Copy to your `secrets.toml`

## Usage

### Running the App

```bash
streamlit run home.py
```

## Project Structure

```
llm-benchmarking/
├── home.py                 # Main Streamlit application
├── env/                    # Virtual environment
├── .streamlit/
│   └── secrets.toml        # API keys (not committed)
├── README.md               # This file
└── .gitignore
```