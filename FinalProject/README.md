# Team 8 Section 1 Final project
## Identify and solve U.S. airlines flight problems by analyzing tweets 

The airline industry, in general, suffers with several challenges such as flight delays, cancelations, missed flights, lost luggage, etc. which lead to unsatisfied passenger experience. With the advent of social media – these customer challenges come to the forefront and have severe impact on the company’s reputation. 

Twitter data of Airline passengers was used for this analysis. The data was cleansed and preprocessed suitably to be used for NLP methodologies. Two techniques were used in the scope of this project – Sentiment Analysis was carried out to determine if indeed this data could be used to identify problems areas faced by the customers of the airlines.

Project_code_1 reads data from "Tweet Data.xlsx".
### Pre-processing
We do pre-processing to understand the data. This process including data status figure, data cleaning, and visulization.

### Sentiment Analyze
In the step of finding the sentiment for each tweets, we use SentimentIntensityAnalyzer from nltk to figure the entiment of the words. Each sentance (or tweet) is scored, and determind if it is negative, postive or neutral. Use the socre to classficate the data. The result is shown as well.

### Topic Analyze
In this step, according to Latent Dirichlet Allocation process, all the tweets are spearte by topics. As result, show the Top 20 words in each topic for analyze

### Word Cloud
