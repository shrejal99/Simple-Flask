import requests


def get_latest_header_images(idx=0, num=5):
    resp = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&n={0}&idx={1}".format(num, idx)).json()
    
    if resp is None:
        return {}

    return {
        "images": [
            {"url": "https://bing.com" + item["url"], "copyright": item["copyright"]} for item in resp["images"]
        ]
    }


def download_to(url, path):
    req = requests.get(url, stream=True)

    with open(path, "wb") as fd:
        for chunk in req.iter_content():
            fd.write(chunk)
