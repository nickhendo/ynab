import json
import requests
import requests_cache


requests_cache.install_cache(cache_name='ynab_cache', backend='sqlite', expire_after=60*60*24)


class APIClient:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.__url = "https://api.youneedabudget.com/v1/"

    def send_get(self, uri):
        return self.__send_request('GET', uri, data=None)

    def send_post(self, uri, data):
        return self.__send_request('POST', uri, data)

    def send_patch(self, uri, data):
        return self.__send_request('PATCH', uri, data)

    def send_put(self, uri, data):
        return self.__send_request('PUT', uri, data)

    def __send_request(self, method, uri, data):
        url = self.__url + uri

        if method == 'POST':
            self.headers['Content-Type'] = 'application/json'
            payload = bytes(json.dumps(data), 'utf-8')
            response = requests.post(url, headers=self.headers, data=payload)
        elif method == 'PATCH':
            self.headers['Content-Type'] = 'application/json'
            payload = bytes(json.dumps(data), 'utf-8')
            response = requests.patch(url, headers=self.headers, data=payload)
        elif method == 'PUT':
            self.headers['Content-Type'] = 'application/json'
            payload = bytes(json.dumps(data), 'utf-8')
            response = requests.put(url, headers=self.headers, data=payload)
        else:
            self.headers['Content-Type'] = 'application/json'
            response = requests.get(url, headers=self.headers)
        try:
            print(f'Rate limit: {response.headers["X-Rate-Limit"]}')
        except KeyError:
            pass
        if response.status_code > 201:
            try:
                error = response.json()
            except:     # response.content not formatted as JSON
                error = str(response.content)
            raise APIError('YNAB API returned HTTP %s (%s) -> %s' % (response.status_code, error, url))
        else:
            try:
                return response.json()["data"]
            except: # Nothing to return
                return response.text()


class APIError(Exception):
    pass
