import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

# Load and cache the dataset
@st.cache_data
def load_data():
    return pd.read_csv("C:/Users/Dell/Desktop/gen ai project/data/CAR DETAILS FROM CAR DEKHO.csv")

df = load_data()
st.title("🚗 Car Price Prediction Dashboard")

# Sidebar filters for exploring dataset
st.sidebar.header("🔍 Filter Options")
fuel_options = st.sidebar.multiselect("Select Fuel Type", df['fuel'].unique(), default=df['fuel'].unique())
dealer_options = st.sidebar.multiselect("select dealer type",df['seller_type'].unique(), default=df['seller_type'].unique())
transmission_option = st.sidebar.selectbox("Select Transmission", df['transmission'].unique())
year_range = st.sidebar.slider("Select Year Range", int(df['year'].min()), int(df['year'].max()), (2010, 2020))
price_range = st.sidebar.slider("select price range", int(df['selling_price'].min()), int(df['selling_price'].max()), (100000, 500000))

# Filter dataset
filtered_df = df[
    (df['fuel'].isin(fuel_options)) &
    (df['transmission'] == transmission_option) &
    (df['seller_type'].isin(dealer_options)) &
    (df['selling_price'] >= price_range[0]) &
    (df['selling_price'] <= price_range[1]) &
    (df['year'] >= year_range[0]) &
    (df['year'] <= year_range[1])
]

st.subheader("Filtered Dataset")
st.dataframe(filtered_df)

# Plot price distribution
st.subheader("Selling Price Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['selling_price'], kde=True, ax=ax)
st.pyplot(fig)

# Predict Selling Price Section
st.subheader("💡 Predict Car Selling Price")

input_data = {
    'year': st.number_input("Year", 2000, 2025, 2015),
    'km_driven': st.number_input("Kilometers Driven", 0, 500000, 30000),
    'fuel': st.selectbox("Fuel Type", df['fuel'].unique()),
    'seller_type': st.selectbox("Seller Type", df['seller_type'].unique()),
    'transmission': st.selectbox("Transmission", df['transmission'].unique()),
    'owner': st.selectbox("Ownership", df['owner'].unique())
}

if st.button("Predict Price"):
    model, encoders = load_model_and_encoders()
    price = predict_price(input_data, model, encoders)
    st.success(f"✅ Estimated Selling Price: ₹{price:,.2f}")
