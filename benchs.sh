URLS="http://localhost/haanga_benchs/b1.php http://localhost/h2o_benchs/b1.php http://localhost:8000/b1/ http://localhost/haanga_benchs/b1_tpl.php http://localhost/h2o_benchs/b1_tpl.php http://localhost:8000/b1_tpl/ http://localhost/haanga_benchs/b2_tpl.php http://localhost/h2o_benchs/b2_tpl.php http://localhost:8000/b2_tpl/ http://localhost/haanga_benchs/b2_1_tpl.php http://localhost/h2o_benchs/b2_1_tpl.php http://localhost:8000/b2_1_tpl/ http://localhost/haanga_benchs/header.php http://localhost/h2o_benchs/header.php http://localhost:8000/header/"

for url in $URLS
do
	echo $url
	ab -q -S -c 2 -t 30 $url | grep "Requests per second:" | awk '{print "Request/sec: ", $4}'
	echo
done
