import os
import re
import csv
import pandas as pd
import urllib.parse


def crawl(category):

	file_name=category+".csv"
	links=[]

	df = pd.read_csv(file_name)
	links = df.URL #you can also use df['column_name']
	
	user=""
	passwd=""

	string="python edx_crawler.py -u " + user +"  -p "+passwd+" -url "
	for link in links:
		link=link.strip('\n')
		link=urllib.parse.unquote(link,encoding='utf-8', errors='replace')
		query=string+link
		print ("<"+query+">")
		try:
			os.system(query)
		except Exception as e:
			print(e)
			continue			


def main():
	#categs=["Business & Management"]
	categs=["Business & Management", "Computer Science", "Humanities"]
	for c in categs:
		crawl(c)


if __name__== "__main__":
	main()		