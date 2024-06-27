set app=
python manage.py makemigrations %app% && python manage.py migrate %app%
pause