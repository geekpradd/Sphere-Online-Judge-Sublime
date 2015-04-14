from bs4 import BeautifulSoup 
import requests 

URL = "http://www.spoj.com/problems/%s/"

def get_parsed(tag): 
	uri = URL % tag 
	r = requests.get(uri) 
	if r.status_code >=300:
		return None
	soup = BeautifulSoup(r.text) 
	problem = soup.select("#problem-body")[0]
	title = soup.select("#problem-name")[0]
	problem.insert(0, title)
	for tag in ["p", "span", "a", "b", "strong", "i", "em"]:
		for match in problem.findAll(tag):
			match.unwrap()
	for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
		for match in problem.findAll(tag):
			match.unwrap()
	for match in problem.findAll("pre"):
		match.replaceWith("[code]\n"+match.text+"[/code]")
	return problem.text.strip()


