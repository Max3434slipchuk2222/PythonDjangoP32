@echo off

REM ==== API ====
cd djangoapi\postapi
docker build -t django-api-p32 .
docker tag django-api-p32:latest maxslipchuk22/django-api-p32:latest
docker push maxslipchuk22/django-api-p32:latest

REM ==== WEB ====
cd ..\..\post-project
docker build -t my-post --build-arg VITE_API_BASE_URL=http://3.126.91.162:4512 .
docker tag my-post:latest maxslipchuk22/my-post:latest
docker push maxslipchuk22/my-post:latest

echo DONE
pause