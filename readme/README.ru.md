[中文](../README.zh-CN.md) [English](README.en.md) [日本語](README.ja.md) [Deutsch](README.de.md) [Français](README.fr.md) [Português](README.pt-BR.md)

# Инструмент поиска IP-информации

![Скриншот](../screen/screen1.jpg)

## test website

[https://ip.fantacy.online/](https://ip.fantacy.online/)

## Основные функции
- Поиск геоданных IP-адресов в реальном времени
- Определение страны/региона/города/провайдера
- Поддержка многоязычия (русский/английский/китайский/японский/немецкий/французский/португальский)
- Простой RESTful API

## Технологии
- Python 3.8+
- Flask Framework
- Источник данных ip-api.com
# Развертывание

1. Установите зависимости
```bash
pip install -r requirements.txt
```

2. Запуск сервера
   
```bash
python server.py
```
3. Откройте http://localhost:5000 в браузере
   
## API документация
```
GET /api/ip-info?ip=[target_ip]&lang=[language_code]
```

# Поддерживаемые языки
| Код языка | Язык |
|-----------|------------|
| zh-CN | Китайский |
| en | Английский |
| ja | Japanese |
| ru | Russian |
| de | German |
| fr | French |
| pt-BR | Portuguese |