[中文](../README.zh-CN.md) [English](README.en.md) [Русский](README.ru.md) [Deutsch](README.de.md) [Français](README.fr.md) [Português](README.pt-BR.md)

# IP情報検索ツール

![スクリーンショット](../screen/screen1.jpg)

## test website

[https://ip.fantacy.online/](https://ip.fantacy.online/)

## 主な機能
- IPアドレスの地理情報リアルタイム検索
- 国・地域・都市・ISP情報の取得
- 多言語自動対応（日本語/英語/中国語/ロシア語/ドイツ語/フランス語/ポルトガル語）
- シンプルなRESTful API

## 技術スタック
- Python 3.8+
- Flask Webフレームワーク
- ip-api.comデータソース

## インストール手順
1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

2. サーバー起動
```bash
python server.py
```

3. ブラウザで http://localhost:5000 にアクセス

## APIドキュメント
```
GET /api/ip-info?ip=[対象IP]&lang=[言語コード]
```

## 対応言語
| 言語ファイル | 対応言語 |
|---------|---------|
| ja | 日本語 |
| zh-CN | 簡体字中国語 |
| en | 英語 |
| ru | ロシア語 |
| de | ドイツ語 |
| fr | フランス語 |
| pt-BR | ポルトガル語 |