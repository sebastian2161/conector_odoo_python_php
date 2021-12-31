<?php

// Contains the url to post data
// this is my local server url
// demo is the folder name and
// demo1.php is other file
$url_path = 'https://sebastian2161-ejercicio21-rama-v12-3904709.dev.odoo.com/restfulapi/login2';

// Data is an array of key value pairs
// to be reflected on the site
$data = array('db' => 'sebastian2161-ejercicio21-rama-v12-3904709', 'login' => 'admin', 'password'=> 'admin');

// Method specified whether to GET or
// POST data with the content specified
// by $data variable. 'http' is used
// even in case of 'https'

$options = array(
	'http' => array('header' =>'Content-Type: application/x-www-form-urlencoded', 
	                'method' => 'GET',
					'content' => http_build_query($data))
);

// Create a context stream with
// the specified options
$stream = stream_context_create($options);

// The data is stored in the
// result variable
$result = file_get_contents($url_path, false, $stream);
echo $result;
?>
