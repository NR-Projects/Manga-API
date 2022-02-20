class Label:
    MANGA_LINK = "Manga_Link"
    MANGA_NAME = "Manga_Name"
    MANGA_AUTHORS = "Manga_Authors"
    MANGA_GENRES = "Manga_Genres"

    class SFW:
        MANGA_DESC = "Manga_Desc"
        MANGA_PIC_LINK = "Manga_Pic_Link"
        MANGA_LAST_UPDATED = "Manga_Last_Updated"
        MANGA_TOTAL_CHAPTER_COUNT = "Manga_Total_Chapter_Count"
        MANGA_LATEST_CHAPTER_NAME = "Manga_Latest_Chapter_Name"

    class NSFW:
        MANGA_PAGES = "Manga_Pages"
        MANGA_PAGE_LINKS = "Manga_Page_Links"
        MANGA_UPLOADED = "Manga_Uploaded"

class Site:
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}