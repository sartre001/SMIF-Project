import PyPDF2
from collections import Counter

# Read PDF file
file_path = "1Microsoft.pdf"
pdf_file = open(file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = text.split()
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

# Read and tokenize the PDF file
words = []
bigrams = []
trigrams = []

for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text().lower()
    words.extend(text.split())
    bigrams.extend(generate_ngrams(text, 2))
    trigrams.extend(generate_ngrams(text, 3))

# Define your initial positive and negative word lists here
positive_words = []  # Initialize it to an empty list
negative_words = []  # Initialize it to an empty list

# Extend the positive and negative words list
positive_words.extend(["growth", "profitable", "outperform", "innovative", "robust", "efficient", "leading", 
                       "expansion", "enhanced", "diversified", "stable", "accelerated", "positive", "successful", 
                       "increased", "booming", "bullish", "profitability", "optimized", "rewarding"])

negative_words.extend(["decline", "loss", "underperform", "risks", "challenges", "decreased", "volatile", 
                       "slowdown", "shortfall", "litigation", "weakness", "reduction", "concerns", "adverse", 
                       "downturn", "lagging", "bearish", "restructuring", "uncertainty"])

# Count the occurrences of sentiment words including n-grams
word_counter = Counter(words + bigrams + trigrams)
positive_count = {word: word_counter[word] for word in positive_words}
negative_count = {word: word_counter[word] for word in negative_words}

# Get the total counts
total_positive_words_detected = sum(positive_count.values())
total_negative_words_detected = sum(negative_count.values())

# Print the results
print("Positive sentiment word counts:")
for word, count in positive_count.items():
    print(f"{word}: {count}")
print(f"\nTotal positive words detected: {total_positive_words_detected}")

print("\nNegative sentiment word counts:")
for word, count in negative_count.items():
    print(f"{word}: {count}")
print(f"\nTotal negative words detected: {total_negative_words_detected}")

pdf_file.close()
