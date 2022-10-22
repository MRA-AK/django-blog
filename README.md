# Django Blog
Class based view django blog website.
Based on https://github.com/AliBigdeli/mysite project.

## How To Use
1. Install docker and docker compose.
2. Clone the repository.
3. Run the docker compose: `docker-compose -f docker-compose-production.yml up -d --build` 
4. Create database: `docker exec backend python manage.py migrate`
5. Open your browser and go to http://localhost:8000/.

## API
Blog endpoints: http://localhost:8000/blog/api/v1/

#### API Docs:
- DRF built-in documentation: http://localhost:8000/drf-docs/
- Swagger documentation: http://localhost:8000/swagger/
- Redoc documentation: http://localhost:8000/redoc/
- Export swagger in json format: http://localhost:8000/swagger/output.json/

## Celery Beat
The celery beat creates a new post automatically every 10 minutes.

## Create dummy data
For creating five dummy posts:
run `docker-compose exec backend sh -c "python manage.py insert_data"`

## Run tests
For running pytest:
run `docker-compose exec backend sh -c "pytest ."`
