import requests
from bs4 import BeautifulSoup
from models import TransferSpending

def get_content(link:str) -> bytes:

    """
    Function to collect content from website.
    Function is checking if status code is correct (200).
    Args:
        link (str): Link to website.
    Returns:
        Information if connection is wrong (f.e. code 400)
        Content of website
    """

    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    response = requests.get(link, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        raise ValueError(f"Lack of content. Status code: {response.status_code}")

def get_data_from_website(page_content: bytes) -> list:

    """
    Function to collect values from table.
    Args:
        page_content: Website content collected by function get_content
    Returns:
        list_of_values (list): list with values collected from table
    """
        
    content = BeautifulSoup(page_content, 'html.parser')
    page = BeautifulSoup(content.prettify(), 'html.parser')

    finding = str(page.find_all('div', attrs={'class': 'wappenleiste-box'}))  # Looking for team name

    soup = BeautifulSoup(finding, 'html.parser')
    titles = [img['title'] for img in soup.find_all('img')]

    a = page.find_all('div', attrs={'class': 'transfer-zusatzinfo-box'})  # Looking for transfer spendings

    list_of_spendings = []

    for item in a:
        item = item.find_all('span')
        cols = [element.text.strip() for element in item]
        list_of_spendings.append(cols)


    final_list = list(zip(list_of_spendings, titles))

    return final_list

def data_manipulation(website_data:list) -> list:

    """
    Function to prepare a data from website to add them into list of database objects.
    Args:
        Table colleted by function get_data_from_website (list)
    Returns:
        List_of_dict (list): List all values
    """
    
    list_of_database_objects = []

    for row in website_data:
        club_name = str(row[1])
        season = '2024/25'

        average_age = row[0][0]
        average_age = float(average_age[-4:].replace(",", '.'))

        money_spend = row[0][2]
        money_spend = money_spend[-12:-6]

        if money_spend[0] == " ":
            money_spend = float(money_spend[1:].replace(",", '.'))
        elif money_spend[1] == " ":
            money_spend = float(money_spend[2: ].replace(",", "."))
        else:
            money_spend = float(money_spend.replace(",", "."))

        club_spendings = TransferSpending(season=season, club=club_name, average_age=average_age, money_spendings=money_spend)

        list_of_database_objects.append(club_spendings)

    return list_of_database_objects

website = 'https://www.transfermarkt.pl/premier-league/transfers/wettbewerb/GB1'

r = get_content(website)

raw_data = get_data_from_website(r)
final_data = data_manipulation(raw_data)



