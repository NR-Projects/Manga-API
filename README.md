# Manga API

Visit API on ✨ https://manga-api-qz6t.onrender.com/ ✨


## Description

A Manga, Manhwa (+ the Darksides) API to fetch common information related to the requested manga


## Dependencies

- Python3
- Flask


## Installation

> Download Repository

```
git clone <url> or download from github
```

> Install all dependencies

```
pip3 install -r requirements.txt
```

> Run from command prompt
```
flask run
```

## Paths and Response Objects

> Current Functional Paths are
- sfw/mangakakalot
- sfw/readmanganato
- nsfw/nhentai

<br>

Response object Format

For a successful request:
> {
    "Status":"success",
    "Data":{<MANGA_DATA HERE>}
}

For a failed request:
> {
    "Status":"failed",
    "Description":"<ERROR DESCRIPTION>",
    "Data":{}
}


## Examples

1. Add Path to the url to specify site to find manga
2. Always Include ```MangaLink``` as parameter

```
https://manga-api-qz6t.onrender.com/sfw/mangakakalot/?MangaLink=https://mangakakalot.com/manga/pq935703
```

Should have a response of

```
{
  "Response": {
    "Data": {
      "Manga_Authors": [
        "触岛漫画"
      ],
      "Manga_Desc": "Five years ago, the online game “Star Brilliance” unexpectedly manifested into reality. Ye Chen, the only surviving beta-test player, tragically met his end due to his own naivety and folly. However, perhaps favored by destiny, on the brink of death, he found himself transported back to a time before “Star Brilliance” descended upon the world. In this life, he is determined to rectify all the mistakes he made in his past life, vowing never to repeat them. Even if it means standing against the world itself!",
      "Manga_Genres": [
        "Action",
        "Fantasy"
      ],
      "Manga_Last_Updated": "May-12-2024 12:52:17 PM",
      "Manga_Latest_Chapter_Name": "Chapter 20",
      "Manga_Link": "https://mangakakalot.com/manga/pq935703",
      "Manga_Name": "Resurgence of The Solo Beta Player",
      "Manga_Pic_Link": "https://avt.mkklcdnv6temp.com/35/w/31-1695617588.jpg",
      "Manga_Total_Chapter_Count": 20
    },
    "Status": "success"
  }
}
```

## Support

All application bugs, problems, etc. can be placed on the issues tab.

## Contributing

Pull requests are welcome. For all changes, please open an issue first to discuss what you would like to change.

## License

It may be a good idea to read the license, just in case :)