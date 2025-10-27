import urllib.request
import json

class RemoteModel:
    def send_webhook(self, url, payload):
        try:
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
            response = urllib.request.urlopen(req)
            return {'success': True, 'response': response.read().decode('utf-8')[:200]}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def fetch_and_import_data(self, urls, config):
        results = []
        for url in urls:
            try:
                response = urllib.request.urlopen(url)
                content = response.read().decode('utf-8')
                results.append({'url': url, 'data': content[:100]})
            except Exception as e:
                results.append({'url': url, 'error': str(e)})
        return {'imported': results}
