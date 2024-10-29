import requests
from bs4 import BeautifulSoup
import pprint

def get_content(link: str):

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

url = 'https://fbref.com/en/comps/9/2022-2023/wages/2022-2023-Premier-League-Wages'

salaries = get_content(url)

def get_table(page_content, table_id: str):

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

annual_wages = get_table(salaries, 'squad_wages')

def get_data(table):

    """
    Function to save all data into list of dictionaries.
    Args:
        Table colleted by function get_table
    Returns:
        List_of_dict (list): List all values
    """

    list_of_dicts = []

    for item in table:
        one_dict = {}

        weekly_salary = item[2].strip('\n')
        weekly_salary = weekly_salary.strip(" ")
    
        if weekly_salary[10] == " ":
            weekly_salary = weekly_salary[2: 10]
        else:
            weekly_salary = weekly_salary[2: 11]

        annual_salary = item[3].strip('\n')
        annual_salary = annual_salary.strip(" ")
    
        if annual_salary[13] == " ":
            annual_salary = annual_salary[2:13]
        else:
            annual_salary = annual_salary[2:14]

        one_dict['Team'] = item[0]
        one_dict['Number of Players'] = int(item[1])
        one_dict['Weekly Salary'] = float(weekly_salary.replace(",", ""))
        one_dict['Annual Salary'] = float(annual_salary.replace(",", ""))
        one_dict['Season'] = '2022/23'
        
        list_of_dicts.append(one_dict)
    
    return list_of_dicts

list_of_teams = get_data(annual_wages)


