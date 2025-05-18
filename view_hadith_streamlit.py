import pandas as pd
import streamlit as st

FILE_PATH = "/Users/Tosha/Desktop/Hadith RAG/Project Hadith RAG/hadith_corpus_extended.parquet"

@st.cache_data
def load_data():
    return pd.read_parquet(FILE_PATH)

df = load_data()

st.title("📖 HadithView")
st.markdown("Search and browse the hadith corpus by metadata, including book, collection, narrator, or ID.")

# === Input filters ===
hadith_id_input = st.text_input("🔍 Enter specific Hadith ID (exact match):")

df_filtered = df.copy()

if hadith_id_input:
    try:
        hadith_id_int = int(hadith_id_input)
        df_filtered = df[df["hadith_id"] == hadith_id_int]
    except ValueError:
        st.warning("Please enter a valid integer ID.")

# === Author Filter ===
authors = sorted(df_filtered["author_en"].dropna().unique())
selected_author = st.selectbox("🧑‍🏫 Select author:", ["(all)"] + authors)
if selected_author != "(all)":
    df_filtered = df_filtered[df_filtered["author_en"] == selected_author]

# === Collection Book Filter ===
collections = sorted(df_filtered["collection_book"].dropna().unique())
selected_collection = st.selectbox("📚 Select collection book:", ["(all)"] + collections)
if selected_collection != "(all)":
    df_filtered = df_filtered[df_filtered["collection_book"] == selected_collection]

# === Book ID (Numeric) ===
book_ids = sorted(df_filtered["book_id"].dropna().unique())
selected_book_id = st.selectbox("📘 Select book ID (numeric):", ["(all)"] + [str(b) for b in book_ids])
if selected_book_id != "(all)":
    df_filtered = df_filtered[df_filtered["book_id"] == int(selected_book_id)]

# === Chapter Title ===
chapters = sorted(df_filtered["chapter_title_en"].dropna().unique())
selected_chapter = st.selectbox("📖 Select chapter title:", ["(all)"] + chapters)
if selected_chapter != "(all)":
    df_filtered = df_filtered[df_filtered["chapter_title_en"] == selected_chapter]

# === Narrator ===
narrators = sorted(df_filtered["narrator_en"].dropna().unique())
selected_narrator = st.selectbox("👤 Select narrator:", ["(all)"] + narrators)
if selected_narrator != "(all)":
    df_filtered = df_filtered[df_filtered["narrator_en"] == selected_narrator]

# === Search ===
if st.button("Search"):
    if df_filtered.empty:
        st.info("No hadiths found with the selected criteria.")
    else:
        st.markdown(f"### Found {len(df_filtered)} hadith(s):")
        for _, row in df_filtered.iterrows():
            st.markdown(f"---\n### 🆔 Hadith ID: {row['hadith_id']}")
            st.markdown(f"**📙 Book:** {row['book_title_en']} ({row['book_title_ar']})")
            st.markdown(f"**📖 Chapter:** {row['chapter_title_en']} ({row['chapter_title_ar']})")
            st.markdown(f"**👤 Narrator:** {row['narrator_en']}")
            st.markdown("**📝 Arabic Text:**")
            st.markdown(
                f"<div style='font-family: serif; direction: rtl; text-align: right;'>{row['text_ar']}</div>",
                unsafe_allow_html=True
            )
            st.markdown("**🌐 English Translation:**")
            st.markdown(row["text_en"])

            st.markdown("#### 🧾 Metadata:")
            meta_cols = [
                "grade", "source", "tags", "translator", "explanation",
                "related_hadiths", "location", "subject", "collection",
                "volume", "page", "section", "commentary", "keywords",
                "narrator_chain", "date", "category",
                "collection_set", "collection_book", "chapter_file_name", "source_path"
            ]
            for col in meta_cols:
                val = row.get(col, "no data")
                if isinstance(val, list):
                    val = ", ".join(val)
                st.markdown(f"**{col.replace('_', ' ').capitalize()}:** {val}")
else:
    st.info("Please enter search criteria and click 'Search'.")
