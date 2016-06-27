# This is my code
import requests

class blah (object):
    """
    blah blah
    """
    BASE_URL = 'https://myurl.com/api/v1'

    def __init__(self, token, base_url=BASE_URL):
        self.token = token
        self.base_url = base_url
        self.session = session = requests.session()
        session.headers.update(
            {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(self.token)})
