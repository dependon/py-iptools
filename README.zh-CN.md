[English](readme/README.en.md) [日本語](readme/README.ja.md) [Русский](readme/README.ru.md) [Deutsch](readme/README.de.md) [Français](readme/README.fr.md) [Português](readme/README.pt-BR.md)

# IP归属地查询工具

![截图示例](screen/screen1.jpg)

## 功能特性
- 实时查询IP地址地理信息
- 支持国家、地区、城市和ISP查询
- 多语言自动适配（中文/英文/日文/俄文/德文/法文/葡萄牙语）
- 简洁的RESTful API接口

## 技术栈
- Python 3.8+
- Flask Web框架
- ip-api.com数据源

## 部署步骤
1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 启动服务
```bash
python server.py
```

3. 浏览器访问 http://localhost:5000

## 接口文档
```
GET /api/ip-info?ip=[目标IP]&lang=[语言代码]
```

## 多语言支持
| 语言文件 | 对应语言 |
|---------|---------|
| zh-CN | 简体中文 |
| en | 英语 |
| ja | 日语 |
| ru | 俄语 |
| de | 德语 |
| fr | 法语 |
| pt-BR | 葡萄牙语 |