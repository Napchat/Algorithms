from Gragh import Gragh

def buildGragh(wordFile):
	d = {}
	g = Gragh()
	with open(wordFile, 'r') as f:
		# Create buckets of words that differ by one letter
		for line in f:
			word = line[:-1]
			for i in range(len(word)):
				bucket = word[:i] + '_' + word[i+1:]
				if bucket in d:
					d[bucket].append(word)
				else:
					d[bucket] = [word]

		# Add vertices and edges for words in the same bucket
		for bucket in d.keys():
			for word1 in d[bucket]:
				for word2 in d[bucket]:
					if word1 != word2:
						g.addEdge(word1, word2)
	return g
