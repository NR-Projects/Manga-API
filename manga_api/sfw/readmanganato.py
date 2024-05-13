from bs4 import BeautifulSoup
from manga_api.manga_interface import MangaInterface
from manga_api.consts import *
from manga_api.response import *


class Readmanganato(MangaInterface):
    def __init__(self, URL):
        super().__init__(URL)

    def GetData(self) -> dict:
        MangaData = {}

        try:
            # Set Manga Site And Link
            MangaData[Label.MANGA_LINK] = self.URL

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
    
