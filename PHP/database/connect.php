<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>数据库连接</title>
</head>

<body bgcolor="#FFCC99">

<?php 
	header("Content-type:text/html;charset=utf-8");
	
	$link = @mysql_connect("localhost", "roger", "roger");
	if (!$link) // 若连接失败，则显示相应信息并终止程序运行
	{
			echo "连接失败！<br>";
			echo "错误编号：".mysql_errno()."<br>";
			echo "错误信息：".mysql_errno()."<br>";
			die();  // 终止程序运行
	}
?>
	<h2 align="left">数据库连接成功!<br></h2>
<?php 
	mysql_select_db("roger_db", $link);  // 选择系统数据库roger_db
	if(mysql_errno()) {
		echo "数据库选择失败！<br>";
		die();
	}
?>	

	<h3 align="left">数据库选择成功!<br></h3>
<?php 
	function getSport(){
		$Sport="";
		for ($i=0;$i<count($_POST["sport"]);$i++){
			$Sport .= $_POST["sport"][$i]." ";
		}
		return $Sport;
	}
	$str1 = $_POST["name"];
	$str2 = $_POST["password"];
	$str3 = $_POST["suggestion"];
	$str4 = $_POST["fruit"];
	$str5 = getSport();
	$str6 = $_POST["city"];
	
	$sql="insert into costomer (username, password, suggestion, fruit, sport, city) values('$str1', '$str2', '$str3', '$str4', '$str5', '$str6')";
	
//	$sql="insert into costomer (username, password, suggestion, fruit, sport, city) values ('$str1', '$str2', '$str3', '$str4', '$str5', '$str6')";
	 
	$inser = mysql_query($sql, $link); // or die("数据插入失败！<br>");
	if(!$inser) {
		echo "连接失败！<br>";
		echo "错误编号：".mysql_errno()."<br>";
		echo "错误信息".mysql_error()."<br>";
		die("数据插入失败！<br>");
	}
	
	mysql_close($link);
?>	
	<h4 align="left">数据添加成功！<br></h4>
    
	<font size="+1">
	<table width=20% height=10% border="1" >	
	<tr bordercolor="#000033">
		<td valign="center" width="200" height="40" align="right">姓名:</td>
		<td valign="center" width="400" height="30" align="left"> <?php  echo $_POST["name"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000033">
		<td valign="center" width="200" height="40" align="right">密码:</td>
		<td valign="center" width="400" height="30" align="left"> <?php  echo $_POST["password"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000099">
		<td valign="center" width="200" height="40" align="right">建议:</td>
		<td valign="center" width="400" height="20" align="left"> <?php  echo $_POST["suggestion"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000099">
		<td valign="center" width="200" height="40" align="right">水果:</td>
		<td valign="center" width="400" height="20" align="left"> <?php  echo $_POST["fruit"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000099">
		<td valign="center" width="200" height="40" align="right">运动:</td>
		<td valign="center" width="400" height="20" align="left"> <?php  echo getSport(); ?> </td>
	</tr>
	
	<tr bordercolor="#000099">
		<td valign="center" width="200" height="40" align="right">城市:</td>
		<td valign="center" width="400" height="20" align="left"> <?php  echo $_POST["city"]; ?> </td>
	</tr>
	</table>
	</font>
	


</body>
</html>
