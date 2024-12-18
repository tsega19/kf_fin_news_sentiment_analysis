
# Financial News Analysis Pipeline

## Overview

This repository provides a robust pipeline for analyzing financial news data and exploring correlations between news sentiment and stock market movements. It includes exploratory data analysis (EDA), sentiment analysis, and time series analysis to uncover insights from financial news datasets.

---

## Features

### 1. **Exploratory Data Analysis (EDA)**
- Analyze distribution and trends in news headlines.
- Investigate publisher contributions and publication frequency.

### 2. **Sentiment Analysis**
- Utilizes `TextBlob` for sentiment classification (positive, negative, neutral).
- Extracts sentiment polarity for each headline.
- Provides visualizations of sentiment distributions.

### 3. **Time Series Analysis**
- Analyzes trends in publication frequency and sentiment over time.
- Identifies patterns in publication dates and times for actionable insights.

### 4. **Git Integration**
- Structured for collaboration and CI/CD workflows using GitHub Actions.

---

## Project Structure

```plaintext
├── .vscode/
│   └── settings.json            # VSCode workspace settings
├── .github/
│   └── workflows/
│       └── unittests.yml        # GitHub Actions CI for testing
├── .gitignore                   # Git ignore file
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── src/
│   ├── __init__.py
│   └── analysis_pipeline.py     # Core analysis functions
├── notebooks/
│   ├── __init__.py
│   ├── exploratory_analysis.ipynb # Initial exploration
│   └── analysis.ipynb           # Advanced analysis with modular functions
├── tests/
│   ├── __init__.py
│   └── test_analysis.py         # Unit tests for the pipeline
└── scripts/
    ├── __init__.py
    └── run_analysis.py          # Script for automating the pipeline
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- Git

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/tsega19/kf_fin_news_sentiment_analysis.git
   cd <repository_directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scriptsctivate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the directory structure matches the project structure described above.**

---

## Usage

### 1. **Run Analysis Pipeline:**
   Execute the pipeline script:
   ```bash
<<<<<<< Updated upstream
   python scripts/*.py
=======
   python scripts/*.
>>>>>>> Stashed changes
   ```

### 2. **Interactive Analysis:**
   Open and execute the notebooks in the `notebooks/` folder for EDA and visualization:
   ```bash
   jupyter notebook
   ```

---
