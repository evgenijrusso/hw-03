#  Разное
1. создал папку hw-03
2. python -m venv venv
3. venv\scripts\activate
4. pip install django
5. django-admin startproject project (создание проекта)
6. python manage.py runserver (проверяем работу сервера)
7. python manage.py runserver 8002 (изменил порт). Потом  добавил его в конфигурацию проекта (runserver localhost:8002)
8. добавил в `settings`  приложения: 'django.contrib.sites', 'django.contrib.flatpages'. Изменил `urls` 
9. сделал исходные миграции
10. создал каталоги 'template, static' и добавил их относительный адрес в `settings`
11. python manage.py createsuperuser (admin-1)
12. в этот файл `friends.html` я подключил опцию `Registration required.`  Она уже была. Поэтому не стал подлкючать
FlatPageAdmin(FlatPageAdmin).
Доступ к админке: (admin,1)