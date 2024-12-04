# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar herramientas necesarias y librerías de sistema para MySQL
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    libssl-dev \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir django==5.1.2
RUN pip install --no-cache-dir djangorestframework
RUN pip install --no-cache-dir django-cors-headers
RUN pip install --no-cache-dir djangorestframework-simplejwt
RUN pip install --no-cache-dir mysql-connector-python
RUN pip install --no-cache-dir whitenoise

# Crear directorio para archivos estáticos
RUN mkdir staticfiles

# Recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
