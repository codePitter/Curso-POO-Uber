<?php
require_once('payment.php');

class PayPal extends Payment{
    public $refer;
    public $suc;

    public function __construct($id, $refer, $suc) {
        parent::__construct($id);
        $this->refer = $refer;
        $this->suc = $suc;
    }
}
?>