
from pydoc import classname
import requests
from bs4 import BeautifulSoup
 
def scraper(link): # takes in link and outputs title and body text
    # Making a GET request
    r = requests.get(link)
    
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    allClasses = [value 
            for element in soup.find_all(class_=True) 
            for value in element["class"]]
    names = ['entry','body']
    lessClasses = set() 


    for className in allClasses: # appends class names which contain anything from names array
        for i in names:
            if i in className.lower() and 'ad' not in className.lower() and 'site' not in className.lower():
                lessClasses.add(className)

    print(lessClasses)
    title = soup.find('h1')
    lines = soup.find_all(True, {'class':[lessClasses]}) # finds all lines with class names in lessClasses
    print(len(lines))
    if len(lines) <= 1:
        lines = soup.find_all('p')
    bigSentence = ''

    for line in lines: # appends all lines into one big string
        if '.' in line.text and '             ' not in line.text:
            #print(len(line.text), line.text)
            bigSentence += line.text

    print(title.text)
    #print(bigSentence)
    return (title.text, bigSentence)
    