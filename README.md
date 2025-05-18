# 📖 HadithView

> ⚠️ **This project is under active development.**  
> Core functionality is stable, but features, design, and interface are being continuously improved.

**HadithView** is a lightweight Streamlit-based interface for semantic exploration of one of the most comprehensive open-access hadith corpora.  
It enables metadata-driven search and structured viewing of over **50,000 canonical hadiths** drawn from the foundational collections of Sunni Islam.

---

## 🌐 Project Overview

This application provides a direct interface to the **`hadith_corpus_extended.parquet`** file, a unified and highly optimized dataset built from the [Open Hadith Data](https://github.com/mhashim6/Open-Hadith-Data) project by [Muhammad Hashim (mhashim6)](https://github.com/mhashim6).  
The dataset includes complete textual data (Arabic + English), detailed metadata, and structural fields for accurate filtering and analysis.

The app was designed as a complementary visual tool for corpus linguists, students of Islam, digital humanists, and developers building NLP systems over classical religious data.

---

## ⚙️ Features

- 🔎 Full-text and metadata-based search by:
  - Book, collection, author
  - Chapter, narrator, numeric ID
- 🧾 Rich metadata display including isnād, grading, topics, tags, commentary, etc.
- 🌐 Arabic text rendering with right-to-left formatting
- 📦 Efficient backend via `.parquet` dataset

---

## 🛠️ Usage

1. Clone the repository:

```bash
git clone git@github.com:Quchluk/HadithView.git
cd HadithView

	2.	Install dependencies:

pip install -r requirements.txt

	3.	Launch the app:

streamlit run view_hadith_streamlit.py

The app will open in your browser. Use the interface to search and browse the hadith corpus.

---

📚 Dataset

The .parquet file used in this project (hadith_corpus_extended.parquet) contains over 50,000 hadiths from 9 major collections, including the Six Canonical Books (Kutub al-Sittah), fully annotated with metadata for academic use. Each record includes:
	•	Arabic text (diacritized & clean)
	•	English translation
	•	Author, collection, chapter, isnād
	•	Grading, topics, tags, commentary, references

This format enables high-performance access, scalable queries, and serves as a reliable base for building downstream NLP pipelines or educational tools.

⸻

👤 Author

Developed by Anton Smirnov
🔗 github.com/Quchluk

⸻

📄 License

This project is licensed under the MIT License.
``
