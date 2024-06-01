#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# loading both the ratings and to-read data
ratings_df = pd.read_csv('ratings.csv')
to_read_df = pd.read_csv('to_read.csv').sample(frac=0.1, random_state=42)

# calculating the number of ratings per sentiment category
def get_sentiment(rating):
    if rating >= 4:
        return 'Positive'
    elif rating == 3:
        return 'Neutral'
    else:
        return 'Negative'

ratings_df['sentiment'] = ratings_df['rating'].apply(get_sentiment)
sentiment_counts_ratings = ratings_df['sentiment'].value_counts()

# calculating the number of books users intend to read per user
books_per_user = to_read_df.groupby('user_id')['book_id'].count()
to_read_counts = pd.cut(books_per_user, bins=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50], include_lowest=True).value_counts()

# creating a pie chart to visualize sentiment distribution of ratings
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.pie(sentiment_counts_ratings, labels=sentiment_counts_ratings.index, autopct='%1.1f%%', startangle=140, colors=['#F2BABA', '#F8D0C8', '#F9DDD8'])
plt.title('Sentiment Distribution of Ratings')

# creating a line chart to visualize to-read counts distribution
plt.subplot(1, 2, 2)
to_read_counts.plot(kind='line', color='#A759E6')
plt.title('To-Read Counts Distribution')
plt.xlabel('Number of Books')
plt.ylabel('Number of Users')

plt.tight_layout()
plt.show()


# In[ ]:




