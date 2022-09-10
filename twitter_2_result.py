import cgi
from choices_functions import *

form = cgi.FieldStorage()

account_address = form.getvalue('account_address')
num_tweets  = form.getvalue('num_tweets')

funct_choice_2(account_address, int(num_tweets))

print("Content-type: text/html; charset=utf-8\n")

html = """
<!doctype html>
<html lang="fr">

<head>
	<meta charset="utf-8"/>
	<title>COVID-19 Data Extractor</title>
	<link rel="icon" href="src/corona.png">
	<style>
		*
		{
				margin:0px;
				padding:0px;
		}
		body{
				background-color:#334d66;
				font:14px tahoma;
		}
		#main_section div img{
				width:90px;
				height:90px;
		}
		#w_section img{
				width:90px;
				height:90px;
		}
		#top_header,#main_footer{
				background-color:#333366;
				color:#fff;	
				text-align:center;
				margin:5px;	
				border:1px solid black;	
				border-radius:5px;	
		}
		#main_wrapper{
				background-color:#fff;
				border:2px solid black;
				width:65%;		
				margin:50px auto;
				text-align:center;
		}
		#main_footer{
				font-weight:bold;
		}
		#main_section div{
				display:inline-block;
				background-color:#714939;
				margin:6px;
				border:1px solid black;
				border-radius:8px;
				padding:10px;
				text-align:center;
				width:14%;
				height:120px;
				vertical-align:top;
		}
		#main_section div h1 a{
				font:bold 14px tahoma;
				color:white;
		}
		#t_section div{
				display:inline-block;
				background-color:#714939;
				margin:6px;
				border:1px solid black;
				border-radius:80px;
				padding:10px;
				text-align:center;
				width:40%;
				height:40px;
				vertical-align:top;
		}
		#t_section div h1 a{
				font:bold 20px tahoma;
				color:white;
		}
	</style>
</head>

<body>
	<div id="main_wrapper">
		<header id="top_header">
			<h1>Twitter COVID-19 Data Extractor</h1>
		</header>
		<section id="w_section">
			<br>
			<h1>Twitter Extractor</h1>
			<br>
			<h1>A specific user's tweets extractor</h1>
			<br>
			<h2>The CSV file is ready</h2>
			<br>
			<h2>Please click on the file bellow to download it</h2>
			<br>
			<p>Donc forget to save it as a .csv file</p>
			<br>
			<p><a href="Results/export_dataframe_user.csv" download="export_dataframe_user.csv"><img src="src/csv.png" alt="Twitter Scraper"/></a></p>
			<br>
		</section>
	</div>
</body>

</html>
"""

print(html)