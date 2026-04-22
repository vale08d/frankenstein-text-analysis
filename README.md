# Frankenstein Text Analysis

> NLP analysis of Mary Shelley's *Frankenstein* — word frequency, sentiment trends,
> and character mentions, visualized with Python.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TextBlob%20%7C%20NLTK-green?style=flat)
![Data](https://img.shields.io/badge/Data-Pandas%20%7C%20Matplotlib-orange?style=flat)

## What This Does:

- Parses the full text of *Frankenstein* (75,000+ words)
- Calculates word frequency distribution and identifies top 50 most-used words
- Performs sentiment analysis chapter-by-chapter using TextBlob
- Tracks mentions of key characters (Victor, Creature, Clerval, Elizabeth) across the novel
- Visualizes all findings with Matplotlib charts

## Tech Stack:

| Tool | Purpose |
|------|---------|
| Python | Core scripting |
| TextBlob | Sentiment analysis |
| NLTK | Tokenization & stopword removal |
| Pandas | Data structuring & aggregation |
| Matplotlib | Visualization |

## How to Run:

```bash
# Clone the repo
git clone https://github.com/vale08d/frankenstein-text-analysis.git
cd frankenstein-text-analysis

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python frankenstein-text-analysis.py
```

## Sample Output:

<img width="798" height="686" alt="Capture_FRANK" src="https://github.com/user-attachments/assets/78b10ea7-b09c-4756-976e-83169a7b1b02" />


## What I Learned:

Working with raw text data at scale taught me how much preprocessing matters —
stopword removal and tokenization dramatically changed which words surfaced as
"most frequent." Sentiment analysis also revealed an interesting pattern:
narrative sentiment drops sharply in the second half of the novel, which maps
perfectly to the story's arc.

---
*Text source: Project Gutenberg (public domain)*
