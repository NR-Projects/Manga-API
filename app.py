from typing import Tuple
from flask import Flask, jsonify, request

from manga_api.manga_interface import MangaInterface
from manga_api.sfw import mangakakalot, readmanganato
from manga_api.nsfw import nhentai
from manga_api.response import Response


API_CLASS_MAP = {
    "sfw": {
        "mangakakalot": mangakakalot.Mangakakalot,
        "readmanganato": readmanganato.Readmanganato
    },
    "nsfw": {
        "nhentai": nhentai.NHentai
    }
}


app = Flask(__name__)

@app.route("/<manga_type>/<manga_domain>", methods = ["GET"])
def manga_api(manga_type, manga_domain) -> Tuple[str, int]:
    
    manga_interface: MangaInterface = None
    selected_class = None

    # Verify path validity
    try:
        selected_class = API_CLASS_MAP[manga_type][manga_domain]
    except:
        return jsonify(Response=Response("Invalid Path!", None).GetData()), 400

    # Check if required query parameter is present (MangaLink)
    RawMangaLink = request.args.get('MangaLink', type=str)
    if RawMangaLink is None:
        return jsonify(Response=Response("Missing \"MangaLink\" Parameter", {}).GetData()), 400

    # Initialize class
    manga_interface = selected_class(RawMangaLink)
    
    # Start Scraping
    status = manga_interface.FetchHtml()

    if not status:
        return jsonify(Response=Response("Unable to process provided link!", None).GetData()), 400

    res = manga_interface.GetData()

    if res is None:
        return jsonify(Response=Response("Error in collecting content!", None).GetData()), 400
    
    return jsonify(Response=Response("", manga_interface.GetData()).GetData()), 200

if __name__ == '__main__':
    app.run()
