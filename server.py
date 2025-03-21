from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    country_lang_mapping = {
        'CN': 'zh-CN',
        'JP': 'ja',
        'RU': 'ru',
        'DE': 'de',
        'FR': 'fr',
        'ES': 'es',
        'BR': 'pt-BR'
    }
    lang = 'en'
    
    try:
        response = requests.get(f'http://ip-api.com/json/{client_ip}?fields=countryCode', timeout=3)
        if response.json().get('status') == 'success':
            lang = country_lang_mapping.get(response.json()['countryCode'], 'en')
    except Exception:
        pass
    
    return render_template('index.html', lang=lang)

@app.route('/api/ip-info', methods=['GET'])
def get_ip_info():
    ip_address = request.args.get('ip')
    lang = request.args.get('lang', '')
    
    url = f'http://ip-api.com/json/{ip_address}'
    if lang:
        url += f'?lang={lang}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') == 'fail':
            return jsonify({'error': data.get('message', 'Unknown error')}), 400
            
        return jsonify({
            'country': data.get('country'),
            'regionName': data.get('regionName'),
            'city': data.get('city'),
            'isp': data.get('isp'),
            'query': data.get('query')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)