[中文](../README.zh-CN.md) [English](README.en.md) [日本語](README.ja.md) [Русский](README.ru.md) [Français](README.fr.md) [Português](README.pt-BR.md)

# IP-Abfragewerkzeug

![Screenshot](../screen/screen1.jpg)

## test website

[https://ip.fantacy.online/](https://ip.fantacy.online/)

## Hauptfunktionen
- Echtzeit-IP-Geolokalisierung
- Ermittlung von Land/Region/Stadt/Provider
- Mehrsprachenunterstützung (Deutsch/Englisch/Chinesisch/Japanisch/Russisch/Französisch/Portugiesisch)
- Einfache RESTful API


## Technologien
- Python 3.8+
- Flask Web Framework
- ip-api.com Datenquelle

## Installation
1. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

2. Server starten
```bash
python server.py
```

3. Im Browser öffnen: http://localhost:5000

## API Dokumentation
```
GET /api/ip-info?ip=[Ziel-IP]&lang=[Sprachcode]
```

## Unterstützte Sprachen
| Sprachdatei | Sprache |
|---------|---------|
| de | Deutsch |
| en | Englisch |
| zh-CN | Vereinfachtes Chinesisch |
| ja | Japanisch |
| ru | Russisch |
| fr | Französisch |
| pt-BR | Portugiesisch |