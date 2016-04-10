from Classifier import Classifier

vocabularyFile = open("../Step_6/vocabulary.txt", mode='r')
vocabulary = vocabularyFile.read().splitlines()
trainingFile = open("../Step_2/data.txt", mode='r')
trainingData = trainingFile.read().splitlines()

x = Classifier(trainingData, vocabulary)
review = input('Enter a Review\n')
print(x.getClass(review))
