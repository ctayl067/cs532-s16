# -*- coding: UTF-8 -*-
import feedparser 
import unicodedata
import ConfigParser
import sys 

sys.path.insert(0, '../lib/chapter6')

from docclass import *





def readtheCRAP(dataFilename):

	TData=None
	try:
		Tfile=open(dataFilename,'r')
		TData = {}
		for line in Tfile.readlines():
			tmp = line.split('|')
			TData[tmp[0]] = tmp[1].strip('\n')
	except IOError as e:
		sys.stderr.write('Error what are you giving me human? : {0}, {1}\n'.format(dataFilename,e[1]))
	return TData





def setTheIDSforPosts(feedNameFile):

	idsToPosts = None
	try:
		v = open(feedNameFile,'r')
		v.close()
		d = feedparser.parse(feedNameFile)
		idsToPosts={}

		for e in d.entries:
			
			idsToPosts[(e['link'])] = e

	except IOError as e:
		sys.stderr.write('Error...again...you suck: {0}, {1}\n'.format(feedNameFile,e[1]))
	return idsToPosts





def MatchthecCrap(nonTLinks):

	NTLinks=None
	try:
		NTfile=open(nonTLinks,'r')
		nonTLinks = {}
		for line in NTfile.readlines():
			tmp = line.split('|')
			nonTLinks[tmp[0]] = tmp[1].strip('\n')
			#print('THIS SHIT WORKS')
	except IOError as e:
		sys.stderr.write('Error bruh....: {0}, {1}\n'.format(nonTLinks,e[1]))
	
	return nonTLinks





def trainer(trainedList,feedNameFile):

	nonTrainedData=None
	try:
		nonTdata=open(trainedList,'r')
		trainedList = {}
		sys.stderr.write("training Classifier....\n")
		for line in nonTdata.readlines():
			#feedNameFile = idsToPosts[key]
			tmp = line.split('|')
			trainedList[tmp[0]] = tmp[1].strip('\n')
			c1.train(feedNameFile.description, trainingData[key])
			counter += 1
			sys.stderr.write('.....Trained {0} of {1} training entries\n'.format(counter,size))
	except IOError as e: 
		sys.stderr.write("Error man what r u even doing like what the Fudge......")

	
















if __name__ == '__main__':
	

	feedNameFile = '../data/feed_data/news.xml'

	dataFilename = 'trainingData.txt'

	categoryFile = '../data/categories.txt'

	nonTLinks = 'next50.txt'

	trainedList = 'needsTraining.txt'

#READ

	trainingData = readtheCRAP(dataFilename)
	#print(trainingData)

	idsToPosts  = setTheIDSforPosts(feedNameFile)

	NTLinks = MatchthecCrap(nonTLinks)
	trainedStuff = trainer(trainedList,feedNameFile)

	#for i in trainingData.keys():
		#print(idsToPosts[i].description)
		
	#categoryFile = readtheCategories(categoryFile)

	#for element in d.items: