# Comparative Analysis of Heart Disease Datasets  

This project performs a comprehensive **comparative data science study** on two independent heart disease datasets.  
The aim is to explore, preprocess, and model the data, and finally synthesize insights into common and unique risk factors associated with heart disease.  

---

## 📂 Project Structure  

---

## 🚀 Workflow  

1. **Data Overview** (`01_data_overview.ipynb`)  
   - Initial inspection, missing values, duplicates, distributions, correlations.  

2. **Preprocessing** (`02_preprocessing.ipynb`)  
   - Data cleaning, feature scaling, harmonization of datasets.  

3. **Exploratory Data Analysis (EDA)** (`03_eda_dataset_1.ipynb`, `04_eda_dataset_2.ipynb`)  
   - In-depth analysis of distributions, correlations, and outliers.  

4. **Statistical Testing** (`05_stats_tests.ipynb`)  
   - Shapiro–Wilk normality test.  
   - Mann–Whitney U test for group comparisons.  

5. **Modeling**  
   - Logistic Regression and Random Forest models applied to each dataset (`06` and `07`).  
   - Performance evaluation with metrics and ROC curves.  

6. **Comparative Analysis** (`08_comparative_analysis.ipynb`)  
   - Side-by-side comparison of features, test results, and modeling outcomes.  

7. **Error Analysis** (`09_error_analysis.ipynb`)  
   - Identification of model misclassifications and weaknesses.  

8. **Final Report** (`10_final_report.ipynb`)  
   - Consolidation of results and insights.  

---

## 🧪 Statistical Insights  

- Most features are **not normally distributed** (Shapiro–Wilk test).  
- **Mann–Whitney U test** highlights key discriminative features:  
  - **Age** → consistently significant in both datasets.  
  - **Troponin** and **kcm** → significant in Dataset 1.  
  - **Cholesterol** → significant in Dataset 2.  

---

## 📊 Modeling Results  

- **Logistic Regression** provides baseline interpretability.  
- **Random Forest** shows stronger performance and highlights important features.  
- Cross-validation ensures robust evaluation.  

---

## 🔑 Key Takeaways  

- Age is a **robust risk factor** across datasets.  
- Dataset-specific variables (troponin, cholesterol, kcm) provide additional insight.  
- Consistency and divergence between datasets highlight population differences and data collection variability.  

---

## ⚙️ Requirements  

Install dependencies with:  

```bash
pip install -r requirements.txt
