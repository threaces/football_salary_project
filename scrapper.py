import requests
from bs4 import BeautifulSoup
import pprint
from models import AnnualWage, AnnualWagesPlayers

def get_content(link: str) -> bytes:

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
       raise ValueError(f"Lack of content. Status code: {r.status_code}")

url = 'https://fbref.com/en/comps/9/2020-2021/wages/2020-2021-Premier-League-Wages'

salaries = get_content(url)

def get_table(page_content: bytes, table_id: str) -> list:

    """
    Function to collect values from table.
    Args:
        page_content: Website content collected by function get_content
        table_id (str): Value collected from website to identify concrete value
    Returns:
        list_of_values (list): list with values collected from table
    """

    soup = BeautifulSoup(page_content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

    table = soup2.find('table', attrs={'id': f'{table_id}'})
    rows = table.find_all('tr')

    list_of_values = []

    for item in rows[1:]:
        cols = item.find_all('td')
        cols = [element.text.strip() for element in cols]
        list_of_values.append(cols)

    return list_of_values

annual_wages = get_table(salaries, 'player_wages')

def get_data(table) -> list[dict]:

    """
    Function to save all data into list of dictionaries.
    Args:
        Table colleted by function get_table
    Returns:
        List_of_dict (list): List all values
    """

    list_of_dicts = []

    for row in table:
        
        weekly_salary = row[2].strip('\n').strip(" ")
    
        weekly_salary = weekly_salary[2: 10] if weekly_salary[10] == " " else weekly_salary[2: 11]

        annual_salary = row[3].strip('\n')
        annual_salary = annual_salary.strip(" ")
    
        if annual_salary[13] == " ":
            annual_salary = annual_salary[2:13]
        else:
            annual_salary = annual_salary[2:14]

        one_dict = AnnualWage(team=row[0], season='2022/23', weekly_salary=float(weekly_salary.replace(",", "")), annual_salary=float(annual_salary.replace(",", "")))
       
        list_of_dicts.append(one_dict)
    
    return list_of_dicts

def get_data_table(table: list) -> list[dict]:

    """
    Function to save all data into list of dictionaries.
    Args:
        Table colleted by function get_table
    Returns:
        List_of_dict (list): List all values
    """

    list_of_dicts = []

    for row in table:
       
        if len(row[2]) == 2:
            position = row[2]
        else:
            position = row[2][:2]

        weekly_salary = row[5].strip()
        weekly_salary = weekly_salary[2:10]

        if weekly_salary[-1] == "\n":
            weekly_salary = float(weekly_salary[:-1].replace(',', '.')) * 1000
        elif weekly_salary[-2] == "\n":
            weekly_salary = float(weekly_salary[:-2].replace(',', '.')) * 1000
        elif weekly_salary[-3] == "\n":
            weekly_salary = float(weekly_salary[:-3].replace(',', '.')) * 1000
        else:
            weekly_salary = float(weekly_salary[:-4].replace(',', '.'))

        annual_salary = row[-2].strip()
        annual_salary = annual_salary[2: 13]
        
        if annual_salary[-1] == "\n":
            annual_salary = float(annual_salary[:-1].replace(",", ""))
        elif annual_salary[-2] == "\n":
            annual_salary = float(annual_salary[:-2].replace(",", ""))
        else:
            annual_salary = float(annual_salary[:-3].replace(",", ""))

        one_dict = AnnualWagesPlayers(season='2020/21', player_name=row[0], nationality=row[1][-3:], club=row[3], position=position,
                                      age = int(row[4]), weekly_salary=weekly_salary, annual_salary=annual_salary)

        list_of_dicts.append(one_dict)

    return list_of_dicts

list_of_teams = get_data_table(annual_wages)


