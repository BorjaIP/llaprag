from pathlib import Path

import requests

from llaprag.paper import Paper


def download_paper(url):
    """Downloads a paper from the given URL and stores it in a folder data.

    Args:
        url (str): The URL of the paper to download.
    """

    # Create the 'data' folder if it doesn't exist
    if not Path("data").exists():
        Path("data").mkdir()

    # Check if the URL is an arXiv URL
    if "arxiv.org" in url:
        print("URL arXiv type.")

        # Download the paper's PDF
        response = requests.get(url)
        arxiv_id = url.split("/")[-1].replace(".pdf", "")
        path = Path("data") / f"{arxiv_id}.pdf"
        with open(path, "wb") as f:
            f.write(response.content)

    return Paper(pdf_url=url, path=path)
