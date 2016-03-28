class Classifier:
	def __init__(self, trainingData, vocabulary):
		self.wordsFreq = dict()
		self.classFreq = dict()
		self.classCount = dict()
		
		for item in trainingData:
			possibleClass = item[:item.index('\t')]
			if possibleClass not in self.classFreq:
				self.classFreq[possibleClass] = []
				self.classCount[possibleClass] = 0
		
		for i in vocabulary:
			self.wordsFreq[i] = dict(self.classCount)
			
		
		for item in trainingData:
			entry = item.split('\t')
			
			self.classCount[entry[0]]=self.classCount[entry[0]]+1
			
			wordlist = entry[1].split()
			
			for word in wordlist:
				if word in vocabulary:
					self.wordsFreq[word][entry[0]]=self.wordsFreq[word][entry[0]]+1
					self.classFreq[entry[0]].append(word)
	
	def getClass(self, string):
		maxProb = -100
		maxClass = ''
		
		for i in self.classCount:
			prob = self.classCount[i]/(sum(self.classCount.values()))
			# print(i)
			for word in string.split():
				if word in self.wordsFreq:
					wordProb = (self.wordsFreq[word][i]+1)/(len(self.classFreq[i])+len(self.wordsFreq)+1)
				else:
					wordProb = (1/(len(self.classFreq[i])+len(self.wordsFreq)+1))
				prob = prob * wordProb
				# print('\t',word, wordProb)
			
			# print(prob,'\n****************')
		
			if prob > maxProb:
				maxProb = prob
				maxClass = i
		
		# print(maxProb)
		
		return maxClass
