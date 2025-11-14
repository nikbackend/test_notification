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
