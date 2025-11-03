# 🧠 Formspring Data Cyberbullying Classification

## 📘 Project Description  
The **Formspring Data Cyberbullying Classification** project aims to detect and classify instances of cyberbullying within online conversations. Using natural language processing (NLP) and deep learning techniques, the model identifies whether a given text contains bullying, aggression, or offensive content. This project helps promote safer digital communication environments by automatically flagging harmful messages.

---

## 🗂️ Project Agenda
#### 1️⃣ 📊 Dataset Description  
#### 2️⃣ 🏷️ Data Labeling  
#### 3️⃣ 🧹 Data Pre-processing  
#### 4️⃣ 🧠 Model Training  
#### 5️⃣ 💻 Sample Outputs from Streamlit Deployment  


---

 
## 1️⃣ 📊 Dataset Description: Formspring Cyberbullying Detection (Reynolds et al., 2011)

#### 🧾 Overview  
The **Formspring Cyberbullying Detection Dataset** is a benchmark dataset designed for research on online harassment and abusive language detection. It was collected from the now-defunct **Formspring.me** Q&A social platform during the **summer of 2010**.  
The dataset includes **12,772 anonymous question-answer pairs**, each annotated by **three independent workers on Amazon Mechanical Turk** to determine whether the post contains cyberbullying content.

| Statistic | Value |
|------------|--------|
| **Total Samples** | 12,901 |
| **Total Tokens** | ~300,000 |
| **Average Words per Post** | 23 (bullying) / 25 (non-bullying) |

> ⚠️ **Note:** The dataset is highly imbalanced, with over **80% non-bullying samples**, reflecting the natural distribution of online conversations.

#### 📂 Data Fields  
| Field | Description |
|--------|-------------|
| `Userid` | Identifier of the respondent |
| `Asker` | Identifier of the question asker |
| `Post` | Combined text of question and answer (markers removed during preprocessing) |
| `Ans#` | Annotator binary response (*Yes/No*) for bullying – three responses per post |
| `severity#` | Bullying intensity score ranging from **0–10** |
| `bully#` | Words or phrases flagged as bullying indicators |

