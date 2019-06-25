<?php
  date_default_timezone_set('PRC');

function request_post($url = '', $param = '',$cookie='',$header=array()) {
        if (empty($url) || empty($param)) {
            return false;
        }      
        $postUrl = $url;
        $curlPost = $param;
        $ch = curl_init();//初始化curl
        curl_setopt($ch, CURLOPT_URL,$postUrl);//抓取指定网页
        curl_setopt($ch, CURLOPT_HEADER, 0);//设置header
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);//要求结果为字符串且输出到屏幕上
		curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)');
        curl_setopt($ch, CURLOPT_POST, 1);//post提交方式
        curl_setopt($ch, CURLOPT_POSTFIELDS, $curlPost);
		if(!empty($cookie)) curl_setopt($ch, CURLOPT_COOKIE, $cookie);
		if(!empty($header)) curl_setopt($ch,CURLOPT_HTTPHEADER,$header);
        $data = curl_exec($ch);//运行curl
        curl_close($ch);    
        return $data;
    }

function request_get($url = '', $cookie='',$header=array()){
	  if (empty($url)) 
            return false;
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)');
	if(!empty($cookie)) curl_setopt($ch, CURLOPT_COOKIE, $cookie);
    if(!empty($header)) curl_setopt($ch,CURLOPT_HTTPHEADER,$header);
    $data = curl_exec($ch);
    curl_close($ch);
	return $data;
}

  $submitFlagurl="";//catch header and set url,header and cookie
  $submitHeader=Array(
  'Content-Type:application/json;charset=utf-8',
  );

  $save_path="flag.txt";  //You can change the filepath of flags ($save_path)
  $db = sqlite3_open("htdocs\ppxy\ctfflag.db");
  $data=$_POST['flag'];
  $data=trim($data);
  $data=str_replace("\n",'',$data);
  $data=addslashes($data);
  $time=date("Y-m-d H:i:s");
  if(preg_match('/(.*):{1,3}(.*)/', $data, $matches, PREG_OFFSET_CAPTURE)) //catch xx.xx.xx.xx:::flag{xxxxxxxxxxxxxx}
  {
   $ip=rtrim($matches[1][0],':');
   $flag=$matches[2][0];
   $count=substr_count($data,":");
   if($count==1) $remark='py';
   else if($count==2) $remark='py(cache)';
   else if($count==3) $remark='cache';
   sqlite3_exec($db, "INSERT INTO flagx (id,ipaddr,dtime,flagc,remark) VALUES (NULL,'$ip','$time','$flag','$remark')");
   file_put_contents($save_path,$time."\t".$data."\n",FILE_APPEND);
  
   echo request_post($submitFlagurl,"key=$flag&iparr=$ip","session=",$submitHeader); //catch header and sendflag
  }

  sqlite3_close($db);

?>