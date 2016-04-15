from sys import path
path.append('..')
from Step_4.Classifier import Classifier
import pickle


vocabularyFile = open("../Step_3/vocabulary.txt", mode='r', encoding = 'utf-8')
trainingFile = open("../Step_2/data.txt", mode='r', encoding = 'utf-8')
vocabulary = vocabularyFile.read().splitlines()
trainingData = trainingFile.read().splitlines()

trainingData.sort()

positiveData = trainingData[:320]
negativeData = trainingData[320:]

posFactor = len(positiveData)//10
negFactor = len(negativeData)//10

avgAccuracy = 0

for i in range(10):
	testSet = positiveData[i*posFactor:i*posFactor+posFactor] + negativeData[i*negFactor:i*negFactor+negFactor]
	trainingSet = positiveData[:i*posFactor]+positiveData[i*posFactor+posFactor:]+negativeData[:i*negFactor]+negativeData[i*negFactor+negFactor:]
	
	try:
		x = pickle.load(open("model"+str(i)+".pickle", "rb"))
	except (OSError, IOError) as e:
		x = Classifier(trainingSet, vocabulary)
		pickle.dump(x, open("model"+str(i)+".pickle", "wb"))

	right = 0
	wrong = 0
	for reviewItem in testSet:
		(reviewClass, review) = reviewItem.split('\t')
		if reviewClass == x.getClass(review):
			right = right + 1
		else:
			wrong = wrong + 1
	print('Accuracy for TestSet',(i+1), '=',right/(right+wrong))
	avgAccuracy = avgAccuracy + right/(right+wrong)

print('Avg Accuracy =',avgAccuracy/10)

			
			