FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install uv && uv pip install --system flask

COPY app/ ./app/

EXPOSE 5000

CMD ["python", "-m", "flask", "--app", "app:create_app", "run", "--host=0.0.0.0", "--port=5000"]