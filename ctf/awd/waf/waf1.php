<?php

webscan_error();

define('SCAN_GET', true);
define('SCAN_POST', true);
define('SCAN_COOKIES', true);
define('SCAN_REFERER', true);
define('LOG_FILE', '/var/www/html/waf.log');

//get拦截规则
$getfilter = "<[^>]*?=[^>]*?&#[^>]*?>|\\b(alert\\(|confirm\\(|expression\\(|prompt\\()|<[^>]*?\\b(onerror|onmousemove|onload|onclick|onmouseover)\\b[^>]*?>|^\\+\\/v(8|9)|\\b(and|or)\\b\\s*?([\\(\\)'\"\\d]+?=[\\(\\)'\"\\d]+?|[\\(\\)'\"a-zA-Z]+?=[\\(\\)'\"a-zA-Z]+?|>|<|\s+?[\\w]+?\\s+?\\bin\\b\\s*?\(|\\blike\\b\\s+?[\"'])|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";
//post拦截规则
$postfilter = "<[^>]*?=[^>]*?&#[^>]*?>|\\b(alert\\(|confirm\\(|expression\\(|prompt\\()|<[^>]*?\\b(onerror|onmousemove|onload|onclick|onmouseover)\\b[^>]*?>|\\b(and|or)\\b\\s*?([\\(\\)'\"\\d]+?=[\\(\\)'\"\\d]+?|[\\(\\)'\"a-zA-Z]+?=[\\(\\)'\"a-zA-Z]+?|>|<|\s+?[\\w]+?\\s+?\\bin\\b\\s*?\(|\\blike\\b\\s+?[\"'])|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";
//cookie拦截规则
$cookiefilter = "\\b(and|or)\\b\\s*?([\\(\\)'\"\\d]+?=[\\(\\)'\"\\d]+?|[\\(\\)'\"a-zA-Z]+?=[\\(\\)'\"a-zA-Z]+?|>|<|\s+?[\\w]+?\\s+?\\bin\\b\\s*?\(|\\blike\\b\\s+?[\"'])|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";

//referer获取
$webscan_referer = empty($_SERVER['HTTP_REFERER']) ? array() : array('HTTP_REFERER'=>$_SERVER['HTTP_REFERER']);

/**
 *   关闭用户错误提示
 */
function webscan_error() {
  if (ini_get('display_errors')) {
    ini_set('display_errors', '0');
  }
}

/**
 *  日志记录
 */
function webscan_slog($logs) {
$fh = fopen(LOG_FILE, "a");
fwrite($fh, print_r($logs, true));
fclose($fh);
}

/**
 *  参数拆分
 */
function webscan_arr_foreach($arr) {
  static $str;
  if (!is_array($arr)) {
    return $arr;
  }
  foreach ($arr as $key => $val ) {

    if (is_array($val)) {

      webscan_arr_foreach($val);
    } else {

      $str[] = $val;
    }
  }
  return implode($str);
}


/**
 *  防护提示页
 */
function webscan_pape(){
  $pape=<<<HTML
  <html>
  <title>PLease GO Die.</title>
  <body style="margin:0; padding:0">
  <center><font size="50" >注入成功！</font></center>
  <center><img src='data:img/jpg;base64,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
u7HJMQGfaqNWrr/S2v8AaaIFM86ytHnWUJf/2Q=='/>

  </body>
  </html>
HTML;
  echo $pape;
}

/**
 *  攻击检查拦截
 */
function webscan_StopAttack($StrFiltKey,$StrFiltValue,$ArrFiltReq,$method) {
  $StrFiltValue=webscan_arr_foreach($StrFiltValue);
  if (preg_match("/".$ArrFiltReq."/is",$StrFiltValue)==1){
    webscan_slog(array('ip' => $_SERVER["REMOTE_ADDR"],'time'=>strftime("%Y-%m-%d %H:%M:%S"),'page'=>$_SERVER["PHP_SELF"],'method'=>$method,'rdata'=>$StrFiltValue,'user_agent'=>$_SERVER['HTTP_USER_AGENT'],'request_url'=>$_SERVER["REQUEST_URI"]));
    exit(webscan_pape());
  }
  if (preg_match("/".$ArrFiltReq."/is",$StrFiltKey)==1){
    webscan_slog(array('ip' => $_SERVER["REMOTE_ADDR"],'time'=>strftime("%Y-%m-%d %H:%M:%S"),'page'=>$_SERVER["PHP_SELF"],'method'=>$method,'rdata'=>$StrFiltKey,'user_agent'=>$_SERVER['HTTP_USER_AGENT'],'request_url'=>$_SERVER["REQUEST_URI"]));
    exit(webscan_pape());
  }

}

if (SCAN_GET) {
  foreach($_GET as $key=>$value) {
    webscan_StopAttack($key,$value,$getfilter,"GET");
  }
}
if (SCAN_POST) {
  foreach($_POST as $key=>$value) {
    webscan_StopAttack($key,$value,$postfilter,"POST");
  }
}
if (SCAN_COOKIES) {
  foreach($_COOKIE as $key=>$value) {
    webscan_StopAttack($key,$value,$cookiefilter,"COOKIE");
  }
}
if (SCAN_REFERER) {
  foreach($webscan_referer as $key=>$value) {
    webscan_StopAttack($key,$value,$postfilter,"REFERRER");
  }
}
?>