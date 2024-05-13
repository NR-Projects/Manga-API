from bs4 import BeautifulSoup
from manga_api.manga_interface import MangaInterface
from ..consts import *
from ..response import *


class NHentai(MangaInterface):
    def __init__(self, URL):
        super().__init__(URL)
    
    def GetData(self) -> dict:
        MangaData = {}

        try:
            MangaData[Label.MANGA_LINK] = self.URL

            full_manga_content = BeautifulSoup(self.Response.content, 'html.parser')

            DataContainer = full_manga_content.find('div', {'id':'bigcontainer'})
            DetailsContainer = DataContainer.find('div', {'id':'info'})
            TagsContainer = DetailsContainer.find('section', {'id':'tags'})

            # Get Pic Link
            PicLinkContainer = DataContainer.find('div', {'id':'cover'}).find('a')
            PicLink = PicLinkContainer.find('img')['data-src']
            MangaData[Label.MANGA_PIC_LINK] = PicLink

            # Get Manga Name
            MangaNameContainer = DetailsContainer.find('h1')
            Name = MangaNameContainer.find('span', {'class':'pretty'}).text
            MangaData[Label.MANGA_NAME] = Name

            # Get Other Details
            PageNumber = 'NOT FOUND'
            GenreList = []
            AuthorList = []
            for el in TagsContainer:
                TagField = el.find(text=True, recursive=False).strip()

                if TagField =='Artists:':
                    AuthorList.append(el.find('span').find('a').find('span').text)

                if TagField == 'Tags:':
                    GenreContainer = el.find('span', {'class':'tags'})
                    for GenreInfo in GenreContainer:
                        GenreList.append(GenreInfo.find('span', {'class':'name'}).text.strip())
                
                if TagField == 'Pages:':
                    PagesContainer = el.find('span', {'class':'tags'})
                    PageNumber = PagesContainer.find('span', {'class':'name'}).text.strip()

            MangaData[Label.MANGA_AUTHORS] = AuthorList
            MangaData[Label.MANGA_GENRES] = GenreList
            MangaData[Label.NSFW.MANGA_PAGES] = PageNumber
        except:
            return None

        return MangaData

