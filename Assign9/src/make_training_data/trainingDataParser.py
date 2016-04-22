import feedparser 
import ConfigParser
import unicodedata
import sys 






if __name__ == '__main__':
	

	# Get a list of categories  
	categoryList = None
	try:
	
		fp = open('50SCRIPT.txt', 'r')
		categoryList = [category.strip('\n') for category in fp.readlines()]
		#categoryList = [str(category.strip('\r')) for category in categoryList]

	except IOError as e:
		sys.stderr.write("Error open,ing {0}, {1}\n".format('ManualEntries.txt',e[1]))

	print(categoryList)

	#createMatchedData(fp)
	for line in categoryList:
		tokenizedString = line.split('|')
		uri=tokenizedString[0]
		category=tokenizedString[1]
		print(uri)
		print(category)
		print('\n')