import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

@st.cache_data
def load_data(path='datasets/car_dataset.csv'):
    df = pd.read_csv(path)
    return df.dropna().reset_index(drop=True)

def app():
    st.header("📊 Correlation Map (Interactive)")
    df = load_data()

    st.markdown("🔮 **Explore the magical connections between numerical features using an interactive map.**")

    # Select only numerical columns
    num_cols = df.select_dtypes(include='number').columns.tolist()

    # Multiselect for dynamic filtering
    selected_cols = st.multiselect(
        "🎯 Select numerical features to include:",
        num_cols,
        default=num_cols
    )

    if len(selected_cols) < 2:
        st.warning("Please select at least two numerical columns.")
        return

    # Compute correlation matrix
    corr = df[selected_cols].corr().round(2)

    # Create a Plotly heatmap
    fig = go.Figure(
        data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.index,
            colorscale="RdBu",
            zmin=-1, zmax=1,
            hoverongaps=False,
            colorbar=dict(title="Correlation"),
            text=corr.values,
            hovertemplate='Corr(%{x}, %{y}) = %{z}<extra></extra>'
        )
    )

    fig.update_layout(
        title="🔗 Correlation Heatmap",
        xaxis_title="Features",
        yaxis_title="Features",
        width=None,  # Responsive width
        height=600,
        margin=dict(l=40, r=40, t=50, b=40),
    )

    st.plotly_chart(fig, use_container_width=True)

    # Optional: Show strongest relationships
    st.markdown("### 💡 Top Feature Pairs by Absolute Correlation")

    corr_pairs = corr.abs().unstack().reset_index()
    corr_pairs.columns = ['Feature 1', 'Feature 2', 'Correlation']
    corr_pairs = corr_pairs[corr_pairs['Feature 1'] != corr_pairs['Feature 2']]
    corr_pairs = corr_pairs.sort_values(by='Correlation', ascending=False).drop_duplicates()

    strong_corr = corr_pairs[corr_pairs['Correlation'] >= 0.5]
    st.dataframe(strong_corr.reset_index(drop=True), use_container_width=True)
