# 🧠 Formspring Data Cyberbullying Classification

## 📘 Project Description  
The **Formspring Data Cyberbullying Classification** project aims to detect and classify instances of cyberbullying within online conversations. Using natural language processing (NLP) and deep learning techniques, the model identifies whether a given text contains bullying, aggression, or offensive content. This project helps promote safer digital communication environments by automatically flagging harmful messages.

---

## 🗂️ Project Agenda
#### 1️⃣ 📊 Dataset Description  
#### 2️⃣ 🏷️ Data Labeling  
#### 3️⃣ 🧹 Data Pre-processing  
#### 4️⃣ 🧠 Model Training  
#### 5️⃣ 📈 Results  
#### 6️⃣ 💻 Sample Outputs from Streamlit Deployment  


---
 
## 1️⃣ 📊 Dataset Description: Formspring Cyberbullying Detection (Reynolds et al., 2011)

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

#### 🧠 Annotation Process  
- A post is labeled as **bullying** if **at least one of the three annotators** agreed.
> 💡 **Tip:** If you’d like to explore the dataset before diving into the notebooks, click the button to view the raw data. [![View Dataset](https://img.shields.io/badge/View_Dataset-CSV-blue?style=for-the-badge&logo=github)](https://github.com/Yousef-Jaber-Abdelaziz/Formspring-Data-Cyberbullying-Classification/blob/6d8041e46163d643e09f2fe1ac7cf856d067ce6d/Datasets/0-Root%20Data/formspring.csv)


---



