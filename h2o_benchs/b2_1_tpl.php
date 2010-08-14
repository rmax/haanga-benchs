<?
include('init.php');

$h2o = new h2o('templates/b2_filters_tpl.html');
$objects = array();
for ($i = 0; $i < 100; $i++) {
	$o = new stdClass();
	$o->i = $i;
	$o->epoch = (int) time();
	array_push($objects, $o);
}
echo $h2o->render(compact('objects'));
?>
