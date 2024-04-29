import os
import re
from nltk.stem import PorterStemmer

stop_words = {"a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"}
files = [f'./files/testfile{i}.txt' for i in range(1, 11)]

def stem_word(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word)

def clean_word(word):
    word = re.sub(r'\d+|\b\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}\b', '', word)
    word = word.lower()
    return word

def process_file(input_file, output_file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_file)
    with open(input_file, 'r') as f:
        text = f.read()
    words = re.findall(r'\b\w+\b', text)
    cleaned_words = [clean_word(word) for word in words if word.lower() not in stop_words]    
    stemmed_words = [stem_word(word) for word in cleaned_words]    
    output_file = os.path.join(script_dir, output_file)

    with open(output_file, 'w') as f:
        f.write(' '.join(stemmed_words))

for file in files:
    process_file(file, 'sortie.txt')
