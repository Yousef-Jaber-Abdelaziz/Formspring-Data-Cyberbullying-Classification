# 🧠 Formspring Data Cyberbullying Classification

## 📘 Project Description  
The **Formspring Data Cyberbullying Classification** project aims to detect and classify instances of cyberbullying within online conversations. Using natural language processing (NLP) and deep learning techniques, the model identifies whether a given text contains bullying, aggression, or offensive content. This project helps promote safer digital communication environments by automatically flagging harmful messages.

---

## 📋 Project Agenda  

## 🗂️ Project Agenda

1. #### 📊 Dataset Description  
   Introduces the Formspring dataset used for cyberbullying detection, detailing its structure, source, and distribution of labeled samples.

2. #### 🏷️ Data Labeling  
   Explains how posts were annotated by multiple human reviewers, ensuring accurate classification of bullying versus non-bullying content.

3. #### 🧹 Data Pre-processing  
   Covers text cleaning, normalization, tokenization, and preparation steps to enhance model performance and data quality.

4. #### 🧠 Model Training  
   Describes the training process using classical ML models (Logistic Regression, SVM, Naïve Bayes) and the fine-tuned DistilBERT transformer for NLP.

5. #### 📈 Results  
   Summarizes model evaluation metrics, highlighting DistilBERT’s superior performance in detecting cyberbullying text accurately.

6. #### 💻 Sample Outputs from Streamlit Deployment  
   Demonstrates real-time text classification using a Streamlit app for interactive cyberbullying detection.


---
 
## 📊 Dataset Description: Formspring Cyberbullying Detection (Reynolds et al., 2011)

#### 🧾 Overview  
The **Formspring Cyberbullying Detection Dataset** is a benchmark dataset designed for research on online harassment and abusive language detection. It was collected from the now-defunct **Formspring.me** Q&A social platform during the **summer of 2010**.  
The dataset includes **12,772 anonymous question-answer pairs**, each annotated by **three independent workers on Amazon Mechanical Turk** to determine whether the post contains cyberbullying content.

| Statistic | Value |
|------------|--------|
| **Total Samples** | 12,772 |
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

---

#### 🧠 Annotation Process  
- A post is labeled as **bullying** if **at least one of the three annotators** agreed.  

