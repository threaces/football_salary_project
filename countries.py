import requests
from pydantic import BaseModel, Field
from collections import defaultdict, Counter
from functools import singledispatch

class Country(BaseModel):

    common:str
    cca3: str

class CountryResponse(BaseModel):

    name:Country = Field(...,description="Country object")
    cca3: str


r = requests.get("https://restcountries.com/v3.1/all")

country_data = r.json()


#print([CountryResponse(**country).name.common for country in country_data])

country_info = [
    {"common_name": CountryResponse(**country).name.common, "cca3": CountryResponse(**country).cca3}
    for country in country_data
]

# Print the result (common names and cca3 codes)
for info in country_info:
    print(f"Country: {info['common_name']}, CCA3: {info['cca3']}")


'''list_names = ['James', 'Katrine', 'Adam', "James", "James", "Adam"]

dict_names = defaultdict(int)

for item in list_names:
    dict_names[item] += 1

print(dict(sorted(dict_names.items(), key=lambda item: item[1], reverse=True)))
print(Counter(list_names).most_common())

@singledispatch
def sample_function(money):

    raise NotImplementedError("Not supported type")

@sample_function.register
def _(money: int):
    print(money * 2)
@sample_function.register
def _(money: str):
    print(money)

sample_function(20)
sample_function("abba")'''

