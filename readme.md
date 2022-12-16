# Мой тг бот средней паршивости для управления домашним сервачком 

Данный pet-project не претендует на секьюрность и правильность исполнения, но да и ладно :)

---

Что умеет:
- Добавлять торренты в watch dir transmission'а
- Перезагружать и выключать хост
- Создавать и убивать SSH-туннель

---

Переменные, которые стоит указать что бы это все завелось:
- `ALLOWED_USER_ID_LIST` в `constants.py` - список ID telegram пользователей, которые могут пользоваться ботом, проверка выполняется в `authentication.py` для каждого действия.

Переменные среды:
- `TELEGRAM_API_TOKEN` - токен Telegram
- `NGROK_TOKEN` - токен Ngrok'а
- `TORRENT_FILES_DIR` - директория, куда скачиваются .torrent файлы для скачивания в Transmission
- `LOGS_DIR` - директория, где будут храниться логи

---

Для демонизации можно использовать systemd. Для этого поместите `telegram_bot.service` в `/etc/systemd/system/`, предварительно вставив туда свои токены и пути к директориям, после выполните:

```
systemctl daemon-reload
systemctl enable telegram_bot.service
systemctl start telegram_bot
```

