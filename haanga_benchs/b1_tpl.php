<?
include('init.php');
$objects = array();
for ($i = 0; $i < 100; $i++) {
	$epoch = time();
	Haanga::Load('b1_tpl.html', compact('i', 'epoch'));
}

?>
