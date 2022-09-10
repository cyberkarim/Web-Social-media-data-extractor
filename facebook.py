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
	<script type="text/javascript" language="javascript">
        function checkform(x)
        {
            var account_address = document.getElementById("account_address");
            var num_pages = document.getElementById("num_pages");
            var cansubmit = true;
            if(account_address.value == "" || num_pages.value == "") cansubmit = false;
            if(x) cansubmit = true;
            document.getElementById('submit').disabled = !cansubmit;
        }
    </script>
</head>

<body>
	<div id="main_wrapper">
		<header id="top_header">
			<h1>Facebook COVID-19 Data Extractor</h1>
		</header>
		<section id="t_section">
            <br>
            <h2>Facebook Extractor</h2>
            <br>
            <h2>A specific user's publications extractor</h2>
            <br>
            <form action="facebook_result.py" method="post" autocomplete="on">
                <fieldset>
                    <legend>Inputs:</legend>
                    <br>
                    <h2>Account's address</h2>
                    <label for="account_address">Enter the account's address (without @):</label>
                    <input type="text" id="account_address" name="account_address" value="WHO" size="30" onKeyup="checkform(0)">
                    <br><br>
                    <h2>The maximum number of pages</h2>
                    <label for="num_pages">Maximum number of publication pages to extract:</label>
                    <input type="number" id="num_pages" name="num_pages" value=1 min="1" onKeyup="checkform(0)" onclick="checkform(0)">
                    <br><br>
                    <h2>Reset</h2><input type="reset" value="Reset" onclick="checkform(1)">
                    <br><br>
                    <h2>Submit</h2><input type="submit" id="submit" value="Submit">
                    <br><br>
                </fieldset>
                <br><br>
            </form>
        </section>
	</div>
</body>

</html>
"""

print(html)