# Sentiment-Analysis

## Table of Contents 📋
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Difficulties](#difficulties)
- [Points to Improve](#points-to-improve)
- [Tools](#tools)
- [Architecture](#architecture)
- [Dashboard](#dashboard)
- [Contact](#contact)

## 🚀 Overview
This project focuses on implementing an exhaustive sentiment analysis of user feedback and reviews. The goal is to interpret user opinions about various courses using **Natural Language Processing (NLP)** techniques for a more contextual and accurate understanding of comments.

Key features include:
1. **NLP-based sentiment analysis** to process and understand the user feedback.
2. **Language translation** feature supporting 133 languages, allowing users to express their opinions in their native language, fostering a more inclusive experience.
3. **Chatbot integration** to enhance overall user interaction by providing personalized and efficient communication assistance.

## 🛠️ Installation
To set up and run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sentiment-analysis.git
    ```
2. Navigate to the project directory:
    ```bash
    cd sentiment-analysis
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up NLP models for sentiment analysis:
    Install spaCy and download the required language models:
    ```bash
    pip install spacy
    python -m spacy download en_core_web_sm
    ```

5. Set up the translation API (if using a cloud service like Google Translate):
    Add your API keys to the configuration file:
    ```bash
    export GOOGLE_TRANSLATE_API_KEY=your-api-key
    ```

6. Run the chatbot:
    ```bash
    python chatbot.py
    ```

## 🚀 Usage
This project includes various modules for sentiment analysis, language translation, and a chatbot.

### Steps to use the project:

1. **Run the sentiment analysis** module to analyze feedback:
    ```bash
    python analyze_sentiment.py --input feedback.csv --output results.csv
    ```
2. **Use the translation feature** to convert user feedback into the desired language:
    ```bash
    python translate.py --input feedback.csv --language fr
    ```
3. **Interact with the chatbot** for a more personalized experience:
    ```bash
    python chatbot.py
    ```

## 🛠️ Difficulties
- Accurately capturing the sentiment of user reviews in multiple languages.
- Ensuring efficient translation across 133 languages.
- Handling complex feedback structures during NLP processing.
- Improving the interpretation of **oxymorons** (contradictory terms) in user reviews.
- Handling **emojis** (visual symbols) that could cause ambiguity during sentiment analysis, as their meaning may vary depending on context and culture.
- Effectively interpreting the use of **colors** in textual feedback, as colors can carry emotional or cultural significance that impacts sentiment.


## 🔧 Points to Improve
- Improve the accuracy of the sentiment analysis model.
- Optimize the translation feature to support real-time translations.
- Enhance chatbot responsiveness and add more interaction scenarios.

## 🛠 Tools
- **SVM/naive bais/NLTKes Réseaux de Neurones/**: For NLP and sentiment analysis.
- **Google Translate API**: For handling multi-language translations.
- **Streamlit**: Backend framework for chatbot integration.
- **Git**: For version control.

## 🏗 Architecture
The architecture of the project consists of:
1. **Raw Data**: User feedback and reviews collected from various courses.
2. **NLP Pipeline**: For cleaning, processing, and analyzing feedback using spaCy.
3. **Translation Module**: For converting feedback into 133 different languages.
4. **Chatbot Module**: For interactive user assistance.

![Project Architecture](Sentiment-Analysis/projet_machine_learning/report/sentiment.png)

## 📞 Contact
For any questions or issues, feel free to reach out:
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samiha-el-mansouri-27505b250/)
