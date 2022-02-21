from bs4 import BeautifulSoup
from flask import Blueprint, request, jsonify
from ..consts import *
from ..classes import *

import requests

readmanganato_endpoint = Blueprint('readmanganato', __name__)

class Readmanganato():
    def __init__(self, Url):
        self.Url = Url

    def GetData(self) -> dict:
        MangaData = {}

        try:
            # Fetch Data from URL
            self.Response = requests.get(self.Url, headers=Site.HEADERS)

            # Set Manga Site And Link
            MangaData[Label.MANGA_LINK] = self.Url

            full_manga_content = BeautifulSoup(self.Response.content, 'html.parser')

            UpperInfo = full_manga_content.find("table", {"class":"variations-tableInfo"}).find("tbody")
            LowerInfo = full_manga_content.find("div", {"class":"story-info-right-extent"})
            Chapters_Container = full_manga_content.find("ul", {"class":"row-content-chapter"})

            # Get Manga Name
            Name = full_manga_content.find("div", {"class":"story-info-right"}).find("h1").get_text()
            MangaData[Label.MANGA_NAME] = Name

            # Get Manga Authors
            AuthorList = []
            Authors = UpperInfo.find_all("tr")[1].find("td", {"class":"table-value"}).find_all("a")
            for author in Authors:
                AuthorList.append(author.get_text())
            MangaData[Label.MANGA_AUTHORS] = AuthorList

            # Get Last Updated
            Last_Updated = LowerInfo.find_all("p")[0].find("span", {"class":"stre-value"}).get_text()
            MangaData[Label.SFW.MANGA_LAST_UPDATED] = Last_Updated

            # Get Genres
            GenreList = []
            Genres = UpperInfo.find_all("tr")[3].find("td", {"class":"table-value"}).find_all("a")
            for genre in Genres:
                GenreList.append(genre.get_text())
            MangaData[Label.MANGA_GENRES] = GenreList

            # Get Pic Link
            Pic_Link = full_manga_content.find("div", {"class":"story-info-left"}).find("span", {"class":"info-image"}).find("img")["src"]
            MangaData[Label.MANGA_PIC_LINK] = Pic_Link

            # Get Desc
            Desc = "".join(full_manga_content.find("div", {"class": "panel-story-info-description"}).findAll(text=True, recursive=False)).strip()
            MangaData[Label.SFW.MANGA_DESC] = Desc

            # Get Total Chapter Count
            Total_Chapter_Count = len(Chapters_Container.find_all("li", {"class":"a-h"}))
            MangaData[Label.SFW.MANGA_TOTAL_CHAPTER_COUNT] = Total_Chapter_Count

            # Get Latest Chapter Name     
            Latest_Chapter_Name = Chapters_Container.find_all("li", {"class":"a-h"})[0].find("a").get_text()
            MangaData[Label.SFW.MANGA_LATEST_CHAPTER_NAME] = Latest_Chapter_Name
        
        except:
            return None

        return MangaData

@readmanganato_endpoint.route('/', methods = ['GET'])
def index():
    RawMangaLink = request.args.get('MangaLink', type=str)

    if RawMangaLink is None:
        return jsonify(Response=Response('failed', 'missing "/MangaLink"/ parameter', {}).GetData()), 400

    MangaData = Readmanganato(RawMangaLink).GetData()

    if MangaData is None:
        return jsonify(Response=Response('failed', 'invalid "/MangaLink"/ parameter', {}).GetData()), 400

    return jsonify(Response=Response('success', '', MangaData).GetData()), 200