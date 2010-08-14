1. instala easy_install si no lo tienes ya
2. sudo easy_install pip
3. pip install -r requirements.txt


Para ejecutar el servidor con 1 solo thread:

python manage.py run_unicorn -w 1 

Puedes jugar con el número de workers, poner gunicorn en modo daemon etc, etc.
