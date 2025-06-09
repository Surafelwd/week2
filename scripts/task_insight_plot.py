# Task 4: Insights and Recommendations
# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

# Create 'visuals' directory if it doesn't exist
os.makedirs('visuals', exist_ok=True)

# Load sentiment-labeled review data
df = pd.read_csv('data/all_reviews_with_sentiment.csv')

# Example cleaning (ensure no NaNs in required columns)
df = df.dropna(subset=['review', 'sentiment'])

# --------------------------
# 1. Plot: Sentiment Distribution per Bank
# --------------------------
sns.countplot(data=df, x='sentiment', hue='bank')
plt.title('Sentiment Distribution per Bank')
plt.xlabel('Sentiment')
plt.ylabel('Review Count')
plt.legend(title='Bank')
plt.tight_layout()
plt.savefig('visuals/sentiment_distribution.png')
plt.clf()

# --------------------------
# 2. Plot: Rating Distribution
# --------------------------
sns.histplot(data=df, x='rating', hue='bank', multiple='stack', bins=5)
plt.title('Rating Distribution by Bank')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('visuals/rating_distribution.png')
plt.clf()

# --------------------------
# 3. Plot: Word Cloud per Sentiment (Optional)
# --------------------------
for sentiment_label in ['positive', 'neutral', 'negative']:
    text = ' '.join(df[df['sentiment'] == sentiment_label]['review'].astype(str))
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud: {sentiment_label.capitalize()} Reviews')
    plt.tight_layout()
    plt.savefig(f'visuals/wordcloud_{sentiment_label}.png')
    plt.clf()

# --------------------------
# 4. Extract Top Drivers and Pain Points
# --------------------------
# (Use basic keyword frequency or pre-tagged themes if available)
from collections import Counter
import re

# Combine all reviews for initial keyword frequency
def extract_keywords(text):
    return re.findall(r'\b[a-z]{4,}\b', text.lower())  # basic word filtering

keywords = extract_keywords(' '.join(df['review']))
common_words = Counter(keywords).most_common(50)

# Save to file or print top terms
print("Top Keywords:")
for word, freq in common_words[:20]:
    print(f"{word}: {freq}")

# --------------------------
# 5. Recommendations (To be written manually based on above insights)
# --------------------------
# Examples:
# - Drivers: Easy navigation, quick login, lightweight app
# - Pain Points: Frequent crashes, login errors, delayed transactions
# - Suggestions: Add dark mode, improve error messaging, enable biometric login
