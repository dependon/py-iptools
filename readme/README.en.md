[中文](../README.zh-CN.md) [日本語](README.ja.md) [Русский](README.ru.md) [Deutsch](README.de.md) [Français](README.fr.md) [Português](README.pt-BR.md)

# IP Geolocation Tool

![Screenshot](../screen/screen1.jpg)

## test website

[https://ip.fantacy.online/](https://ip.fantacy.online/)

## Features
- Real-time IP geolocation lookup
- Country/Region/City/ISP information
- Multi-language support (English/Chinese/Japanese/Russian/German/French/Portuguese)
- RESTful API interface

## Technology Stack
- Python 3.8+
- Flask Framework
- ip-api.com data source

## Deployment
1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Start server
```bash
python server.py
```

3. Open http://localhost:5000 in browser

## API Documentation
```
GET /api/ip-info?ip=[target_ip]&lang=[language_code]
```

## Supported Languages
| Language Code | Language |
|--------------|----------|
| zh-CN | Chinese |
| en | English |
| ja | Japanese |
| ru | Russian |
| de | German |
| fr | French |
| pt-BR | Portuguese |