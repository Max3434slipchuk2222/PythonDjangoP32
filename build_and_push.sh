#!/bin/bash

# Зупиняємо скрипт, якщо виникне помилка
set -e

echo "==== Починаємо збірку API ===="
# Переходимо в папку з API
cd djangoapi/postapi
docker build -t django-api-p32 .
docker tag django-api-p32:latest maxslipchuk22/django-api-p32:latest
docker push maxslipchuk22/django-api-p32:latest

echo "==== Починаємо збірку WEB (Frontend) ===="
# Повертаємося на два рівні назад і йдемо у фронтенд
cd ../../post-project
docker build -t my-post --build-arg VITE_API_BASE_URL=http://172.30.133.106:4512 .
docker tag my-post:latest maxslipchuk22/my-post:latest
docker push maxslipchuk22/my-post:latest

echo "УСЕ ГОТОВО (DONE)!"