<?php
if(!isset($_POST['pwd']) || md5($_POST['pwd'])!='ae4dcdd9fcc80ee9b87eb224239b5319') die('Wrong!');//pwd: j4bgsn
  $db = sqlite3_open("htdocs\ppxy\ctfflag.db");
  $cc=30;
  if(isset($_GET['p']))
	 $cc=(int)$_GET['p'];
  $query = sqlite3_query($db, "select distinct flagc,ipaddr from flagx order by dtime desc"." limit $cc");//dtime,remark
  if (!$query) die (sqlite3_error($db));
  echo "<table ><tr><td width=200>time</td><td width=200>IPaddr</td><td width=400>flags</td><td width=50>remark</td>";
 while ( ($row = sqlite3_fetch_array($query)))
{
	$query1 = sqlite3_query($db, "select flagc,ipaddr,dtime,remark from flagx where ipaddr='".$row['ipaddr']."' and flagc='".$row['flagc']."' order by dtime desc limit 1");
	if(($row1 = sqlite3_fetch_array($query1)))
	echo "<tr><td>",$row1['dtime'],"</td><td>",$row1['ipaddr'],'</td><td>',$row1['flagc'],"</td><td>",$row1['remark'],"</td></tr>\n";
	sqlite3_query_close($query1);
}
echo "</table>";
sqlite3_query_close($query);
sqlite3_close($db);
?>