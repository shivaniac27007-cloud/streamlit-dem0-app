import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt  
#st.write("hello world")
#st.write({"key":["value"]})#json dict format

st.title("Simple Data Dashboard")#title

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")#upload a file

if uploaded_file is not None:
    #using pandas df
    df=pd.read_csv(uploaded_file) 

    st.subheader("Data preview")#header
    st.write(df.head())#show first 5 values

    st.subheader("Data Summary")#header2
    st.write(df.describe())#summary-avg,value,count of 5 values
    #summary is modifiable

    st.subheader("Filter Data")#header 3
    #widgets to be passed so the user can interact
    columns=df.columns.tolist()#give the list of columns
    selected_column=st.selectbox("Select column to filter by",columns)#column to choose
    unique_values=df[selected_column].unique()#all unique values from the selected column
    selected_value=st.selectbox("Select value",unique_values)#rows to choose

    #to show the filtered data to be plotted
    st.header("Filtered Data to be plotted")#header 4
    filtered_df=df[df[selected_column]==selected_value]#take all rows where df at slected column is equal to selected value
    st.write(filtered_df)

    #plotting
    st.subheader("Plot Data")#header 5
    x_column=st.selectbox("Select x-axis value",columns)
    y_column=st.selectbox("Select y-axis value",columns)

    if st.button("Generate Plot"):
    # Create a matplotlib figure and axis
        fig, ax = plt.subplots()

        # Plot the selected X and Y columns
        ax.plot(filtered_df[x_column], filtered_df[y_column])

        # Add labels and title
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.subheader("Filtered Data Plot")#header 6

        # Rotate x-axis labels (useful if dates are on X-axis)
        plt.xticks(rotation=45)

        # Display the matplotlib plot in Streamlit
        st.pyplot(fig)
    else:
        st.info("Select axes and click 'Generate Plot'")
    
    st.subheader("Basic Analysis")#header 7

    if st.button("Show Analysis"):
        if not filtered_df.empty and filtered_df[y_column].dtype != "object":
            st.write("### Summary Statistics")

            st.write(f"**Total Records:** {len(filtered_df)}")
            st.write(f"**Minimum {y_column}:** {filtered_df[y_column].min()}")#min of column
            st.write(f"**Maximum {y_column}:** {filtered_df[y_column].max()}")#max of column
            st.write(f"**Average {y_column}:** {filtered_df[y_column].mean():.2f}")#avg upto 2 decimal places

            st.info(
                f"The average {y_column} for '{selected_value}' "
                f"is {filtered_df[y_column].mean():.2f}, "
                f"with values ranging from "
                f"{filtered_df[y_column].min()} to {filtered_df[y_column].max()}."
            )
        else:
            st.warning("Please select a numeric column and ensure data is available")
        
#Use Python with pandas
#Build a Streamlit UI
#Load CSV file
#Perform basic data exploration
#Add interactive filtering
#Generate a plot on user action