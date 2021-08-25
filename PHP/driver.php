<?php 
class Driver extends Account{
    public function __construct($name, $docuemnt, $email, $password){   
        parent::__construct($name, $docuemnt, $email, $password);
    }
}

?>