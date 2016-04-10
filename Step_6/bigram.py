import operator

originalDataFile = open("../Step_2/data.txt",mode='r')
newDataFile = open("vocabulary.txt", mode='w')

vocab = dict()

for line in originalDataFile:
	
	text = line.split()
	
	for i in range (1, len(text)-1):
		if text[i] in vocab:
			vocab[text[i]]+=1
		else:
			vocab[text[i]] = 1
		if (text[i] + " " + text[i+1]) in vocab:
			vocab[text[i] + " " + text[i+1]]+=1
		else:
			vocab[text[i] + " " + text[i+1]] = 1
	
	if text[len(text)-1] in vocab:
		vocab[text[len(text)-1]]+=1
	else:
		vocab[text[len(text)-1]] = 1

sorted_vocab = [a for a in vocab if vocab[a] >= 3]

sorted_vocab.sort();

for a in sorted_vocab:
		newDataFile.write(a + '\n')

