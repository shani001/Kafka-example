import requests,json
import pandas as pd


#fetching data from API
def fetchapi(url):
    
    response=requests.get(url=url)
    myvar=response.json()
    return myvar

#saving data to csv file
def save_to_csv(myvar):
    panda = pd.json_normalize(myvar["items"])
    print(panda)
    panda.to_csv('planet_data.csv', index=False)


#saving data to text file
def print_data(myvar):
    for items in myvar['items']:
        print("Id =",items['id'],"Name =",items["name"])


def save_to_txt(myvar):
    with open('planet_data.txt', 'a', encoding='utf-8') as f:
        for items in myvar['items']:
            f.write(f"Id = {items['id']} Name = {items['name']}\n")


if __name__ == "__main__":
    url = "https://dragonball-api.com/api/characters"
    myvar=fetchapi(url)
    print_data(myvar)
    save_to_txt(myvar) 
    save_to_csv(myvar)