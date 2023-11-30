up:
	docker-compose up

build:
	docker-compose build

down:
	docker-compose down

make migrate:
	docker-compose run --rm django python manage.py migrate

make makemigrations:
	docker-compose run --rm django python manage.py makemigrations

make createsuperuser:
	docker-compose run --rm django python manage.py createsuperuser

make sh:
	docker-compose run --rm django sh
