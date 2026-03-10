# Auction Fraud Detector

Spring 2026 Computer Science Capstone Project  
Machine Learning System for Early Fraud Detection in Online Auctions

---

## Project Overview

Online auction platforms are vulnerable to fraudulent behaviors such as shill bidding, where malicious users artificially inflate auction prices. Detecting these patterns early is critical for maintaining fair marketplaces and protecting legitimate users.

This project explores how machine learning models can analyze bidder behavior patterns to detect fraudulent activity. Using behavioral features derived from auction data, the system trains classification models to distinguish between legitimate and fraudulent bidding behavior.

The trained model is integrated into an interactive **Streamlit web application** that allows users to input bidding behavior features and receive a real-time fraud prediction.

---

## Machine Learning Models

Two supervised learning models were trained and evaluated:

- Logistic Regression
- Random Forest Classifier

The models were evaluated using several performance metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- AUC (Area Under the ROC Curve)

The Random Forest model demonstrated the strongest overall performance and was used for the deployed prediction interface.

---

## Project Structure
auction-fraud-detector
│
├── app.py # Streamlit application interface
├── fraud_model.pkl # Trained machine learning model
├── feature_names.pkl # Feature order used by the model
├── requirements.txt # Python dependencies
└── README.md


---

## Running the Application Locally

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/auction-fraud-detector.git

```

### 2. Install Required Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Application

Start the web application using:

```bash
streamlit run app.py
```

### 4. Open the Application

After running the command, Streamlit will launch a local server.

Open your browser and go to:

```bash
http://localhost:8501
```
