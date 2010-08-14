<?
include('init.php');
$h2o = new h2o('templates/b1_tpl.html');
$objects = array();
for ($i = 0; $i < 100; $i++) {
	$epoch = time();
	echo $h2o->render(compact('i', 'epoch'));
}

?>
