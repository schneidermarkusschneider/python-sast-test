class WebhookProcessor:
    def extract_source_urls(self, config):
        if 'sources' in config:
            return config['sources']
        return [config.get('url', '')]
