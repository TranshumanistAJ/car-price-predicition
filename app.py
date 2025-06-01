import streamlit as st

from multipage import MultiPage
from app_pages import summary, correlation, hypothesis, prediction

# 🔮 Invoke the enchanted MultiPage spellbook
app = MultiPage("🔮 Car Price Prediction Oracle")

# 🗂️ Add realms (pages) to the spellbook
app.add_page("📜 Summary Scroll", summary.app)
app.add_page("📊 Correlation Map", correlation.app)
app.add_page("🧪 Hypothesis Forge", hypothesis.app)
app.add_page("🎯 Prediction Portal", prediction.app)

# 🚪 Step into the first page
app.run()
