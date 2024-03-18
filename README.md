# Cirrhosis-Prediction-with-AI
### Context

The dataset contains laboratory values of blood donors and patients with Hepatitis C, along with demographic information such as age. The data was obtained from the UCI Machine Learning Repository: [HCV Data](https://archive.ics.uci.edu/ml/datasets/HCV+data).

### Content

All attributes except "Category" and "Sex" are numerical. The attributes are organized as follows:

#### Patient Data (Attributes 1 to 4):
1. X (Patient ID/Number)
2. Category (Diagnosis) - Values: '0=Blood Donor', '0s=Suspect Blood Donor', '1=Hepatitis', '2=Fibrosis', '3=Cirrhosis'
3. Age (in years)
4. Sex (Male or Female)

#### Laboratory Data (Attributes 5 to 14):
5. ALB (Albumin)
6. ALP (Alkaline Phosphatase)
7. ALT (Alanine Aminotransferase)
8. AST (Aspartate Aminotransferase)
9. BIL (Bilirubin)
10. CHE (Cholinesterase)
11. CHOL (Cholesterol)
12. CREA (Creatinine)
13. GGT (Gamma-Glutamyl Transferase)
14. PROT (Protein)

The target attribute for classification is "Category", which distinguishes between blood donors and Hepatitis C patients, including the progression of the disease (Hepatitis C, Fibrosis, Cirrhosis).
1. [Data Overview](#data-overview)
2. [Importing Libraries](#importing-libraries)
3. [Data Cleaning & Preprocessing](#data-cleaning-and-preprocessing)
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
    - [Univariate Analysis](#univariate-analysis)
    - [Bivariate Analysis](#bivariate-analysis)
    - [Multivariate Analysis](#multivariate-analysis)
5. [Data Encoding](#data-encoding)
6. [Data Scaling](#data-scaling)
7. [Data Modeling](#data-modeling)
8. [Model Evaluation](#model-evaluation)
9. [Pipeline](#pipeline)
10. [Deployment](#deployment)
