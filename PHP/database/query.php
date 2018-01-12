<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>信息检索</title>
</head>

<body>
<?php
	$link = @mysqli_connect("localhost", "roger", "roger");
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
	@mysqli_select_db($link, "roger_db");  // 选择系统数据库roger_db
	if(@mysqli_errno()) {
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
//	$name = trim($_POST["number"]);
	$name = $_POST["number"];
//	echo $name;
	
	$sql="select * from costomer where username = '$name'";          /* where username = '$name' */
//	$sql="insert into costomer (username, password, suggestion, fruit, sport, city) values ('$str1', '$str2', '$str3', '$str4', '$str5', '$str6')";
	 
	$result = @mysqli_query($link, $sql) or die("信息检索失败！");
?>	

	<h4 align="left">数据查询成功！<br></h4>
    
<?php	
	$rows = @mysqli_num_rows($result);
	if ($rows == 0){
		die("未找到".$name."的相关信息！");
	}
	$row = @mysqli_fetch_array($result);
//	echo $rows;
?>	
	<table width=20% height=10% border="1" >	
	<tr bordercolor="#000033">
		<td valign="center" width="200" height="40" align="right">姓名:</td>
		<td valign="center" width="400" height="30" align="left"> <?php  echo $row["username"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000033">
		<td valign="center" width="200" height="40" align="right">密码:</td>
		<td valign="center" width="400" height="30" align="left"> <?php  echo $row["password"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000099">
		<td valign="center" width="200" height="40" align="right">建议:</td>
		<td valign="center" width="400" height="20" align="left"> <?php  echo $row["suggestion"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000099">
		<td valign="center" width="200" height="40" align="right">水果:</td>
		<td valign="center" width="400" height="20" align="left"> <?php  echo $row["fruit"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000099">
		<td valign="center" width="200" height="40" align="right">运动:</td>
		<td valign="center" width="400" height="20" align="left"> <?php  echo $row["sport"]; ?> </td>
	</tr>
	
	<tr bordercolor="#000099">
		<td valign="center" width="200" height="40" align="right">城市:</td>
		<td valign="center" width="400" height="20" align="left"> <?php  echo $row["city"]; ?> </td>
	</tr>
	</table>
    
    
</body>
</html>
