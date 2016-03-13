'''
Created vocabulary. Vocabulary is defined as the set of all words in the corpus which appears at least 2 times. The vocabulary is a text file named vocabulary.txt.
'''
import re

originalDataFile = open("../Step_2/data.txt",mode='r', encoding = 'utf-8')

corpus = originalDataFile.read().split()
corpus = sorted(corpus,key=str)

newDataFile = open("vocabulary.txt", mode='w', encoding = 'utf-8')

vocab = set([])

for a in corpus:
	corpus.remove(a)
	if a in corpus:
		vocab.add(a)	

vocab = sorted(vocab,key=str)

for a in vocab:
	if(not(a == '+') and not(a == '-')):
		newDataFile.write(a)
		newDataFile.write('\n')

