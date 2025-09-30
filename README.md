# Flask Sentiment Analysis

A comprehensive Flask web application that performs sentiment analysis using Watson NLP service with a robust fallback system. This project demonstrates advanced error handling, PEP8 compliance, and modular design patterns.

![Python](https://img.shields.io/badge/python-v3.13.1-blue.svg)
![Flask](https://img.shields.io/badge/flask-v3.1.2-green.svg)
![PyLint Score](https://img.shields.io/badge/pylint-10.00/10-brightgreen.svg)

## 🌟 Features

- **Flask Web Interface**: Clean, user-friendly web interface for text input and sentiment analysis
- **Watson NLP Integration**: Primary sentiment analysis using IBM Watson NLP service
- **Intelligent Fallback System**: Rule-based sentiment analyzer when external service is unavailable
- **Robust Error Handling**: Comprehensive error handling for network issues and invalid inputs
- **PEP8 Compliant**: Achieves 10/10 PyLint score with proper code formatting and documentation
- **Modular Architecture**: Well-organized code structure with separate modules

## 🚀 Quick Start

### Prerequisites

- Python 3.13.1 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SaifRiaz3256/Flask-Sentiment-Analysis.git
   cd Flask-Sentiment-Analysis
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask requests pylint
   ```

4. **Run the application**
   ```bash
   python server.py
   ```

5. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Enter text and click "Analyze Text" to see sentiment results

## 📁 Project Structure

```
Flask-Sentiment-Analysis/
├── SentimentAnalysis/           # Sentiment analysis module
│   ├── __init__.py             # Package initialization
│   └── sentiment_analysis.py   # Core sentiment analysis logic
├── static/                     # Static files (CSS, JS)
│   └── mywebscript.js         # Frontend JavaScript
├── templates/                  # HTML templates
│   └── index.html             # Main web interface
├── server.py                  # Flask application server
├── test_fallback.py          # Fallback system tests
├── test_task7.py             # Error handling tests
├── TASK7_IMPLEMENTATION.md   # Task 7 documentation
├── .gitignore                # Git ignore rules
├── LICENSE                   # Project license
└── README.md                 # This file
```

## 🔧 How It Works

### Primary Analysis (Watson NLP)
1. User enters text in the web interface
2. Text is sent to Watson NLP service via API call
3. Service returns sentiment label (POSITIVE, NEGATIVE, NEUTRAL) and confidence score
4. Results are displayed to the user

### Fallback Analysis (Rule-based)
When the Watson service is unavailable:
1. System automatically switches to rule-based analyzer
2. Text is analyzed using predefined positive/negative word lists
3. Sentiment is calculated based on word frequency and context
4. Results maintain the same format as Watson API

### Error Handling
- **Status Code 500**: Invalid inputs return "Invalid input! Try again."
- **Connection Timeouts**: Automatic fallback to rule-based analyzer
- **Network Issues**: Graceful degradation with informative messages

## 📊 API Response Format

Both Watson NLP and fallback systems return consistent JSON format:

```json
{
    "label": "SENT_POSITIVE",
    "score": 0.85
}
```

- `label`: Sentiment classification (SENT_POSITIVE, SENT_NEGATIVE, SENT_NEUTRAL)
- `score`: Confidence score (0.0 to 1.0)

## 🧪 Testing

Run the test suites to verify functionality:

```bash
# Test fallback system
python test_fallback.py

# Test error handling (Task 7)
python test_task7.py
```

## 📋 Code Quality

This project maintains high code quality standards:

- **PyLint Score**: 10.00/10
- **PEP8 Compliant**: Full adherence to Python style guidelines
- **Comprehensive Documentation**: Docstrings for all functions and modules
- **Error Handling**: Robust exception handling throughout

## 📝 Tasks Completed

- ✅ **Task 7**: Enhanced error handling for invalid inputs and service failures
- ✅ **Task 8**: Applied PEP8 standards and achieved perfect PyLint score (10/10)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Saif Riaz** - [SaifRiaz3256](https://github.com/SaifRiaz3256)

---
⭐ **Star this repository if you found it helpful!** ⭐ 
