# Insurance Cost Prediction App

> **Predict medical insurance charges** based on personal and medical history using a Linear/Regularized Regression model, packaged in a sleek Streamlit web app.

---

## 🚀 Project Overview

A machine learning project that:

* **Predicts** insurance charges for individuals.
* **Compares** the performance of Linear, Ridge, and Lasso regression models.
* Applies **log transformation** (optional) for skewed targets to improve R².
* Provides an **interactive UI** via a Streamlit app for real-time predictions.

---

## 📂 Folder Structure

```
InsuranceCostPredictor/
├── app.py                   # Streamlit application
├── insurance_model.pkl      # Trained regression model (Pickle)
├── requirements.txt         # Python dependencies
├── .gitignore               # Files to ignore in Git
├── screenshots/            # Plots: smoker_vs_charges.png, bmi_vs_charges.png
└── README.md                # Project documentation
```

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/insurance-cost-predictor.git
   cd insurance-cost-predictor
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\\Scripts\\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Data & Features

* **Dataset**: Kaggle Medical Insurance Dataset (Mirichoi0218).
* **Core features**:

  * `age`, `sex`, `bmi`, `children`, `smoker`, `region`
  * Extended features: `Claim_Amount`, `past_consultations`, `Hospital_expenditure`, `NUmber_of_past_hospitalizations`, `Anual_Salary`
* **Target**: `charges` (insurance cost)
* **Preprocessing**:

  * Handle missing values by removal or imputation.
  * Label encoding for categorical variables.
  * Optional log transformation of `charges` for improved model performance.

---

## 📊 Model Training & Evaluation

1. **Train-test split**: 80/20 split
2. **Scaling**: StandardScaler on numerical features
3. **Models compared**:

   * **Linear Regression**
   * **Ridge Regression** (α tuned)
   * **Lasso Regression** (α tuned)
4. **Metrics**:

   * R² Score (up to 85% achieved)
   * RMSE (Root Mean Squared Error)

> **Tip**: Use cross-validation and grid search to fine-tune `alpha` for Ridge/Lasso.

---

## 🎨 Visualizations

Here are the actual plots based on our dataset:

<img src="screenshots/regression_plot.png" alt="Regression Plot" width="500" />
<p align="center"><b>Figure 1:</b> Regression Line: Actual vs Predicted Insurance Charges</p>

<img src="screenshots/smoker_vs_charges.png" alt="Smoker vs Charges" width="500" />
<p align="center"><b>Figure 2:</b> Insurance Charges Comparison: Smokers vs Non-Smokers</p>

> 📂 You can find these images inside the `screenshots/` folder.

## 🖥️ Running the App

1. Ensure `insurance_model.pkl` is in the project root.
2. Launch Streamlit:

   ```bash
   streamlit run app.py
   ```
3. Open [`http://localhost:8501`](http://localhost:8501) in your browser.

---

## ☁️ Deployment

* Deployed on **Streamlit Community Cloud**.
* **Live Demo**: [https://share.streamlit.io/your-username/insurance-cost-predictor/main/app.py](#)

---

## 🤝 Contributing

1. Fork this repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

<p align="center">Made with ❤️ and ☕ by Your Name</p>
