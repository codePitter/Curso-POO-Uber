<?php
require_once('payment.php');

class CreditCard extends Payment{
    public $entity;
    public $expDate;
    public $cvv;

    public function __construct($id, $entity, $expDate, $cvv) {
        parent::__construct($id);
        $this->entity = $entity;
        $this->expDate = $expDate;
        $this->cvv = $cvv;

    }


}
?>