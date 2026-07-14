<div align="center">
  <br />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Human_Development_Index_%28HDI%29.svg/1024px-Human_Development_Index_%28HDI%29.svg.png" alt="HDI Map" width="400" />
  <h1>🌍 Human Development Index (HDI) Predictor</h1>
  <p>
    <strong>A Comprehensive, Machine Learning-Powered Measure of Global Well-Being</strong>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.13-blue.svg?style=for-the-badge&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/Flask-3.x-white.svg?style=for-the-badge&logo=flask&logoColor=black" alt="Flask">
    <img src="https://img.shields.io/badge/scikit--learn-1.9-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
    <img src="https://img.shields.io/badge/Bootstrap-5-7952B3.svg?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  </p>
</div>

<br />

## 📖 Table of Contents
- [Project Description](#-project-description)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [System Architecture](#-system-architecture)
- [Model Performance](#-model-performance)
- [Local Installation](#-local-installation)
- [Cloud Deployment (Render)](#-cloud-deployment-render)
- [Development Team](#-development-team)
- [License](#-license)

---

## 🎯 Project Description
The **Human Development Index (HDI) Predictor** is an end-to-end Machine Learning web application designed to instantly evaluate the human development tier of a hypothetical region based on core socioeconomic indicators. 

The HDI was created by the United Nations Development Programme (UNDP) to emphasize that people and their capabilities should be the ultimate criteria for assessing the development of a country, rather than economic growth alone. This project democratizes access to complex UN statistical calculations by translating decades of global historical data (1990-2022) into an accessible, real-time prediction interface.

---

## ✨ Key Features
- **Deterministic Accuracy**: Uses an optimized Multiple Linear Regression model to perfectly map real-world indicators back to the UNDP's geometric index calculations.
- **"Google-Grade" UI/UX**: A highly responsive, Material 3 inspired Bento-grid web interface built with Bootstrap 5.
- **Dynamic Data Visualization**: Generates color-coded status badges and animated gauge charts to contextualize the predicted HDI score against standard global development tiers.
- **Interactive Project Portal**: An integrated, SPA-style documentation hub detailing the exact SDLC, API specs, and risk mitigations for academic evaluation.

---

## 💻 Technology Stack

| Category | Technologies Used |
|---|---|
| **Backend Framework** | Python 3.13, Flask, Gunicorn (WSGI) |
| **Machine Learning** | Scikit-Learn, NumPy |
| **Data Engineering** | Pandas, Matplotlib, Seaborn (Jupyter Notebooks) |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5 |
| **Deployment** | Render (PaaS) |

---

## 🧠 Machine Learning Workflow
1. **Data Acquisition**: Integrated the Kaggle HDR Dataset (1990–2022) alongside the Official UNDP 2025 Statistical Annex.
2. **Exploratory Data Analysis (EDA)**: Analyzed feature distributions, handled missing values, and validated Pearson correlation matrices (`>0.90` correlation with health/education).
3. **Data Preprocessing**: Implemented a mathematical `np.log()` transformation on Gross National Income (GNI) to normalize severe global wealth skewness.
4. **Ablation Study & Training**: Proved through testing that a standard scaled model offered zero improvement over an unscaled model due to the linear nature of the index. Trained a lightweight Linear Regression model.
5. **Serialization**: Exported the final pipeline via `pickle` for integration with the Flask API memory space.

---

## 🏗️ System Architecture

```text
[ Client Browser (HTML/CSS/JS) ]
        | (POST Form Data)
        v
[ Flask API Server (app.py) ] --> [ Input Validation & np.log() Transformation ]
        |
        v
[ Scikit-Learn (HDI.pkl) ] --> [ Linear Regression Predictor ]
        | (Returns Float 0.000 - 1.000)
        v
[ Flask Template Engine ] --> [ result.html (Gauge UI) rendered back to Client ]
```

---

## 📊 Model Performance
Because the HDI target label is synthesized using a deterministic rule-based heuristic, our linear model reconstructs the mathematical mapping almost perfectly on the cleaned dataset.

* **R² Score:** `0.9986` (Explains 99.86% of the variance in human development)
* **Mean Absolute Error (MAE):** `0.0038`
* **Root Mean Squared Error (RMSE):** `0.0060`

---

## ⚙️ Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/HumanDevelopmentIndex.git
   cd HumanDevelopmentIndex
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\Activate.ps1
   # On MacOS/Linux:
   source venv/bin/activate
   ```

3. **Install exact dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Web Server:**
   ```bash
   python app.py
   ```
   *Visit `http://localhost:5000` in your browser.*

---

## 🚀 Cloud Deployment (Render)
This repository is pre-configured for PaaS deployments via the included `Procfile`.
1. Fork or clone this repository to your GitHub account.
2. Sign up / Log in to [Render](https://render.com/).
3. Create a new **Web Service** and connect your GitHub repository.
4. Configure the Build Command: `pip install -r requirements.txt`
5. Configure the Start Command: `gunicorn app:app`
6. Click **Deploy Web Service**.

---



## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
