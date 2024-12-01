# Usa una imagen oficial de Python como base
FROM python:3.12-slim

# Instala las herramientas y dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias de Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Establece las variables de entorno
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ova_api.settings
ENV PORT=8000

# Recolecta los archivos estáticos y aplica las migraciones
RUN python manage.py collectstatic --noinput && python manage.py migrate

# Expone el puerto configurado
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "ova_api.wsgi:application"]
