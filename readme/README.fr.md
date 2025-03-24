[中文](../README.zh-CN.md) [English](README.en.md) [日本語](README.ja.md) [Русский](README.ru.md) [Deutsch](README.de.md) [Português](README.pt-BR.md)

# Outil de recherche d'information IP

![Capture d'écran](../screen/screen1.jpg)

## test website

[https://ip.fantacy.online/](https://ip.fantacy.online/)

## Fonctionnalités principales
- Géolocalisation IP en temps réel
- Détection du pays/région/ville/fournisseur
- Support multilingue (Français/Anglais/Chinois/Japonais/Russe/Allemand/Portugais)
- API RESTful simple

## Technologies
- Python 3.8+
- Framework Web Flask
- Source de données ip-api.com

## Installation
1. Installer les dépendances
```bash
pip install -r requirements.txt
```

2. Démarrer le serveur
```bash
python server.py
```

3. Accéder à http://localhost:5000 dans le navigateur

## Documentation API
```
GET /api/ip-info?ip=[IP-cible]&lang=[code-langue]
```

## Langues supportées
| Fichier langue | Langue |
|---------|---------|
| fr | Français |
| en | Anglais |
| zh-CN | Chinois simplifié |
| ja | Japonais |
| ru | Russe |
| de | Allemand |
| pt-BR | Portugais |