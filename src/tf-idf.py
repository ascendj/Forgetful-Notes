import csv
import math
from sklearn.feature_extraction.text import TfidfVectorizer

def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_word_frequencies(csv_file_path):
    word_frequencies = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) 
        for row in csvreader:
            word, frequency = row
            word_frequencies[word.lower()] = int(frequency)
    return word_frequencies

def calculate_idf_scores(word_frequencies, min_df=0, max_df=0.5):
    idf_scores = {}
    estimated_total_documents = sum(word_frequencies.values())
    for word, freq in word_frequencies.items():
        doc_freq = freq / estimated_total_documents
        if doc_freq < min_df or doc_freq > max_df:
            continue
        idf_scores[word] = math.log((1 + estimated_total_documents) / (1 + freq)) + 1  # Smooth idf
    return idf_scores

def calculate_tfidf_scores(tfidf_matrix, feature_names, idf_scores):
    tfidf_adjusted_scores = []
    for idx, tf_score in enumerate(tfidf_matrix.toarray()[0]):
        word = feature_names[idx]
        idf = idf_scores.get(word, 0)  
        tfidf = tf_score * idf 
        tfidf_adjusted_scores.append((word, tfidf))
    return tfidf_adjusted_scores

def get_top_n_keywords(tfidf_scores, top_n=10):
    sorted_items = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
    return sorted_items[:top_n]

def main(document_path, frequency_csv_path, top_n=10):
    document_content = read_document(document_path)
    documents = [document_content]
    
    word_frequencies = load_word_frequencies(frequency_csv_path)
    idf_scores = calculate_idf_scores(word_frequencies)
    
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    adjusted_tfidf_scores = calculate_tfidf_scores(tfidf_matrix, feature_names, idf_scores)
    top_keywords = get_top_n_keywords(adjusted_tfidf_scores, top_n)
    
    print("Top Keywords:")
    for word, score in top_keywords:
        print(f"- {word}: {score:.4f}")

if __name__ == "__main__":
    main('data/entanglement.txt', 'data/unigram_freq.csv', top_n=10)
