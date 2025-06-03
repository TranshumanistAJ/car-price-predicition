import streamlit as st  # Importing Streamlit for web app interface
import pandas as pd  # Importing pandas for data handling
import plotly.express as px  # Importing Plotly Express for quick plotting
import plotly.graph_objects as go  # Importing Graph Objects for detailed Plotly customization

@st.cache_data  # Cache the loaded data for performance
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)  # Read CSV from the given path
    return df.dropna().reset_index(drop=True)  # Drop missing values and reset index

def app():
    st.header("📊 Correlation Map (Interactive)")  # Set app header
    df = load_data()  # Load the dataset

    st.markdown("🔮 **Explore the magical connections between numerical features using an interactive map.**")  # Intro text

    # Select only numerical columns
    num_cols = df.select_dtypes(include='number').columns.tolist()  # Get list of numeric columns

    # Multiselect for dynamic filtering
    selected_cols = st.multiselect(  # Allow user to select multiple numeric features
        "🎯 Select numerical features to include:",
        num_cols,
        default=num_cols  # Default to all numeric columns
    )

    if len(selected_cols) < 2:  # Warn if less than 2 columns are selected
        st.warning("Please select at least two numerical columns.")
        return  # Exit the function

    # Compute correlation matrix
    corr = df[selected_cols].corr().round(2)  # Compute correlation and round to 2 decimals

    # Create a Plotly heatmap
    fig = go.Figure(  # Start figure
        data=go.Heatmap(  # Use Heatmap trace
            z=corr.values,  # Matrix of correlation values
            x=corr.columns,  # Column names for x-axis
            y=corr.index,  # Column names for y-axis
            colorscale="RdBu",  # Color scale from red to blue
            zmin=-1, zmax=1,  # Fix color range
            hoverongaps=False,  # Disable hover on gaps
            colorbar=dict(title="Correlation"),  # Add color bar title
            text=corr.values,  # Show values on hover
            hovertemplate='Corr(%{x}, %{y}) = %{z}<extra></extra>'  # Custom hover format
        )
    )

    fig.update_layout(  # Update layout of the heatmap
        title="🔗 Correlation Heatmap",  # Title of the chart
        xaxis_title="Features",  # X-axis title
        yaxis_title="Features",  # Y-axis title
        width=None,  # Auto width for responsiveness
        height=600,  # Fixed height
        margin=dict(l=40, r=40, t=50, b=40),  # Margins around plot
    )

    st.plotly_chart(fig, use_container_width=True)  # Display the plot in Streamlit

    # Optional: Show strongest relationships
    st.markdown("### 💡 Top Feature Pairs by Absolute Correlation")  # Section header

    corr_pairs = corr.abs().unstack().reset_index()  # Flatten correlation matrix to pairwise format
    corr_pairs.columns = ['Feature 1', 'Feature 2', 'Correlation']  # Rename columns
    corr_pairs = corr_pairs[corr_pairs['Feature 1'] != corr_pairs['Feature 2']]  # Exclude self-correlation
    corr_pairs = corr_pairs.sort_values(by='Correlation', ascending=False).drop_duplicates()  # Sort and drop duplicates

    strong_corr = corr_pairs[corr_pairs['Correlation'] >= 0.5]  # Filter for strong correlations
    st.dataframe(strong_corr.reset_index(drop=True), use_container_width=True)  # Show results in a table
