import urllib3
import logging
import json

class Callback:

    response = None

    def __init__(self, payload):
        self.payload = payload

    def execute(self):
        params = self.payload
        try:
            http = urllib3.PoolManager()
            response = http.request(
                params['callType'],
                params['host'],
                body = json.dumps(params['body']).encode('utf-8'),
                headers=params['headers'],
                fields=params['params']
            )
            self.response = response

            if response.status == 200:
                logging.info('HTTP request completed..')
            else:
                logging.error('HTTP request encountered some errors..')

        except urllib3.exceptions.NewConnectionError:
            logging.warn('HTTP request failed to complete..')

    def result(self):
        return self.response.data
