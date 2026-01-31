# 🎬 AI-Based OTT Movie Recommendation System

An AI-powered movie recommendation system inspired by OTT platforms like Netflix and Amazon Prime. This project recommends similar movies to users based on content similarity using Machine Learning and provides an interactive web interface using Streamlit.

---

## 🚀 Project Overview

This application suggests movies based on **content-based filtering**. When a user selects a movie, the system analyzes movie features and recommends other similar movies using cosine similarity.

The goal of this project is to understand how real-world recommendation systems work and how Machine Learning models can be integrated into web applications.

---

## ✨ Key Features

* 🎥 Content-based movie recommendation system
* 🤖 Machine Learning similarity model
* 📊 Uses movie metadata for recommendations
* ⚡ Fast and accurate movie suggestions
* 🖥️ Interactive UI built with Streamlit
* 🧹 Clean GitHub project structure (no large ML files tracked)

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries & Tools:**

  * Pandas
  * NumPy
  * Scikit-learn
  * Streamlit
* **Version Control:** Git & GitHub

---

## 🧠 Machine Learning Approach

* Type: **Content-Based Filtering**
* Similarity Measure: **Cosine Similarity**
* Data Processing: Movie metadata is vectorized and compared to find similar movies

---

## 📂 Project Structure

```
AI-OTT-Web-App/
│
├── Project/
│   ├── app.py
│   ├── movie_dict.pkl   (ignored)
│   └── similarity.pkl   (ignored)
│
├── ResearchPaper/
├── .gitignore
├── README.md
└── requirements.txt
```

> ⚠️ Note: `.pkl` model files are ignored using `.gitignore` and are generated locally.

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/theankitcse/AI-OTT-Web-App.git
cd AI-OTT-Web-App
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run Project/app.py
```

---

## 📸 Application Preview

Once the app runs, you can:

* Select a movie from the dropdown
* Get a list of recommended similar movies instantly

---

## 📘 What I Learned

* How recommendation systems work in real-world applications
* How to implement content-based filtering
* How to calculate similarity using Machine Learning
* How to build and deploy interactive apps using Streamlit
* How to manage ML projects professionally with Git & GitHub
* Best practices for handling large ML files

---

## 🔮 Future Improvements

* Add collaborative filtering
* Deploy the app on cloud (Streamlit Cloud / Hugging Face)
* Improve UI and performance
* Add user authentication

---

## 🔗 GitHub Repository

👉 [https://github.com/theankitcse/AI-OTT-Web-App](https://github.com/theankitcse/AI-OTT-Web-App)

---

## 🙌 Acknowledgements

Inspired by real-world OTT recommendation systems and Machine Learning use cases.

---

## 👤 Author

**Ankit Kumar**
Aspiring Data Analyst & Machine Learning Enthusiast

---

⭐ If you like this project, don’t forget to star the repository!
