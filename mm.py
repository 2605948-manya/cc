import streamlit as st

from ui_helpers import show_result, run_analysis, add_to_history

st.set_page_config(page_title="Headline Checker", layout="wide")
st.title("Headline Checker")

# ---- Replace this with your real analyzer ------------------------------
# from my_model import analyze_headline as analyze_fn
def analyze_fn(headline: str) -> dict:
    # Dummy result so you can confirm the UI works
    return {
        "headline": headline,
        "clickbait": {
            "probability": 0.62,
            "reasons": [
                {"label": "Curiosity-gap wording", "detail": "Phrases like 'you won't believe'."}
            ],
        },
        "credibility": {
            "probability": 0.45,
            "reasons": ["Sensational tone"],
        },
        "features": {"word_count": len(headline.split()), "has_number": any(c.isdigit() for c in headline)},
    }
# ------------------------------------------------------------------------

headline = st.text_input("Enter a headline", placeholder="Paste a news headline here")

if st.button("Analyze", type="primary"):
    result = run_analysis(analyze_fn, headline)
    if result is not None:
        st.session_state["last_result"] = result
        add_to_history(result)

# Show the last result (kept in session_state so it survives reruns,
# e.g. when the download button is clicked)
if "last_result" in st.session_state:
    show_result(st.session_state["last_result"])
    