import streamlit as st
import pickle
import pandas as pd
import pandas as pd
import streamlit as st
import pandas as pd
data = pd.read_csv("dataset/pricing_data.csv")
st.subheader("Demand vs Price Analysis")
st.scatter_chart(data[['demand','price']])
data = pd.read_csv("dataset/pricing_data.csv")
st.subheader("Demand Trend")
st.line_chart(data[['demand']])
data = pd.read_csv("dataset/pricing_data.csv")
st.subheader("Demand vs Price Analysis")
st.scatter_chart(data[['demand','price']])
st.title("Dynamic Pricing System")
st.write("Enter product details to get recommended price")

# load trained model
model = pickle.load(open("model/pricing_model.pkl","rb"))

# price optimizer
def optimize_price(predicted_demand, base_price):

    if predicted_demand > 250:
        return base_price * 1.15

    elif predicted_demand > 200:
        return base_price * 1.05

    else:
        return base_price * 0.95


st.title("Dynamic Pricing System")

# user inputs
demand = st.slider("Demand",0,500)
competitor_price = st.number_input("Competitor Price")
stock = st.slider("Stock",0,200)
rating = st.slider("Rating",0.0,5.0)
season = st.selectbox("Season",[0,1])
discount = st.slider("Discount %",0,50)

# button
if st.button("Predict Price"):

    prediction = model.predict([[demand,competitor_price,stock,rating,season,discount]])

    optimized_price = optimize_price(demand, prediction[0])

    st.success(f"Recommended Price: ₹{optimized_price:.2f}")