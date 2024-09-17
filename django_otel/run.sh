export DJANGO_SETTINGS_MODULE=django_otel.settings
export OTEL_SERVICE_NAME=django-sample-otel
opentelemetry-instrument python manage.py runserver --noreload