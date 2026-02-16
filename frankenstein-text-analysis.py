from pathlib import Path
from textblob import TextBlob
from nltk.corpus import stopwords
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt

# Load the text file
blob = TextBlob(Path('Frankenstein.txt').read_text(encoding='utf-8'))

# Load stop words and extend with custom words
stop_words = stopwords.words('english')
custom_stopwords = ['one', 'could', 'would', 'yet', 'shall', 'upon', 'must',
                   'may', 'might', 'every', 'first', 'two', 'three']
stop_words.extend(custom_stopwords)

# Get word frequencies 
items = blob.word_counts.items()

# Eliminate stop words and non-alphabetic words
items = [item for item in items if item[0] not in stop_words and item[0].isalpha()] #isalpha() removes punctuation/numbers

# Sort by frequency in descending order
sorted_items = sorted(items, key=itemgetter(1), reverse=True)

# Get top 10 words
top10 = sorted_items[0:10]

# Convert to DataFrame
df = pd.DataFrame(top10, columns=['word', 'count'])

# Display the data
print("\nFrankenstein - TOP 10 WORDS:")
print(df.to_string(index=False))

# Visualize with bar chart
axes = df.plot.bar(x='word', y='count', legend=False)
plt.title('Frankenstein - TOP 10 WORDS', fontsize=14, fontweight='bold')
plt.xlabel('Words', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.gcf().tight_layout()
plt.show()