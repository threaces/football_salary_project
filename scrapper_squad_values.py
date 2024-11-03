import requests
from bs4 import BeautifulSoup
from models import SquadValue


def get_web_content(link: str) -> bytes:

    """
    Function to collect content from website.
    Function is checking if status code is correct (200).
    Args:
        link (str): Link to website.
    Returns:
        Information if connection is wrong (f.e. code 400)
        Content of website
    """

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    r = requests.get(link, headers=headers)

    if r.status_code == 200:
        return r.content
    else:
        raise ValueError(f"Lack of content/ Access denied. Status code: {r.status_code}")


link = 'https://www.transfermarkt.pl/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2024'

value = get_web_content(link)

def get_raw_data(page_content: bytes, class_name: str) -> list:

    """
    Function to collect values from table.
    Args:
        page_content: Website content collected by function get_content
        class_name (str): Value collected from website to identify concrete value
    Returns:
        list_of_values (list): list with values collected from table
    """

    soup = BeautifulSoup(page_content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

    table = soup2.find('table', attrs={'class': f'{class_name}'})
    rows = table.find_all('tr')

    list_of_lists = []

    for item in rows[2:]:
        cols = item.find_all('td')
        cols = [element.text.strip() for element in cols]
        list_of_lists.append(cols)

    return list_of_lists

table = get_raw_data(value, 'items')

def clean_data(list_of_items: list) -> list:

    """
    Function to save all data into list of dictionaries.
    Args:
        Table colleted by function get_table
    Returns:
        List_of_dict (list): List all values
    """

    list_of_dicts = []

    for row in list_of_items:

        one_dict = {}
        
        one_dict['Team'] = row[1]
        one_dict['Squad'] = int(row[2])

        avg_age = float(row[3].replace(',', '.'))  

        if row[-1][-3] == 'd':
            squad_value = float(row[-1][:4].replace(",", ".")) * 1000000000
        else:
            squad_value = float(row[-1][:5].replace(",", ".")) * 1000000

        if row[-2][4] == " ":
            avg_player_value = float(row[-2][:4].replace(",", ".")) * 1000000
        else:
            avg_player_value = float(row[-2][:5].replace(',', '.')) * 1000000

        one_dict = SquadValue(team=row[1], squad_member=int(row[2]), average_age=avg_age, season='2024/25', 
                              average_player_value=round(avg_player_value, 2), squad_value=round(squad_value, 2))

        list_of_dicts.append(one_dict)

    return list_of_dicts             

data = clean_data(table)


