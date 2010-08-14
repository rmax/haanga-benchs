<?
include 'Haanga.php';
$config = array(
	'template_dir' => '/home/gallir/benchs/templates',
	//'autoload'	 => FALSE, /* Don't use Haanga's autoloader */
	//'bootstrap'	=> 'haanga_bootstrap',
	'cache_dir' => '/var/tmp',
	'compiler' => array( /* opts for the tpl compiler */
		/* Avoid use if empty($var) */
		'if_empty' => FALSE,
		/* we're smart enought to know when escape :-) */
		'autoescape' => FALSE, 
		/* let's save bandwidth */
		'strip_whitespace' => TRUE, 
		/* call php functions from the template */
		'allow_exec'  => TRUE, 
	),
	'use_hash_filename' => FALSE, /* don't use hash filename for generated php */
);


Haanga::configure($config);

?>
