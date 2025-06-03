#!/bin/bash

# Create Streamlit config directory
mkdir -p ~/.car-price-prediction/

# Create Streamlit credentials file
echo "\
[general]\n\
email = \"ajdeutschland103@hotmail.com\"\n\
" > ~/.car-price-prediction/credentials.toml

# Create Streamlit server config file
echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
" > ~/.car-price-prediction/config.toml

# Setup virtual environment and install requirements
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
