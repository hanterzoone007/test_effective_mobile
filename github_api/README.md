# GitHub API Test

## Установка
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Создать файл .env:
   ```text
   GITHUB_USERNAME=your_github_username
   GITHUB_TOKEN=your_github_token
   NAME_REPO='test-repo-123456'
   ```
3. Запуск скрипрта:
   ```bash
   pytest -v test_api.py
   ```
