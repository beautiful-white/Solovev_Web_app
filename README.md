# Дырявая вебапка

## Запуск через Docker

​```bash
docker build -t web-vuln .
docker run -d -p 5000:5000 --name web-vuln web-vuln
​```

## Доступ

- Регистрация: http://localhost:5000/register
- Авторизация: http://localhost:5000/login
- Приветствие: http://localhost:5000/hello