FROM python:3.9-slim

# Додаємо файл додатка до робочої директорії контейнера
WORKDIR /app
ADD app.py .

# Встановлюємо залежності в одному шарі
RUN pip install --no-cache-dir flask flask-restful

# Відкриваємо порт для додатка
EXPOSE 5003

# Команда для запуску додатка
CMD ["python", "app.py"]
