# Manga API

Visit API on ✨ https://ts-manga-api.herokuapp.com ✨


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
https://ts-manga-api.herokuapp.com/sfw/mangakakalot?MangaLink=https://mangakakalot.com/read-gj8eg158504836414
```

Should have a response of

```
{"Response":{"Data":{"Manga_Authors":["Ononata Manimani"],"Manga_Desc":"Raul who had defeated the demon king as the strongest hero should have become the savior of the world.\n\nHaving his treasured companions and family killed by power hungry aristocrats, he was executed with false charges brought against him by the princess. Just before his life collapsed, at last his heart fell into darkness.\n\n...I will tear those traitors from limb to limb. Burn them at the stake. Sever them to pieces. Skewer them. I will kill every one of those bastards without mercy and make them taste hell's suffering.....!!!\n\nObtaining the power of darkness, Raul was revived. Sneering, he vowed revenge.\n\n\u201cOh, I\u2019m looking forward to it \u2013 from now I'll bask in their blood as I please.\u201d\n\nSeveral days after the hero's revival in the imperial capital where flowers bloomed in profusion, the parade that would advance towards tragedy began.","Manga_Genres":["Action","Adult","Drama","Fantasy","Seinen","Tragedy"],"Manga_Last_Updated":"Feb-12-2022 08:01:04 AM","Manga_Latest_Chapter_Name":"Chapter 48","Manga_Link":"https://mangakakalot.com/read-gj8eg158504836414","Manga_Name":"Fukushuu o Koinegau Saikyou Yuusha wa, Yami no Chikara de Senmetsu Musou Suru","Manga_Pic_Link":"https://avt.mkklcdnv6temp.com/43/y/17-1583496846.jpg","Manga_Total_Chapter_Count":66},"Status":"success"}}
```

## Support

All application bugs, problems, etc. can be placed on the issues tab.

## Contributing

Pull requests are welcome. For all changes, please open an issue first to discuss what you would like to change.

## License

It may be a good idea to read the license, just in case :)