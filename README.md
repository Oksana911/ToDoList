# Планировщик задач

## Приложение для управления персональными и рабочими задачами

### Python 3.10, Django 4.0.1, Postgres, Docker

<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> 

### TO START: 
- Установите зависимости: 
> pip install -r requirements.txt

- Заполните переменные окружения в .env_example
- Разверните БД:
> docker-compose up -d
- Накатите миграции:
> ./manage.py migrate
- Запустите проект:
> ./manage.py runserver 

- Команда для запуска Telegram-бота
> ./manage.py runbot

### Функционал приложения:
- при успешном login пользователь попадает на страницу с категориями (создать, отредактировать, удалить категорию, фильтр по названию)
- страница Целей представляет собой доску, где каждая цель — это карточка на данной доске:
-- доска делится на 3 колонки по статусам (к выполнению, в работе, выполнено)
-- на каждой карточке отображается краткая информация о цели
-- при нажатии на карточку можно посмотреть детали, отредактировать/удалить цель и оставить к ней комментарий
-- есть фильтры по категории, по приоритету, по статусу, по дате дедлайна; есть поиск по названию
- имеется страница просмотра профиля пользователя с возмодностью редактирования информации о пользователе и смены пароля на новый
- в главном меню предусмотрена возможность привязки Telegram-бота 'mytodolist' к аккаунту пользователя посредством верификационного кода, высылаемого ботом новым пользователям
-- функционал бота: 1) в ответ на команду /goals присылает все открытые цели пользователя, 2) с помощью команды /create можно создать цель


