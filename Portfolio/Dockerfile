FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install django-admin

# Make migrations and apply them during container build
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --no-input

# Create superuser using environment variables
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '', '$DJANGO_SUPERUSER_PASSWORD')" \
    | python manage.py shell

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "Portfolio.wsgi:application"]

