# 🧠 Formspring Data Cyberbullying Classification

## 📘 Project Description  
The **Formspring Data Cyberbullying Classification** project aims to detect and classify instances of cyberbullying within online conversations. Using natural language processing (NLP) and deep learning techniques, the model identifies whether a given text contains bullying, aggression, or offensive content. This project helps promote safer digital communication environments by automatically flagging harmful messages.

---

## 📋 Project Agenda  

#### 📊 Dataset Description  
The dataset used in this project is derived from **Formspring.me**, a social networking platform where users exchanged public Q&A messages. The dataset contains thousands of text samples labeled to represent bullying or non-bullying behavior.

#### 🏷️ Data Labeling  
Each text entry in the dataset was labeled manually by 3 different experts to ensure accurate categorization of bullying intensity and type. The labeling helps train the model to distinguish between harmless teasing and serious harassment.

#### 🧹 Data Pre-processing  
The preprocessing pipeline includes text cleaning, tokenization, stopword removal, and lemmatization. Additionally, the text was vectorized using **TF-IDF** to convert raw sentences into numerical representations suitable for model training.

#### 🧠 Model Training  
A **BERT-based model** was fine-tuned on the labeled dataset to achieve high accuracy in text classification. The model learns contextual word relationships to understand the subtle tone of messages, distinguishing between neutral and aggressive expressions effectively.

#### 📈 Results  
The model achieved strong accuracy and F1-score on the validation dataset, demonstrating robust performance in detecting cyberbullying content. Evaluation metrics confirm that the system generalizes well on unseen data.

### 💻 Sample Outputs from Streamlit Deployment  
The model was deployed using **Streamlit**, providing an easy-to-use interface where users can input text messages and instantly see whether they are classified as *cyberbullying* or *non-cyberbullying*.

---
 
