# Team 8 Section 1 Final project
## Identify and solve U.S. airlines flight problems by analyzing tweets 

The airline industry, in general, suffers with several challenges such as flight delays, cancelations, missed flights, lost luggage, etc. which lead to unsatisfied passenger experience. With the advent of social media – these customer challenges come to the forefront and have severe impact on the company’s reputation. 

Twitter data of Airline passengers was used for this analysis. The data was cleansed and preprocessed suitably to be used for NLP methodologies. Two techniques were used in the scope of this project – Sentiment Analysis was carried out to determine if indeed this data could be used to identify problems areas faced by the customers of the airlines.

## Project_code_1 
### Pre-processing
After reading data from "Tweet Data.xlsx". We do pre-processing to understand the data. This process including data status figure, data cleaning, and visulization.

### Sentiment Analyze
In the step of finding the sentiment for each tweets, we use SentimentIntensityAnalyzer from nltk to figure the entiment of the words. Each sentance (or tweet) is scored, and determind if it is negative, postive or neutral. Use the socre to classficate the data. The result is shown as well.

### Topic Analyze
In this step, according to Latent Dirichlet Allocation process, all the tweets are spearte by topics. As result, show the Top 20 words in each topic for analyze

### Word Cloud
The word Cloud is a collection of all key-words for each complaint reason. Each reason's top words are collected for regular expression in the next step. Besides, save 'negativeTweets.csv' for next step.

## Project_code_2 reads data from "Tweet Data.xlsx".
### Function for fitting the problem to the right reason
The function is use to analyze a sentance's compalint reason if the sentance is not exract from our database. In this function, we use Decision Tree to classificate different type of reasons. The trained model is used for analyzing which reason shall the sentance if to.

### Auto read system (two parts) 
#### 1. Regular Expression Dictionary
In this section, all the reason is seprate into diffection locations. Each reason is paired with certain key-words. Also, it get paired with reason itself for problem fitting function.

#### 2. Auto reply
The system will read the sentance and than give the best reply according to the complaint. The reply will contain the airline information during the reply.
If the sentance is not using data from our database, it will use the problem fitting function to identiy the right reason for the sentance.
