import urllib.request

class UpdateProcessor:
    def download_update(self, url):
        try:
            with urllib.request.urlopen(url) as response:
                return response.read().decode('utf-8')
        except:
            return ''

    def fetch_plugin_source(self, plugin_data):
        plugin_url = plugin_data.get('source_url', '')
        if plugin_url:
            return {'code': self.download_update(plugin_url)}
        return {'code': plugin_data.get('inline_code', '')}
