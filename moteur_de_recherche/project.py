from nltk.stem import PorterStemmer
from collections import Counter
import math
import re
import os

def stem_words_fnc(documents):
    stemmer = PorterStemmer()
    stemmed_words = {}
    stop_words = {"a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it",
                  "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these",
                  "they", "this", "to", "was", "will", "with"}

    for document in documents:
        with open(document, 'r') as f:
            text = f.read()
        words = re.findall(r'\b\w+\b', text)
        stemmed_words_for_document = [stemmer.stem(word) for word in words if word not in stop_words]
        stemmed_words[document] = stemmed_words_for_document

    return stemmed_words

def SF_in_documents(documents):
    SF_per_document = {}
    stemmed_words = stem_words_fnc(documents)

    for document, stemmed_words in stemmed_words.items():
        frc = Counter(stemmed_words)
        SF_per_document[document] = frc

    return SF_per_document

def global_frc(documents):
    g_frc = Counter()

    SF_per_document = SF_in_documents(documents)
    for document, frequencies in SF_per_document.items():
        g_frc += frequencies

    return g_frc

def calculate_idf(documents):
    N = len(documents)
    global_freqs = global_frc(documents)

    idf = {}
    for word, global_frequency in global_freqs.items():
        idf[word] = math.log(N / global_frequency)

    return idf

def calculate_weights(documents):
    SF_per_document = SF_in_documents(documents)
    idf = calculate_idf(documents)

    weights = {}
    for document, frequencies in SF_per_document.items():
        base_document = os.path.basename(document)
        file_name, _ = os.path.splitext(base_document)
        weights[file_name] = {word: frequency * idf[word] for word, frequency in frequencies.items()}

    return weights

def build_inverted_file(documents):
    weights = calculate_weights(documents)

    with open('fich-inv.txt', 'w') as f:
        for document, word_weights in weights.items():
            for word, weight in word_weights.items():
                f.write(f'{word}----{document}-----{weight}\n')

def index_corpus(documents):
    documents = [os.path.abspath(document) for document in documents]
    build_inverted_file(documents)

def read_user_query():
    return input("Enter your query: ")

def index_user_query(query):
    stemmer = PorterStemmer()
    stop_words = {"a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it",
                  "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these",
                  "they", "this", "to", "was", "will", "with"}

    words = re.findall(r'\b\w+\b', query)
    stemmed_words = [stemmer.stem(word) for word in words if word not in stop_words]

    return stemmed_words

def calculate_query_weights(query_words, documents):
    idf = calculate_idf(documents)
    query_weights = {word: idf.get(word, 0) for word in query_words}

    return query_weights

def calculate_similarity_score(document_weights, query_weights):
    score = 0
    for word, weight in query_weights.items():
        score += document_weights.get(word, 0) * weight

    return score

def search_documents(query, documents):
    query_words = index_user_query(query)
    query_weights = calculate_query_weights(query_words, documents)
    document_weights = calculate_weights(documents)

    scores = {}
    for document, weights in document_weights.items():
        scores[document] = calculate_similarity_score(weights, query_weights)

    sorted_documents = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    return [document for document, score in sorted_documents if score != 0]

def main():
    documents = [
        "./files/testfile10.txt",
        "./files/testfile1.txt",
        "./files/testfile2.txt",
        "./files/testfile3.txt",
        "./files/testfile4.txt",
        "./files/testfile5.txt",
        "./files/testfile6.txt",
        "./files/testfile7.txt",
        "./files/testfile8.txt",
        "./files/testfile9.txt",
    ]

    index_corpus(documents)

    query = read_user_query()
    relevant_documents = search_documents(query, documents)

    print("Relevant documents:")
    for document in relevant_documents:
        print(document)

if __name__ == "__main__":
    main()