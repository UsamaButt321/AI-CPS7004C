# Define lists of positive and negative words
positive_words = ['happy', 'good', 'great', 'fantastic', 'wonderful', 'love', 'excellent', 'amazing']
negative_words = ['sad', 'bad', 'terrible', 'awful', 'worst', 'hate', 'poor', 'horrible']


def analyze_sentiment(text):
    # Tokenize the text into words

    # Initialise sentiment scores
    positive_score = 0
    negative_score = 0

    # Calculate the sentiment score
    for word in words:
        

    # Determine overall sentiment (neutral by default)
    sentiment = 'Neutral'

    if positive_score > negative_score:
        sentiment = 'Positive'
    elif negative_score > positive_score:
        sentiment = 'Negative'

    return sentiment


# Example usage
text = "I love the wonderful and fantastic weather, but I hate the bad traffic."
result = analyze_sentiment(text)
print(f"The sentiment of the text is: {result}")
