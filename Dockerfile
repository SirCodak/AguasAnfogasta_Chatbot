# Usa una imagen base oficial de Python
FROM python:3.13.2

# Establece el directorio de trabajo en la imagen de Docker
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor de Docker
COPY . /app

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 3978

# Define el comando para ejecutar tu aplicación
CMD ["python", "app.py"]
