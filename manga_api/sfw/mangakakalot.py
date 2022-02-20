from bs4 import BeautifulSoup
from flask import Blueprint, request
from ..consts import *

import requests

mangakakalot_endpoint = Blueprint('sfw', __name__)

class Mangakakalot():
    def __init__(self, Response, Url):
        self.Response = Response
        self.Url = Url
    
    def GetData(self) -> dict:
        MangaData = {}

        # Set Manga Link
        MangaData[Label.MANGA_LINK] = self.Url

        full_manga_content = BeautifulSoup(self.Response.content, 'html.parser')

        Infos = full_manga_content.find("ul", {"class":"manga-info-text"}).find_all("li")
        Chapters_Container = full_manga_content.find("div", {"class": "chapter-list"})

        # Get Manga Name
        Name = Infos[0].find('h1').get_text()
        MangaData[Label.MANGA_NAME] = Name

        # Get Manga Authors
        AuthorList = []
        Authors = Infos[1].find_all("a")
        for author in Authors:
            AuthorList.append(author.get_text())
        MangaData[Label.MANGA_AUTHORS] = AuthorList

        # Get Last Updated
        LastUpdated = Infos[3].get_text()[len("Last_Updated : "):]
        MangaData[Label.SFW.MANGA_LAST_UPDATED] = LastUpdated

        # Get Genres
        GenreList = []
        Genres = Infos[6].find_all("a")
        for genre in Genres:
            GenreList.append(genre.get_text())
        MangaData[Label.MANGA_GENRES] = GenreList

        # Get Pic Link
        PicLink = full_manga_content.find("div", {"class": "manga-info-pic"}).find("img")["src"]
        MangaData[Label.SFW.MANGA_PIC_LINK] = PicLink

        # Get Desc
        Desc = "".join(full_manga_content.find("div", {"id": "noidungm"}).findAll(text=True, recursive=False)).strip()
        MangaData[Label.SFW.MANGA_DESC] = Desc

        # Get Total Chapter Count
        TotalChapterCount = len(Chapters_Container.find_all("div", {"class":"row"}))
        MangaData[Label.SFW.MANGA_TOTAL_CHAPTER_COUNT] = TotalChapterCount

        # Get Latest Chapter Name
        LatestChapterName = Chapters_Container.find_all("div", {"class":"row"})[0].find("span").find("a").get_text()
        MangaData[Label.SFW.MANGA_LATEST_CHAPTER_NAME] = LatestChapterName

        return MangaData

@mangakakalot_endpoint.route('/', methods = ['GET'])
def index():
    RawMangaLink = request.args.get('MangaLink')
    IncludeMangaDetails = request.args.get('IncludeMangaDetails')
    ExcludeMangaDetails = request.args.get('ExcludeMangaDetails')