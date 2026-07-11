# Phishing Email Detection Model

## Overview

The **Phishing Email Detection Model** is a machine learning project developed using Python and Scikit-learn to classify emails as **Phishing** or **Legitimate**. The model uses Natural Language Processing (NLP) techniques to extract features from email text and predicts whether an email is malicious.

> **Note:** This project is intended for educational and internship purposes.

---

## Features

- Detect phishing emails using Machine Learning
- Text preprocessing using TF-IDF Vectorizer
- Email classification using Naive Bayes
- Predict custom email messages
- Save trained model using Joblib
- Simple and easy-to-understand Python code

---

## Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## Project Structure

```text
Phishing-Email-Detection-Model/
│── phishing_detector.py
│── emails.csv
│── requirements.txt
│── README.md
│── phishing_model.pkl
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Phishing-Email-Detection-Model.git
```

Move into the project folder:

```bash
cd Phishing-Email-Detection-Model
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python phishing_detector.py
```

Enter an email message when prompted.

Example:

```
Enter an email:
Congratulations! You have won a free iPhone. Click here.
```

Output:

```
⚠️ Prediction: PHISHING
```

Another example:

```
Enter an email:
Meeting has been scheduled for tomorrow at 10 AM.
```

Output:

```
✅ Prediction: LEGITIMATE
```

---

## Dataset

The dataset (`emails.csv`) contains two columns:

- **text** – Email message
- **label** – phishing or legitimate

---

## Future Enhancements

- Deep Learning (LSTM/BERT)
- Flask or Django Web Application
- Email Attachment Analysis
- URL Reputation Checking
- Real-time Email Scanning
- Web Browser Extension

---

## Learning Outcomes

- Machine Learning Fundamentals
- Natural Language Processing (NLP)
- Text Classification
- Data Preprocessing
- Model Training and Evaluation
- Python Programming

---

## License

This project is licensed under the **MIT License**.

---

## Author

**Bhaathma E. D.**  
B.E. Computer Science and Engineering (Cyber Security)  
Arunai Engineering College  
Internship Mini