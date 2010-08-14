<?
include('init.php');

$objects = array();
for ($i = 0; $i < 100; $i++) {
	$o = new stdClass();
	$o->i = $i;
	$o->epoch = (int) time();
	array_push($objects, $o);
}
Haanga::Load('b2_filters_tpl.html', compact('objects'));
?>
