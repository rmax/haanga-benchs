<?
include('init.php');

$title = "Cabecera menéame";
$globals = array();
$globals['favicon'] = "icon.jpg";
$globals['noindex'] = True;
$globals['tags'] = 'test1, test2';
$globals['description'] = 'Pruebas de descripción';
$globals['server_name'] = 'www.meneame.net';
$globals['base_url'] = '/';


$globals['base_static'] = 'http://static.meneame.net';
$globals['js_main'] = 'general01.php';
$globals['security_key'] = 'xxxxxxxxxxxxxxxxxxxxxxx';


$globals['thumbnail'] = 'void.jpg';
$globals['thumbnail_logo'] = 'void.jpg';
$globals['extra_head'] = '';
$globals['extra_js'] = array('void.js', 'void1.js');
$globals['q'] = 'q=aslkdlñak ñlsakd ñlaks&kasjlkadjlajsdljkl';
$globals['lang'] = 'es';
$globals['css_main'] = 'main.css';
$globals['css_color'] = 'main.css';


Haanga::Load('header.html', compact('globals', 'title'));
Haanga::Load('header.html', compact('globals', 'title'));
Haanga::Load('header.html', compact('globals', 'title'));
?>
