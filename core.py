from bs4 import BeautifulSoup 
import requests 

URL = "http://www.spoj.com/problems/%s/"

def get_parsed(tag): 
    uri = URL % tag 
    r = requests.get(uri) 
    if r.status_code >=300:
        return None
    soup = BeautifulSoup(r.text) 
    table = soup.select("#problem-meta")[0].find("tbody")
    time = table.findAll("tr")[2].findAll("td")[1].text
    source = table.findAll("tr")[3].findAll("td")[1].text
    memory = table.findAll("tr")[4].findAll("td")[1].text
    problem = soup.select("#problem-body")[0]
    title = soup.select("#problem-name")[0]
    problem.insert(0, title)
    kwargs = {"Time_Limit":time, "Source_Limit":source,"Memory_Limit":memory}

    for tag in ["p", "span", "a", "b", "strong", "i", "em"]:
        for match in problem.findAll(tag):
            match.unwrap()
    for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        for match in problem.findAll(tag):
            match.unwrap()
    for match in problem.findAll("pre"):
        match.replaceWith("[code]\n"+match.text+"[/code]")
    content = problem.text.strip() + "\n\n"
    for key in kwargs:
    	content+= key.replace("_", " ")+ ": " + kwargs[key] +"\n"
    return content



