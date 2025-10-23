# 📘 Google Play Store Apps Rating Prediction

**Domain:** Data Analytics | Machine Learning | Streamlit Dashboard  
**Developer:** Amit Khotele  
**Project Link:**https://playstore.streamlit.app/

---

## 🔍 Project Overview

The mobile app market has grown exponentially over the past decade, with millions of apps on the Google Play Store. This project analyzes app data to uncover trends, relationships, and patterns that influence user ratings. Using machine learning, it predicts app ratings and provides an interactive dashboard for exploration.

By leveraging Python, Machine Learning, and Streamlit, this project delivers data-driven insights to help developers and marketers enhance app quality and visibility.

---

## 🎯 Objectives

- Analyze and visualize app trends on the Google Play Store.  
- Identify factors influencing app ratings.  
- Build a machine learning model to predict app ratings.  
- Create an interactive Streamlit dashboard for exploration and prediction.  

---

## 🧰 Tools & Technologies

| Category | Tools / Frameworks |
|----------|------------------|
| Programming Language | Python |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn, Joblib |
| Dashboard | Streamlit |
| Dataset | Google Play Store Apps Dataset (`googleplaystore.csv`) |
| IDE | Jupyter Notebook / VS Code |
| Model | Random Forest Regressor |

---

## 🧹 Data Preprocessing

The dataset had 10,000+ app records with inconsistencies. Key preprocessing steps:

- Removed duplicate entries.  
- Converted text-based numeric fields:
  - Reviews: e.g., `"1M"`, `"1k"` → numeric  
  - Installs: removed commas and `"+"`  
  - Size: standardized into KB  
  - Price: removed `$` and converted to numeric  
- Converted `Last Updated` to datetime and calculated `App_Age_years`.  
- Created categorical features:
  - `Price_Category`: Free / Low / Medium / Premium  
  - `Rating_Level`: Low / Average / High  
  - `Install_Band`: e.g., 0–1K, 1K–10K  
  - `Primary_Genre`: extracted first genre  

---

## 📊 Exploratory Data Analysis (EDA)

**Key Insights:**

- Most common categories: Family, Game, Tools, Productivity, Lifestyle  
- Majority of apps rated 4.0–4.5  
- Over 90% of apps are free  
- Dominant content rating: "Everyone"  
- Top genres by installs: Tools, Entertainment, Communication  
- Strong correlation between Reviews & Installs with Ratings  

**Visualizations:**

- Distribution of App Ratings  
- Top 10 App Categories  
- Free vs Paid Apps (Pie Chart)  
- Price vs Rating  
- Reviews vs Rating (Scatter Plot)  
- Top Genres by Installs  
- Content Rating Distribution  
- App Update Trends (Line Chart)  
- Correlation Heatmap  

---

## 📸 Project Screenshot


<img width="1920" height="1080" alt="Screenshot 2025-10-22 172011" src="https://github.com/user-attachments/assets/44b27c53-8f35-421e-ae25-4887255f656e" />
<img width="1920" height="1080" alt="Screenshot 2025-10-22 172110" src="https://github.com/user-attachments/assets/10f3c599-c290-4d4e-b61d-f8c7834459eb" />
<img width="1920" height="1080" alt="Screenshot 2025-10-22 172100" src="https://github.com/user-attachments/assets/63eaf13f-80ad-4e99-9b8f-77d5c9245bbd" />



---

## 🧠 Machine Learning Model

**Model:** Random Forest Regressor  

**Features:**  
`Category, Reviews, Size_KB, Installs_Num, Price_Num, App_Age_years, Type, Content Rating, Primary_Genre`  

**Target:** `Rating`  

**Performance Metrics:**  

| Metric | Value |
|--------|-------|
| MAE    | ~0.18 |
| RMSE   | ~0.25 |
| R² Score | ~0.82 |

**Feature Importance:**  

1. Reviews  
2. Installs_Num  
3. Category  
4. Price_Num  
5. App_Age_years  

Model serialized using Joblib as `playstore_rf_model.joblib` for reuse in the Streamlit app.

---

## 💻 Streamlit Dashboard

**Features:**

- **Exploratory Dashboard:** KPI cards, charts for top categories, rating distribution, free vs paid apps  
- **Visual Insights:** Scatter plots, box plots for deeper analysis  
- **Prediction Module:** Users input app details to get instant rating predictions  

**UI Highlights:**

- Intuitive filters: Category, Type, Content Rating, Install Band  
- Interactive Plotly visualizations  
- Non-scrollable sidebar with personal links  

---

## 📈 Results & Insights

- Paid apps often have slightly higher ratings than free apps  
- Education, Health, and Productivity apps perform well in user ratings  
- Higher installs and reviews strongly correlate with higher ratings  
- Random Forest model provides reliable predictions  

---

## 🧩 Future Enhancements

- Integrate live data from Google Play API  
- Include NLP-based sentiment analysis from user reviews  
- Deploy the Streamlit app online via Streamlit Cloud or Render  
- Build a Power BI version for advanced reporting  

---

## 🧾 Conclusion

This project demonstrates the end-to-end Data Science workflow: from data cleaning and feature engineering to visualization, prediction, and interactive deployment. The insights help developers understand what drives higher app ratings and improve user satisfaction.

---

## 👨‍💻 Developer Information

**Amit Khotele**  
📧 Email: amitkhotele2@gmail.com  
💼 LinkedIn: [linkedin.com/in/amitkhotele](https://www.linkedin.com/in/amitkhotele)  
🐙 GitHub: [github.com/amitkhotele](https://github.com/amitkhotele)  
