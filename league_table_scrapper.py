import requests
from bs4 import BeautifulSoup
from models import LeagueTable

def get_page_content(link:str) -> bytes:

    """
    Function to collect content from website.
    Function is checking if status code is correct (200).
    Args:
        link (str): Link to website.
    Returns:
        Information if connection is wrong (f.e. code 400)
        Content of website
    """

    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    response = requests.get(link, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        raise ValueError(f"Lack of content. Status code: {response.status_code}")
    
page = "https://fbref.com/en/comps/9/2020-2021/2020-2021-Premier-League-Stats"

content = get_page_content(page)

def create_data_to_database(content:bytes) -> list:

    """
    Function to collect values from table and save into database object.
    Args:
        page_content: Website content collected by function get_content
    Returns:
        list_of_values (list): list with values collected from table
    """

    soup1 = BeautifulSoup(content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    table_content = soup2.find('table', attrs={'id': "results2020-202191_overall"})
    rows = table_content.find_all('tr')

    counter = 0

    list_of_database_objects = []

    for row in rows[1:]:
        row = row.find_all("td")
        counter += 1
        column = [element.text.strip() for element in row]
        column.append(counter)

        object_to_database = LeagueTable(season='2020/21', team=str(column[0]), matches = int(column[1]), points=int(column[8]), position=column[-1])
        
        list_of_database_objects.append(object_to_database)

    return list_of_database_objects

league_table = create_data_to_database(content)


