from .models import User
import numpy as np
from sklearn.linear_model import LogisticRegression
froom .twitter import vectorize_tweet


def predict(user0_name, user1_name, hypo_tweet_text):

    user0 = User.query.filter(User.username == user0_name)
    user1 = User.query.filter(User.username == user1_name)

    #2D numpy arrays
    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    # X matrix for training the logistic regression
    vects = np.vstack([user0_vects, user1_vects])

    # Numpy Arrays
    zeros = np.zeros(len(user0.tweets))
    ones = np.ones(len(user1.tweets))

    # y vector (target) for training the logistic regression
    labels = np.concatenate([zeros, ones])

    log_reg = LogisticRegression()

    #train our logistic regression
    log_reg.fit(vects, labels)

    # Vectorize (get tge word embeddings for)
    # Hypothetical tweet text
    hypo_tweet_text = vectorize_tweet(hypo_tweet_text)
    
    #Get a prediction for which user is mopre likely to say the hypo_tweet_text
    prediction = log_reg.predict(hypo_tweet_vect.reshape(1, -1))

    return prediction