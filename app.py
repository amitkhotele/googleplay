import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from sklearn.preprocessing import LabelEncoder
import numpy as np

st.set_page_config(page_title="Google Play Store Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("googleplaystore_cleaned.csv")
    return df

@st.cache_resource
def load_model():
    return joblib.load("playstore_rf_model.joblib")

df = load_data()
model = load_model()

st.title("📱 Google Play Store Apps Analysis & Rating Prediction")
st.markdown("##### Built by **Amit Khotele** — Explore app trends and predict ratings using Machine Learning")

with st.sidebar:
    st.header("🔍 Filters")
    category = st.selectbox("Select Category", ["All"] + sorted(df["Category"].dropna().unique().tolist()))
    app_type = st.selectbox("Select Type", ["All"] + sorted(df["Type"].dropna().unique().tolist()))
    content_rating = st.selectbox("Select Content Rating", ["All"] + sorted(df["Content Rating"].dropna().unique().tolist()))
    install_band = st.selectbox("Select Install Band", ["All"] + sorted(df["Install_Band"].dropna().unique().tolist()))
    st.markdown("---")
    st.markdown("""<div style='text-align:center; font-size:13px;'>
    👨‍💻 <b>Analyzed by <span style="color:orange">Amit Khotele</span></b><br>
    <a href="mailto:amitkhotele2@gmail.com" target="_blank">📧 Email</a> |
    <a href="https://www.linkedin.com/in/amitkhotele" target="_blank">💼 LinkedIn</a> |
    <a href="https://github.com/amitkhotele" target="_blank">🐙 GitHub</a>
    </div>""", unsafe_allow_html=True)

filtered = df.copy()
if category != "All":
    filtered = filtered[filtered["Category"] == category]
if app_type != "All":
    filtered = filtered[filtered["Type"] == app_type]
if content_rating != "All":
    filtered = filtered[filtered["Content Rating"] == content_rating]
if install_band != "All":
    filtered = filtered[filtered["Install_Band"] == install_band]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Apps", len(filtered))
c2.metric("Average Rating", round(filtered["Rating"].mean(), 2))
c3.metric("Total Reviews", f"{int(filtered['Reviews'].sum()):,}")
c4.metric("Paid Apps (%)", f"{(filtered['Type'].value_counts(normalize=True).get('Paid', 0)*100):.1f}%")

tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Visual Insights", "🔮 Predict Rating"])

with tab1:
    fig1 = px.histogram(filtered, x="Rating", nbins=30, title="Distribution of Ratings", color_discrete_sequence=["#1f77b4"])
    st.plotly_chart(fig1, use_container_width=True)

    top_cat = filtered["Category"].value_counts().head(10)
    fig2 = px.bar(x=top_cat.index, y=top_cat.values, title="Top 10 Categories", color=top_cat.values, color_continuous_scale="blues")
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.pie(filtered, names="Type", title="Free vs Paid Apps", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    fig4 = px.scatter(filtered, x="Reviews", y="Rating", color="Category", size="Installs_Num",
                      title="Reviews vs Rating by Category", hover_name="App")
    st.plotly_chart(fig4, use_container_width=True)

    fig5 = px.box(filtered, x="Price_Category", y="Rating", title="Price Category vs Rating", color="Price_Category")
    st.plotly_chart(fig5, use_container_width=True)

    content_df = filtered["Content Rating"].value_counts().reset_index()
content_df.columns = ["Content Rating", "Count"]

fig6 = px.bar(content_df, 
              x="Content Rating", 
              y="Count", 
              title="Content Rating Distribution", 
              color="Count",
              color_continuous_scale="viridis")

st.plotly_chart(fig6, use_container_width=True)


with tab3:
    st.subheader("🎯 Enter App Details for Rating Prediction")
    col1, col2 = st.columns(2)
    category_in = col1.selectbox("App Category", sorted(df["Category"].dropna().unique()))
    type_in = col2.selectbox("App Type", sorted(df["Type"].dropna().unique()))
    content_in = col1.selectbox("Content Rating", sorted(df["Content Rating"].dropna().unique()))
    genre_in = col2.selectbox("Primary Genre", sorted(df["Primary_Genre"].dropna().unique()))
    reviews_in = col1.number_input("Reviews", min_value=0, step=1000)
    size_in = col2.number_input("Size (KB)", min_value=0.0, step=500.0)
    installs_in = col1.number_input("Installs", min_value=0, step=10000)
    price_in = col2.number_input("Price ($)", min_value=0.0, step=0.1)
    age_in = col1.number_input("App Age (years)", min_value=0.0, step=0.1)

    if st.button("🚀 Predict Rating"):
        le = LabelEncoder()
        inputs = pd.DataFrame({
            "Category": [category_in],
            "Reviews": [reviews_in],
            "Size_KB": [size_in],
            "Installs_Num": [installs_in],
            "Price_Num": [price_in],
            "App_Age_years": [age_in],
            "Type": [type_in],
            "Content Rating": [content_in],
            "Primary_Genre": [genre_in]
        })

        for col in ["Category", "Type", "Content Rating", "Primary_Genre"]:
            inputs[col] = le.fit(df[col].astype(str)).transform(inputs[col].astype(str))

        pred = model.predict(inputs)[0]
        st.success(f"⭐ Predicted App Rating: **{pred:.2f} / 5**")
