import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# -------------------- Config --------------------
st.set_page_config(page_title="Car Price Predictor", layout="wide")
st.title('🚗 Car Price Prediction App')
st.markdown('Welcome! This app predicts the **selling price** of a car based on its features.')

# -------------------- Load Dataset --------------------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df.dropna().reset_index(drop=True)

DATA_PATH = 'datasets/car_dataset.csv'
df = load_data(DATA_PATH)
st.success(f'✅ Dataset Loaded & Cleaned: {df.shape[0]} rows, {df.shape[1]} columns')

# Preview
with st.expander("🔍 Preview Original Dataset"):
    st.dataframe(df.head().style.background_gradient(cmap='BuGn'), use_container_width=True)

# -------------------- Split Features/Target --------------------
X = df.drop(columns=['selling_price'])
y = df['selling_price']

categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numerical_cols = X.select_dtypes(exclude=['object']).columns.tolist()

# -------------------- Build Preprocessor --------------------
@st.cache_resource
def get_pipeline():
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ], remainder='passthrough')

    model = Pipeline([
        ('preprocess', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))
    ])
    return model

model = get_pipeline()

# -------------------- Training Section --------------------
st.divider()
st.markdown("## 🧠 Train Model")

if 'model_trained' not in st.session_state:
    st.session_state.model_trained = False

if st.button("🚀 Train Model"):
    with st.spinner("Training the model..."):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        st.session_state.model_trained = True
        st.session_state.X_test = X_test
        st.session_state.y_test = y_test
        st.session_state.y_pred = y_pred
        st.session_state.model = model

    st.success(f"✅ Model Trained | R² Score: {r2:.2f}, MAE: {mae:,.0f}, RMSE: {rmse:,.0f}")

    # -------------------- Plots --------------------
    st.markdown("### 📊 Training Insights")

    col1, col2 = st.columns(2)

    with col1:
        # Feature Importance
        importances = model.named_steps['regressor'].feature_importances_
        ohe_features = model.named_steps['preprocess'].transformers_[0][1].get_feature_names_out(categorical_cols)
        all_features = list(ohe_features) + numerical_cols
        importance_df = pd.DataFrame({'feature': all_features, 'importance': importances})
        importance_df = importance_df.sort_values(by='importance', ascending=False).head(10)

        fig1 = px.bar(
            importance_df[::-1],  # reverse for horizontal
            x='importance', y='feature',
            orientation='h',
            title="Top 10 Feature Importances",
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        # Actual vs Predicted
        fig2 = px.scatter(
            x=st.session_state.y_test,
            y=st.session_state.y_pred,
            labels={'x': 'Actual Price', 'y': 'Predicted Price'},
            title="Actual vs Predicted Prices",
            height=400
        )
        fig2.update_traces(marker=dict(size=5))
        st.plotly_chart(fig2, use_container_width=True)

    # Residuals Plot
    residuals = st.session_state.y_test - st.session_state.y_pred
    fig3 = px.histogram(
        residuals, nbins=30, marginal="rug", 
        title="Residuals Distribution",
        height=400
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Target Distribution
    fig4 = px.histogram(
        y, nbins=40, title="Selling Price Distribution",
        height=400, color_discrete_sequence=['skyblue']
    )
    st.plotly_chart(fig4, use_container_width=True)

# -------------------- Prediction Section --------------------
st.divider()
st.markdown("## 🎯 Predict Car Price")

if not st.session_state.model_trained:
    st.warning("⚠️ Please train the model first by clicking 'Train Model'")
else:
    input_data = {}

    st.subheader("🧾 Categorical Features")
    cols = st.columns(len(categorical_cols))
    for i, col in enumerate(categorical_cols):
        options = sorted(df[col].unique())
        input_data[col] = cols[i].selectbox(f'{col}', options)

    st.subheader("🔢 Numerical Features")
    cols = st.columns(len(numerical_cols))
    for i, col in enumerate(numerical_cols):
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        mean_val = float(df[col].mean())
        input_data[col] = cols[i].number_input(
            f'{col}',
            min_value=min_val,
            max_value=max_val,
            value=mean_val,
            step=1.0
        )

    if st.button("🔮 Predict Price"):
        input_df = pd.DataFrame([input_data])
        predicted_price = st.session_state.model.predict(input_df)[0]
        st.success(f"💰 **Predicted Selling Price: $ {predicted_price:,.0f}**")
