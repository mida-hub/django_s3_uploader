# django_s3_uploader
cf. https://qiita.com/nokonoko_1203/items/242367a83c313a5e46bf

# setup
```
cd app
pipenv shell
pipenv install
django-admin startproject config .
python manage.py migrate
python manage.py runserver
```

localhost:8000 にアクセスして確認する

# docker-compose
```
docker-compose up -d --build
```

# migrate
```
docker-compose exec django python manage.py migrate --noinput
```

# entrypoint
```
chmod +x app/entrypoint.sh
```

# 本番
```
chmod +x app/entrypoint.prod.sh

docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec django python manage.py makemigrations --noinput
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear
```

# ec2 systemdの参考
https://qiita.com/kanga/items/5f956bc47068c9774522
