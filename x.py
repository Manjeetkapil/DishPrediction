import requests
from bs4 import BeautifulSoup
URL = "https://www.indianhealthyrecipes.com/apple/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
title = soup.find('meta', attrs = {'property':'og:title'})
description = soup.find('meta', attrs = {'name':'description'})
inpu = soup.findAll('input')
# print(inpu)
allo = []
for i in inpu:
	if i.has_attr("aria-label"):
		allo.append(i['aria-label'])

# print(allo)
# print(soup.prettify())
# print(title)
# print(description) 
# content = soup.find('div',attrs = {'class':'entry-content'})
# for para in content.findAll('p'):
# 	# print(para.contents)
# 	for s in para.select('strong'):
# 		s.extract()
# 	print(para.contents)
ingredient_p = soup.find('div',attrs={'class':'wprm-recipe-ingredient-group'})
ingre_inpu = ingredient_p.findAll('input')
ingredient = []
for i in ingre_inpu:
	if i.has_attr("aria-label"):
		ingredient.append(i['aria-label'])
print('ingredient\n\n')
print(ingredient)
print('\n')
instruction_p = soup.findAll('div',attrs={'class':'wprm-recipe-instruction-group'})
pre_inpu = instruction_p[0].findAll('input')
preparation = []
for i in pre_inpu:
	if i.has_attr("aria-label"):
		preparation.append(i['aria-label'])
print('preparation\n\n')
print(preparation)
print('\n')
final_inpu = instruction_p[1].findAll('input')
final = []
for i in final_inpu:
	if i.has_attr('aria-label'):
		final.append(i['aria-label'])
print('making banana bread\n\n')
print(final)
print('\n')