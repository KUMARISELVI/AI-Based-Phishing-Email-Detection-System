## Key Features
- Secure session-based authentication
- Machine learning-based email classification
- Probability-based risk scoring (0–100) with severity categories (High, Medium, Low)
- Persistent logging with MySQL
- Interactive dashboard with dynamic KPIs and Chart.js visualizations
- CSV export of threat logs
- Server-side pagination
- Real-time alerts for high-risk emails

## Machine Learning Pipeline
1. Email text preprocessing (lowercasing & cleaning)
2. Feature extraction using TF-IDF
3. Classification using Logistic Regression
4. Risk score calculation from model probability
5. Severity assignment based on risk score
6. Store results in MySQL
7. Update dashboard analytics in real-time

## System Architecture
- **Frontend:** HTML, CSS, JavaScript
- **Backend/API Layer:** Flask (Python)
- **Machine Learning Model:** Scikit-learn
- **Database:** MySQL for data persistence

## Technology Stack
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, TF-IDF, Logistic Regression
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Visualization:** Chart.js

