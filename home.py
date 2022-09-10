#coding:utf-8
import cgi

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
			<h1>COVID-19 Data Extractor</h1>
		</header>
		
		<section id="main_section">
			<div>
				<h1><a href="worldometers.py"><img src="src/worldometers.jpg" alt="Worldometers Scraper"/>Worldometers</a></h1>
			</div>
			<div>
				<h1><a href="facebook.py"><img src="src/facebook.png" alt="Facebook Scraper"/>Facebook</a></h1>
			</div>
			<div>
				<h1><a href="twitter.py"><img src="src/twitter.png" alt="Twitter Scraper"/>Twitter</a></h1>
			</div>
		</section>
	<footer id="main_footer">
			<p>| Developped By Ahmad MOUDNI, Chaimaa EZZAAM, Bader EL ANSARI, Karim MAJDI, Yassine LAZGHAN |</p>
	</footer>
	</div>
</body>

</html>
"""

print(html)