import pandas as pd

# Укажи путь к своему файлу
FILE_PATH = "/Users/Tosha/Desktop/Hadith RAG/Project Hadith RAG/hadith_corpus_extended.parquet"

# Загружаем данные
df = pd.read_parquet(FILE_PATH)

# Показываем общую информацию о столбцах
print("=== Общая структура данных ===")
print(df.info())

# Список всех столбцов
print("\n=== Список столбцов ===")
print(df.columns.tolist())

# Проверка на уникальность hadith_id
print("\n=== Уникальность hadith_id ===")
print("Уникален ли hadith_id?", df["hadith_id"].is_unique)

# Анализ длины хадисов (английский текст)
print("\n=== Длина хадисов (text_en) ===")
print(df["text_en"].str.len().describe())

# Показываем первые 3 строки для просмотра структуры
print("\n=== Пример строк ===")
print(df[["hadith_id", "book_id", "chapter_id", "hadith_id_in_book", "collection_book", "text_en"]].head(3))