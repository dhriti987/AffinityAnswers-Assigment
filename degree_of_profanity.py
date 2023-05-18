import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from typing import List

class DegreeOfProfanity:

    def __init__(self, racial_slurs: List[str]) -> None: # Intializi
        self.racial_slurs = racial_slurs

    def get_degree_of_profanity(self, tweet: List[str]) -> float:
        slurs_in_tweet = [word for word in tweet if word in self.racial_slurs] # Selecting the Slurs
        degree_of_profanity = len(slurs_in_tweet)/len(tweet)
        return degree_of_profanity
    
    def compute_degree_of_profanities(self, tweets: List[str]) -> List:
        try:
            lemmatizer = WordNetLemmatizer()  # Lemmatizer 
            degree_of_profanities = []  # List that will contain Degree of Profanity for each tweet
            
            for tweet in tweets:  # Parsing a tweet at a time
                sentences = nltk.sent_tokenize(tweet)  # Tokenization of Sentence
                for sentence in sentences:
                    words = nltk.words_tokenize(sentence)  # Word Tokenization
                    words = words.lower()  # Lowering the words to ignore the case sensitivity
                    tweet = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')] # Discarding Stopwords
                    degree_of_profanities.append(self.get_degree_of_profanity(tweet=tweet))
            
            return degree_of_profanities
        except Exception as e:
            raise e
