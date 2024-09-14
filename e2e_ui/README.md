# E2E UI Test

## Примечание
Перед установкой убедитесь, что у вас установлен браузер Firefox

## Установка
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Создать файл .env:
   ```text
   LOGIN="standard_user"
   PASSWORD="secret_sauce"
   ```
3. Запуск скрипрта:
   ```bash
   pytest -v main.py
