import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("FEMSA Dashboard")

# Upload the Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)

    # Display the dataframe
    st.write(df)

    # Select columns for the x and y axes
    x_axis = st.selectbox("Select the column for the x-axis", df.columns)
    y_axis = st.selectbox("Select the column for the y-axis", df.columns)

    # Generate the plot
    fig, ax = plt.subplots()
    ax.plot(df[x_axis], df[y_axis])
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(f"{y_axis} vs {x_axis}")

    # Display the plot
    st.pyplot(fig)
