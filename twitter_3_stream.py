import cgi
import os

form = cgi.FieldStorage()

keywords = form.getvalue('keywords')
stream_mode = form.getvalue('stream_mode')
num_tweets  = form.getvalue('num_tweets')
keywords_list = keywords.split()

f = open("stream.py", "w")
f.write("from choices_functions import *\n\n")
if(stream_mode == 'limited'):
	f.write("funct_choice_3("+str(keywords_list)+", "+'1'+", "+num_tweets+")")
elif(stream_mode == 'unlimited'):
	f.write("funct_choice_3("+str(keywords_list)+", "+'0'+")")
f.write("\n\nx = input()")
f.close()

os.system("python stream.py")

#print("Content-type: text/html; charset=utf-8\n")

#html = """
#<!DOCTYPE html>
#<html>
#<head>
#<title>COVID-19 Data Extractor</title>
#</head>
#<body>

#<h1>The Stream is Live</h1>

#</body>
#</html>
#"""

#print(html)

#os.system("python stream.py")
