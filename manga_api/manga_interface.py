import requests
from manga_api.consts import Site


class MangaInterface:
    def __init__(self, URL) -> None:
        self.URL = URL
        pass

    def FetchHtml(self) -> bool:
        # Use requests to fetch data
        response = requests.get(self.URL, headers=Site.HEADERS)
        
        # Check response status
        print(response.status_code)
        if response.status_code == 200:
            self.Response = response.content
            return True
        
        self.Response = None
        return False