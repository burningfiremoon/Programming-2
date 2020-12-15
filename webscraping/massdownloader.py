# massdownloader.py
#

import os
import requests
import bs4

url = "https://xkcd.com"  # starting url

# Create a folder/directory to store comics
os.makedirs("xkcdimages", exist_ok=True)

# Loop while the url DOES NOT end with a "#"

while not url.endswith("#"):
    # Downloading the html
    # ----- Downloading the HTML -----
    print(f"Download page{url}...")
    res = requests.get(url)
    res.raise_for_status() # STOP if there's an erroa
    soup = bs4.BeautifulSoup(res.text, "html.parser")


    # -----Finding the URL/href of the image ------
    comic_elem = soup.select("#comic img")
    if comic_elem == [] or comic_elem[0].get("src").startswith("/2067") or comic_elem[0].get("src").startswith("/1525"):
        print("Couldn't find image...")
    else:
        comic_url = "https:" + comic_elem[0].get("src")
        print(f"\tDownloading image {comic_url}...")
        # -----Downloading the image-----
        res = requests.get(comic_url)
        res.raise_for_status()



        # -----Saving the image to disk-----
        image_file = open(os.path.join("xkcdimages", os.path.basename(comic_url)), "wb") # wb = write in binary
        for chunk in res.iter_content(1000000):
            image_file.write(chunk)
        image_file.close()
    # -----Getting the Prev button's URL-----
    prev_link = soup.select('a[rel="prev"]')[0]
    url = " https://xkcd.com" + prev_link.get("href")

print("done")