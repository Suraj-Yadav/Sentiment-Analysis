from math import log2

class Classifier:
	def __init__(self, trainingData, vocabulary):
		self.wordsFreq = dict()
		self.classWordList = dict()
		self.classCount = dict()
		
		for item in trainingData:
			possibleClass = item[:item.index('\t')]
			if possibleClass not in self.classWordList:
				self.classWordList[possibleClass] = []
				self.classCount[possibleClass] = 0
		
		for i in vocabulary:
			self.wordsFreq[i] = dict(self.classCount)
			
		
		for item in trainingData:
			text = item.split()
			
			self.classCount[text[0]] += 1
	
			i = 0
			while i<(len(text)-1):
				if (text[i] + " " + text[i+1]) in vocabulary:
					word = text[i] + " " + text[i+1]
					self.wordsFreq[word][text[0]] += 1
					self.classWordList[text[0]].append(word)
					i+=2
				elif text[i] in vocabulary:
					word = text[i]
					self.wordsFreq[word][text[0]] += 1
					self.classWordList[text[0]].append(word)
					i+=1
				else:
					i+=1
			
			if text[len(text)-1] and i<len(text) in vocabulary:
				word = text[len(text)-1]
				self.wordsFreq[word][text[0]] += 1
				self.classWordList[text[0]].append(word)	
				
		#print(self.wordsFreq)
		#print(self.classWordList)
		#print(self.classCount)	

	
	def getClass(self, string):
		maxProb = float('-inf')
		maxClass = ''
		
		for possibleClass in self.classCount:
			logProb = log2(self.classCount[possibleClass])-log2(sum(self.classCount.values()))
			# print(i)
			
			i = 0
			text = string.split()
			
			while i<(len(text)-1):
				if (text[i] + " " + text[i+1]) in self.wordsFreq:
					word = text[i] + " " + text[i+1]
					#print(word,"1")
					wordLogProb = log2(self.wordsFreq[word][possibleClass]+1)-log2(len(self.classWordList[possibleClass])+len(self.wordsFreq)+1)
					i+=2
				elif text[i] in self.wordsFreq:
					word = text[i]
					#print(word,"2")
					wordLogProb = log2(self.wordsFreq[word][possibleClass]+1)-log2(len(self.classWordList[possibleClass])+len(self.wordsFreq)+1)
					i+=1
				else:
					#print("$$")
					wordLogProb = -log2(len(self.classWordList[possibleClass])+len(self.wordsFreq)+1)
					i+=1
				logProb += wordLogProb
				
			if logProb > maxProb:
				maxProb = logProb
				maxClass = possibleClass
		
		# print(maxProb)
		
		return maxClass
