1)Если будет ошибка с бд необходимо прописать в командной строке:
    python manage.py makemigrations myapp     
    python manage.py migrate       
    python manage.py loaddata areas_fixture.json  
    python manage.py loaddata cases_fixture.json  
    python manage.py loaddata clients_fixture.json
2)Суперюзер:
    Login: ivan
    Password: 123123
    PS: Если необходимо создать нового:
        python manage.py createsuperuser
        И далее по инструкции
