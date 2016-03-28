from Classifier import Classifier

vocabularyFile = open("../Step_3/vocabulary.txt", mode='r', encoding = 'utf-8')
vocabulary = vocabularyFile.read().splitlines()
trainingFile = open("../Step_2/data.txt", mode='r', encoding = 'utf-8')
trainingData = trainingFile.read().splitlines()

x = Classifier(trainingData, vocabulary)
review = input('Enter a Review\n')
print(x.getClass(review))