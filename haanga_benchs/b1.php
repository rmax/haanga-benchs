<?
include('init.php');

for ($i = 0; $i < 100; $i++) {
	printf('<p>La hora (%d) en epochs es: %d</p>', $i, time());
}
?>