#### 🧠 Annotation Process  
- A post is labeled as **bullying** if **at least one of the three annotators** agreed.
> 💡 **Tip:** If you’d like to explore the dataset before diving into the notebooks, click the button to view the raw data. [![View Dataset](https://img.shields.io/badge/View_Dataset-CSV-blue?style=for-the-badge&logo=github)](https://github.com/Yousef-Jaber-Abdelaziz/Formspring-Data-Cyberbullying-Classification/blob/6d8041e46163d643e09f2fe1ac7cf856d067ce6d/Datasets/0-Root%20Data/formspring.csv)


---

## 2️⃣ 🏷️ Data Labeling  

Each post in the dataset was annotated by three independent human evaluators, providing binary responses (*Yes/No*) and a **severity score** ranging from 0 to 10.  

To ensure a clear distinction between bullying and non-bullying content, the following custom labeling rule was applied:

```text
IF any annotator assigned a severity > 0:
    → Label = 1 (Cyberbullying)
ELSE:
    → Label = 0 (Non-bullying)
```
> 🧮 **Labeling Summary:**  
> This logic resulted in **1,915 samples** being annotated as **cyberbullying** based on the applied severity rule.  

> 🧭 **Quick Navigation:**  
> Navigate the notebook [![Jupyter](https://img.shields.io/badge/-Notebook-FFA500?style=flat-square&logo=jupyter&logoColor=white)](https://github.com/Yousef-Jaber-Abdelaziz/Formspring-Data-Cyberbullying-Classification/blob/44fca2ce81215e597b8495defec4c2903643bd45/Project%20Code/Notebooks/0_Cyber-bullying-Class-Split.ipynb)  
> View the splitted data samples [![Dataset](https://img.shields.io/badge/-Datasets-4CAF50?style=flat-square&logo=files&logoColor=white)](https://github.com/Yousef-Jaber-Abdelaziz/Formspring-Data-Cyberbullying-Classification/tree/bcebbe1dbb37099a674dc9a3e59d648a32ff2f0b/Datasets/1-Data%20Class%20Splitting)


---


## 3️⃣ 🧹 Data Pre-processing  

All preprocessing steps were implemented in the notebook **`1_Cyber-bullying-Preprocessing.ipynb`** to ensure clean, standardized text input for model training.  

| Step | Description |
|------|-------------|
| **1. Data Loading & Merging** | Imported `bully_data.csv` (label=1) and `not_bully_data.csv` (label=0), then combined and shuffled the data for balanced sampling. |
| **2. HTML, URL & Symbol Cleaning** | Applied `BeautifulSoup` and regular expressions to strip HTML tags, remove URLs, and retain only alphabetic characters and spaces. |
| **3. Slang & Contraction Expansion** | Replaced slang terms (e.g., `"lol"`) and contractions (e.g., `"don’t"`) using custom JSON dictionaries: `slangs.json` and `contractions.json`. |
| **4. Grammar & Spelling Correction (LLM-based)** | Used **Microsoft Phi-2** model for contextual text correction via the prompt: <br> `"Correct grammar and spelling: {text}"` <br> Truncated long inputs (>500 chars) and extracted corrected text. |
| **5. Punctuation Removal** | Removed punctuation marks using `str.maketrans` to ensure uniform tokenization. |
| **6. Named Entity Replacement** | Leveraged **spaCy** to anonymize named entities, e.g., `"John in New York"` → `"person in location"`. |
| **7. Tokenization, Lemmatization & Stopword Removal** | Used **NLTK** to tokenize, POS-tag, and lemmatize text; removed standard English stopwords while preserving critical bullying terms such as `ass`, `bitch`, `fuck`, etc. |
| **8. Final Cleaning** | Dropped empty or NaN entries and removed duplicate posts to ensure data consistency. |
| **9. Export Processed Data** | Saved the final cleaned dataset as `all_data_processed.csv` containing: <br>• `post`: tokenized text <br>• `label`: 0 (non-bully) / 1 (bully). |

📓 You can explore the preprocessing notebook here: [![Jupyter](https://img.shields.io/badge/-Notebook-FFA500?style=flat-square&logo=jupyter&logoColor=white)](https://github.com/Yousef-Jaber-Abdelaziz/Formspring-Data-Cyberbullying-Classification/blob/067e3ef191213c72fb8bba25d7d17db351839801/Project%20Code/Notebooks/1-cyber-bullying-preprocessing.ipynb)  
📂 View the processed dataset: [![Dataset](https://img.shields.io/badge/-Processed_Data-4CAF50?style=flat-square&logo=files&logoColor=white)](https://github.com/Yousef-Jaber-Abdelaziz/Formspring-Data-Cyberbullying-Classification/tree/412fdde768039cf7954eed59e21c2ed1dcde04d3/Datasets/2-PreProcessed%20Data)


---

## 4️⃣ 🧠 Model Training  

The model development and training process was implemented in **`3-Cyber-bullying-Detection-Deployment.ipynb`**, focusing on robust text feature extraction, imbalance handling, and fine-tuning of the **DistilBERT** transformer model.

| Step | Description |
|------|-------------|
| **1. Feature Extraction** | Leveraged the **DistilBERT tokenizer** from Hugging Face Transformers to convert cleaned text into contextual embeddings using the `distilbert-base-uncased` pre-trained model. Each text was truncated/padded to a fixed maximum sequence length for batch processing. |
| **2. Dataset Splitting** | Divided data into **training (80%)**, **validation (10%)**, and **test (10%)** sets using stratified sampling to preserve class balance. |
| **3. Handling Class Imbalance** | Used **class weighting** inside the loss function to penalize the majority (non-bullying) class more lightly. This ensured fair learning for minority samples (bullying). |
| **4. Model Architecture** | Added a fully connected **dense classification head** on top of the frozen DistilBERT encoder to output a single probability for binary classification (bully / non-bully). |
| **5. Loss Function** | Adopted **Weighted Binary Cross-Entropy Loss (BCEWithLogitsLoss)** — crucial for learning from highly imbalanced data and providing stable gradient updates. |
| **6. Optimization** | Used the **AdamW optimizer** with linear learning rate decay and early stopping based on validation loss. |
| **7. Early Stopping & Best Model Selection** | Training stopped automatically when validation loss stopped improving for one epoch. The best model weights were restored for evaluation. |


#### 🧩 Training Summary

| Metric | Value |
|--------|-------|
| **Model** | DistilBERT (`distilbert-base-uncased`) |
| **Epochs** | 3/10 (early stopped) |
| **Best Validation Loss** | 0.1413 |
| **Optimizer** | AdamW |
| **Loss Function** | Weighted Binary Cross-Entropy (BCEWithLogitsLoss) |
| **Class Imbalance Handling** | Class Weights |
| **Feature Extraction** | DistilBERT contextual embeddings |

---

#### 📈 Validation Results (Optimized Threshold = 0.45)

| Class | Precision | Recall | F1-Score | Support |
|-------|------------|---------|-----------|----------|
| **0 (Non-bullying)** | 0.733 | 0.709 | 0.721 | 151 |
| **1 (Bullying)** | 0.718 | 0.742 | 0.730 | 151 |

**Overall Accuracy:** 0.725  
**Macro Avg F1:** 0.725  

> ✅ The model achieved a **balanced F1-score of 0.73** on the bullying class — demonstrating effective handling of imbalance and high contextual understanding of text.

---

📓 Explore the model training and deployment notebook:  [![Jupyter](https://img.shields.io/badge/-Notebook-FFA500?style=flat-square&logo=jupyter&logoColor=white)](https://github.com/Yousef-Jaber-Abdelaziz/Formspring-Data-Cyberbullying-Classification/blob/1537616a75b9e4aeb5ebfdef687b9c3a0b5d15cb/Project%20Code/Notebooks/2-Cyber-bullying-Detection-Deployment.ipynb)

---
## 5️⃣ 💻 Sample Outputs from Streamlit Deployment  

The cyberbullying detection system was **deployed manually using Streamlit**, providing an interactive web interface for real-time text classification.  
Users can enter or paste any social media message, and the app instantly predicts whether the text is **“Bullying”** or **“Non-Bullying”** using the fine-tuned **DistilBERT model**.  

The Streamlit app loads the trained model, tokenizes the input text, and displays both the **predicted label** and **confidence score** dynamically.  
This deployment demonstrates the real-world usability of the model for monitoring online interactions and moderating user-generated content.


### 🎥 Demo Samples  

<div align="center">

<img src="Deployment Samples/ezgif-54e215e6c03a33.gif" width="400" style="margin-right: 20px;"/>
<img src="Deployment Samples/ezgif-5f9a84e8b4b048.gif" width="400"/>

</div>
