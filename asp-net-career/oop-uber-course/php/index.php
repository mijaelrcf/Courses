<?php
require_once("car.php");
require_once("uberX.php");
require_once("account.php");

$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Sparl");
$uberX->printDataCar();

?>