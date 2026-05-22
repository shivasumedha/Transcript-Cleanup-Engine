# 📝 AI Transcript Cleanup Engine

## 📌 Project Overview

AI Transcript Cleanup Engine is a Streamlit-based NLP mini project designed to clean noisy transcript text generated from speech-to-text systems.

The application automatically removes:
- filler words
- duplicate words
- extra spaces
- punctuation issues

The project also supports:
- transcript file upload
- cleaned transcript download
- light-themed professional UI

---

## 🚀 Features

✅ Filler word removal  
✅ Duplicate word removal  
✅ Extra space cleanup  
✅ Punctuation correction  
✅ File upload support  
✅ Download cleaned transcript  
✅ Professional light-themed UI  

---

## 🛠 Technologies Used

- Python
- Streamlit
- Regex (`re`)

---

## 📂 Project Structure

```text
AI-Transcript-Cleanup-Engine/
│
├── app.py
├── README.md
├── requirements.txt
```

---

## ▶️ How to Run the Project

### Step 1: Install Streamlit

```bash
pip install streamlit
```

### Step 2: Run the Application

```bash
streamlit run app.py
```

---

## 📸 Example Input

```text
um AI AI is is powerful powerful
```

## ✅ Example Output

```text
AI is powerful.
```

---

## 📂 File Upload Example

### Uploaded File Content

```text
uh hello hello this is is NLP project project
```

### Cleaned Output

```text
Hello this is NLP project.
```

---

## 🧠 Working Process

1. User enters transcript text or uploads a `.txt` file.
2. The application processes the text.
3. Filler words and duplicate words are removed.
4. Formatting issues are cleaned.
5. Cleaned transcript is displayed.
6. User can download the cleaned transcript.

---

## 🎯 Project Objective

The objective of this project is to improve transcript readability by cleaning noisy speech-to-text outputs before evaluation or further NLP processing.

---

## 👨‍💻 Developer

Shiva

---

## 📌 Future Improvements

- Grammar correction
- AI-based text enhancement
- Multi-language transcript cleanup
- Audio-to-text integration<img width="1919" height="1029" alt="Screenshot 2026-05-22 102014" src="https://github.com/user-attachments/assets/40ed8953-b721-4a61-9d3d-5e207cbe2205" />
