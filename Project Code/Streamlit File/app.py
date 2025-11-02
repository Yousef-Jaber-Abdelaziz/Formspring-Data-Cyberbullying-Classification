import streamlit as st
import re, html, string, emoji, torch, joblib
from bs4 import BeautifulSoup
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# ---------------------------------------------------------
# 1. Preprocessing (must match your training pipeline!)
# ---------------------------------------------------------
def preprocess_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)
    text = html.unescape(text)
    text = re.sub(r"http\S+|www\S+", "", text)
    text = emoji.replace_emoji(text, "")
    text = re.sub(r"(A:|Q:)", "", text)
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"\d+", "", text)
    text = text.lower().strip()
    keep = {'.', ',', "'"}
    pattern = "[" + re.escape("".join(set(string.punctuation) - keep)) + "]"
    text = re.sub(pattern, " ", text)
    text = re.sub(r"\s{2,}", " ", text).strip()
    return text

# ---------------------------------------------------------
# 2. Load Model, Tokenizer, and Threshold
# ---------------------------------------------------------
@st.cache_resource
def load_model_bundle():
    bundle = joblib.load("bully_model_bundle.pkl")
    model_name = "distilbert-base-uncased"
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)
    model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=2)
    model.load_state_dict(bundle["model_state"])
    model.eval()
    threshold = bundle["threshold"]
    return model, tokenizer, threshold

model, tokenizer, threshold = load_model_bundle()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# ---------------------------------------------------------
# 3. Streamlit UI
# ---------------------------------------------------------
st.set_page_config(page_title="Cyberbullying Detector", layout="centered")

st.title("💬 Cyberbullying Detection App")
st.markdown("Type any text below to check if it may be **bullying or not**.")

user_input = st.text_area("Enter a comment:", height=150, placeholder="Type something like: 'You are so stupid and annoying!'")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            cleaned = preprocess_text(user_input)
            encoded = tokenizer(cleaned, return_tensors="pt", truncation=True, padding=True, max_length=128)
            encoded = {k: v.to(device) for k, v in encoded.items()}
            outputs = model(**encoded)
            prob = torch.softmax(outputs.logits, dim=1)[0, 1].item()
            label = int(prob >= threshold)

        st.markdown("---")
        st.subheader("🧠 Model Prediction")
        if label == 1:
            st.error(f"⚠️ **Bullying detected!** (Confidence: {prob:.2f})")
        else:
            st.success(f"✅ **Not Bullying** (Confidence: {1 - prob:.2f})")

        st.markdown(f"**Cleaned Text:** `{cleaned}`")

st.markdown("---")
st.caption("Model trained using DistilBERT with Focal Loss and early stopping. © 2025")
