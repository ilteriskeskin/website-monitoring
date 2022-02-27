import requests
import json

from bs4 import BeautifulSoup


def healt_check(sitemap_url: str) -> list:
    """[summary]
    This function checks links with GET request if they are health or not
    Args:
        sitemap_url (str): Our base url for sitemap.xml
    Returns:
        list: 
        [
            {"link": "www.bombabomba.com", "status": 200},
            {"link": "www.kraloyun.com", "status": 500},
        ]
    """
    healt_check_dict = {}
    healt_check_list = []

    response = requests.get(f'{sitemap_url}')
    soup = BeautifulSoup(response.text, "html.parser")

    links = [link.text for link in soup.find_all("loc")]

    for link in links:
        status_code = requests.get(sitemap_url).status_code
        healt_check_dict["link"] = link
        healt_check_dict["status_code"] = status_code

        healt_check_list.append(healt_check_dict)

    return healt_check_list
