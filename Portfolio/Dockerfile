FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install django-admin

# Make migrations and apply them during container build
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --no-input

# Set up environment variables
ENV DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "Portfolio.wsgi:application"]

