[中文](README.zh-CN.md) [日本語](readme/README.ja.md) [Русский](readme/README.ru.md) [Deutsch](readme/README.de.md) [Français](readme/README.fr.md) [Português](readme/README.pt-BR.md)

# IP Geolocation Tool

![Screenshot](screen/screen1.jpg)

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