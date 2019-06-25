<?php
/* 根据权限不同，就有不同的加载方式。
有root权限
那麽，这样就简单了，直接写在配置中。
vim php.ini
auto_append_file = “/dir/path/phpwaf.php”
重启Apache或者php-fpm就能生效了。
当然也可以写在 .user.ini 或者 .htaccess 中。
php_value auto_prepend_file “/dir/path/phpwaf.php”

只有user权限
没写系统权限就只能在代码上面下手了，也就是文件包含。
这钟情况又可以用不同的方式包含。
如果是框架型应用，那麽就可以添加在入口文件，例如index.php，
如果不是框架应用，那麽可以在公共配置文件config.php等相关文件中包含。
include('phpwaf.php');
还有一种是替换index.php，也就是讲index.php改名为index2.php，然后讲phpwaf.php改成index.php。
当然还没完，还要在原phpwaf.php中包含原来的index.php。
index.php -> index2.php
phpwaf.php -> index.php
include('index2.php');
*/
    error_reporting(0);
    define('LOG_FILENAME','log.txt');
    function waf()
    {
        if (!function_exists('getallheaders')) {
            function getallheaders() {
                foreach ($_SERVER as $name => $value) {
                    if (substr($name, 0, 5) == 'HTTP_')
                        $headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5)))))] = $value;
                }
                return $headers;
            }
        }
        $get = $_GET;
        $post = $_POST;
        $cookie = $_COOKIE;
        $header = getallheaders();
        $files = $_FILES;
        $ip = $_SERVER["REMOTE_ADDR"];
        $method = $_SERVER['REQUEST_METHOD'];
        $filepath = $_SERVER["SCRIPT_NAME"];
//        $filename  = $_SERVER['PHP_SELF'];  //访问的文件
//$parameter = $_SERVER["QUERY_STRING"];  //查询的字符串
        //rewirte shell which uploaded by others, you can do more
        foreach ($_FILES as $key => $value) {
            $files[$key]['content'] = file_get_contents($_FILES[$key]['tmp_name']);
            file_put_contents($_FILES[$key]['tmp_name'], "virink");
        }
        unset($header['Accept']);//fix a bug
        $input = array("Get"=>$get, "Post"=>$post, "Cookie"=>$cookie, "File"=>$files, "Header"=>$header);
        //deal with
        $pattern = "select|insert|update|delete|and|or|\'|\/\*|\*|\.\.\/|\.\/|union|into|load_file|outfile|dumpfile|sub|hex";
        $pattern .= "|file_put_contents|fwrite|curl|system|eval|assert";
        $pattern .="|passthru|exec|system|chroot|scandir|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore";
        $pattern .="|`|dl|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|assert|pcntl_exec";
//$pattern .= "WVS|sqlmap|nessus|nikto"; // filter scanner
        $vpattern = explode("|",$pattern);
        $bool = false;
        foreach ($input as $k => $v) {
            foreach($vpattern as $value){
                foreach ($v as $kk => $vv) {
                    if (preg_match( "/$value/i", $vv )){
                        $bool = true;
                        logging($input);
                        break;
                    }
                }
                if($bool) break;
            }
            if($bool) break;
        }
    }
    function logging($var){
        file_put_contents(LOG_FILENAME, "\r\n".time()."\r\n".print_r($var, true), FILE_APPEND);
        // die() or unset($_GET) or unset($_POST) or unset($_COOKIE);
    }
    waf();
?>