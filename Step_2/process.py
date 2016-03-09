import re

stopWordFile = open("stopwords.txt",mode='r',encoding = 'utf-8')

stopWords = stopWordFile.read().splitlines()

originalDataFile = open("../Step_1/data.txt",mode='r', encoding = 'utf-8')

corpus = originalDataFile.read().splitlines()

newDataFile = open("data.txt", mode='w', encoding = 'utf-8')

for str in corpus:
	entry = str.split('\t');
	newDataFile.write(entry[0]+'\t')
	wordList = re.split('[\s\.\[\]\"!,()?/]', entry[1]);
	for word in wordList:
		if word.isalpha() == False:
			if '-' in word:
				subWord = word.split('-');
				if len(subWord)>1 and subWord[0].isalpha() and subWord[1].isalpha():
					newDataFile.write(word.lower()+' ')
					continue
				else:
					print('Error')
			elif "'" in word:
				subWord = word.split("'");
				if len(subWord)>1 and subWord[0].isalpha() and subWord[1].isalpha():
					newDataFile.write(word.lower()+' ')
					continue
				else:
					print('Error')
			else:
				print('Error')
		else:
			newDataFile.write(word.lower()+' ')
	newDataFile.write('\n')