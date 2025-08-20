# Comparative Analysis of Heart Disease Datasets with Logistic Regression and Random Forest

## Project Overview
This project analyzes and compares two independent datasets related to **heart disease**.  
The main objectives are:
- Identify and evaluate key **risk factors** for heart disease.
- Apply **statistical hypothesis testing** to explore significant differences.
- Train and compare **Logistic Regression** and **Random Forest** models.
- Assess model performance using metrics such as **accuracy, precision, recall, F1-score, ROC curve, and AUC**.
- Provide a **comparative evaluation** across both datasets and models to highlight trade-offs between interpretability and predictive power.

The project is structured for transparency and reproducibility, following a clean research workflow.

---

## Folder Descriptions

- **`data/`**  
  Contains all datasets used in the project (`heart_disease_dataset.csv` and `heart.csv`) along with a `README.md` explaining the source, structure, and description of each variable.

- **`notebooks/`**  
  Stores all Jupyter notebooks organized by workflow stage:  
  - `01_data_overview.ipynb` – initial dataset review and descriptive statistics  
  - `02_preprocessing.ipynb` – data cleaning and preparation  
  - `03_eda_dataset1.ipynb` / `04_eda_dataset2.ipynb` – exploratory analysis for each dataset  
  - `05_statistical_tests.ipynb` – Shapiro-Wilk, Mann-Whitney U, and other tests  
  - `06_modeling_dataset1.ipynb` / `07_modeling_dataset2.ipynb` – model training and evaluation  
  - `08_comparative_analysis.ipynb` – model and dataset comparison  
  - `09_final_report.ipynb` – final conclusions and documentation for submission  

- **`tests/`**  
  Includes automated and statistical testing:  
  - `unit_tests.py` – unit tests for Python functions  
  - `hypothesis_tests.py` – statistical hypothesis tests  

- **`src/`**  
  Contains Python scripts with reusable functions, classes, and utility modules used across notebooks.

- **`reports/`**  
  Stores final outputs such as tables, metrics, and summary documents.

- **`visuals/`**  
  Contains saved plots, charts, and figures generated during the analysis.

- **`docs/`**  
  Holds documentation, additional notes, theoretical references, and bibliographic sources.

- **`requirements.txt`**  
  Lists all Python packages and dependencies required to run the project.

---

## Installation & Usage

To reproduce the analysis locally:

```bash
# Clone the repository
git clone https://github.com/plamensve/DS_FINAL_PROJECT.git
cd DS_FINAL_PROJECT

# Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
