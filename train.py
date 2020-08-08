from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pickle
import nltk.classify.util
import sys
import numpy as np


def clean(words):
    return dict([(word, True) for word in words])


negative_ids = movie_reviews.fileids('neg')
positive_ids = movie_reviews.fileids('pos')


negative_features = [(clean(movie_reviews.words(fileids=[f])), 'negative') for f in negative_ids]
positive_features = [(clean(movie_reviews.words(fileids=[f])), 'positive') for f in positive_ids]


negative_cutoff = int(len(negative_features) * 95/100)
positive_cutoff = int(len(positive_features) * 90/100)

train_features = negative_features[:negative_cutoff] + positive_features[:positive_cutoff]
test_features = negative_features[negative_cutoff:] + positive_features[positive_cutoff:]

print('Training on %d data, testing on %d data' % (len(train_features), len(test_features)))
classifier = NaiveBayesClassifier.train(train_features)
print('Training complete')
print('accuracy:', nltk.classify.util.accuracy(classifier, test_features)*100,'%')
classifier.show_most_informative_features()

# Create model file, 
f = open('model', 'wb')
pickle.dump(classifier, f)
f.close()


#To check if it is working or not.


f = open('model', 'rb')
classifier = pickle.load(f)
f.close()



sentence="i don't love you "
features = clean(sentence)
print(classifier.classify(features))

sentence="i love you sweetheart "
features = clean(sentence)
print(classifier.classify(features))


sentence="i am not saying that i don't love you"
features = clean(sentence)
print(classifier.classify(features))

sentence="This size of laptop is very bad"
features = clean(sentence)
print(classifier.classify(features))

