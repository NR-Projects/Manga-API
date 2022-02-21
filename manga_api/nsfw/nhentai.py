from bs4 import BeautifulSoup
from flask import Blueprint, request, jsonify
from ..consts import *
from ..classes import *

import requests

nhentai_endpoint = Blueprint('nhentai', __name__)

class NHentai():
    def __init__(self, Url):
        self.Url = Url
    
    def GetData(self) -> dict:
        MangaData = {}

        try:
            # Fetch Data from URL
            self.Response = requests.get(self.Url)

            MangaData[Label.MANGA_LINK] = self.Url

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

@nhentai_endpoint.route('/', methods=['GET'])
def index():
    RawMangaLink = request.args.get('MangaLink', type=str)

    if RawMangaLink is None:
        return jsonify(Response=Response('failed', 'missing "/MangaLink"/ parameter', {}).GetData()), 400

    MangaData = NHentai(RawMangaLink).GetData()

    if MangaData is None:
        return jsonify(Response=Response('failed', 'invalid "/MangaLink"/ parameter', {}).GetData()), 400

    return jsonify(Response=Response('success', '', MangaData).GetData()), 200
