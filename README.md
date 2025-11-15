# Как запустить проект

## 1. Создать виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate   # Linux/Mac

## 2. Установить зависимости
pip install -r requirements.txt

## 3. Настроить переменные окружения
Создать файл `.env` и заполнить нужные настройки.

## 4. Запустить миграции
aerich init -t src.core.settings.TEST_TORTOISE_ORM  
aerich migrate
aerich upgrade

## 5. Запустить сервер
uvicorn main:app --reload

# Запуск проекта в докере

docker-compose up --build -d

#  Доступные маршруты API
Для начала необходимо зайти в сваггер вставить в адресную строку http://127.0.0.1:8000/docs
### Users (`/users`)

| Метод | URL | Описание |
|-------|------|----------|
| POST | `/users/auth/register` | Регистрация пользователя |
| POST | `/users/auth/login` | Авторизация пользователя |

### Notifications (`/notifications`)

| Метод | URL | Описание |
|-------|------|----------|
| POST | `/notifications/` | Создать уведомление |
| GET  | `/notifications/` | Получить список уведомлений (limit, offset) |
| DELETE | `/notifications/{notification_id}` | Удалить уведомление |

## 7. Запсук тестов в консоль необходимо ввести следующее
pytest .
