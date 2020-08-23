from textblob import TextBlob

feedback1 = " food here"
feedback2 = "Plan for crisis and prepare a response. Limit the damage and protect your brand reputation. Minimize the risks and create a solid plan. Download the templates now! Brand Protection. Brand Measurement. Brand Promotion. Types: Social Media Analytics, Competitive Insights."
blob1 = TextBlob(feedback1)
blob2 = TextBlob(feedback2)

print(blob2.sentiment)
print(blob2.sentiment.polarity)
