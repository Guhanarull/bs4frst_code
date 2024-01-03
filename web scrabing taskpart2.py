import requests
from bs4 import BeautifulSoup
#


response = requests.get("https://www.google.com/shopping/product/r/en-US/4872362199572515937")
print(response)
print(response.status_code)
print(response.url)
# print(response.content)

soup = BeautifulSoup(response.text, 'html.parser')

inmage_url = soup.select_one('#mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(2) > td > a').find('href')

print(inmage_url)

#  # mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(8) > td:nth-child(1)

# #mw-content-text > div.mw-parser-output > table

table = soup.select_one('#mw-content-text > div.mw-parser-output > table')
print(type(table))

tr_list = table.select('tr')
print(len(tr_list))

#kingdom = tr_list[7].select_one('a').text
#phylum = tr_list[8].select_one('a').text
#nextone = tr_list[9].select_one('a').text
#nexttwo = tr_list[10].select_one('a').text
#nextthree = tr_list[11].select_one('a').text

row = ''
f = False
for i in range(7, 15):

    if(i != 15):
        value = tr_list[i].select_one('a').text
    else:
       value = tr_list[i].select_one('b').text

    print(value)
    if(f == False):
        row = value
        f = True
    else:
        row = row + '\t' + value


print(row)

o.write(f"{srt_id}\t{inmage_url}\t{row}\t"+'\n')
o.close()
# print(kingdom)
# print(phylum)
# print(nextone)
# print(nexttwo)
# print(nextthree)

# first_h1 = soup.select('tr')[7].text
# first_h2 = soup.select('tr')[8].text
# first_h3 = soup.select('tr')[9].text
# first_h4 = soup.select('tr')[11].text
# first_h5 = soup.select('tr')[13].text
# first_h6 = soup.select('tr')[14].text
# first_h7 = soup.select('tr')[15].text

# thead = [first_h1, first_h2, first_h3, first_h4, first_h5, first_h6, first_h7]

# file = open("parser_data.txt", "w")
# file.write(f'{kingdom}\t{phylum}\t{nextone}\t{nexttwo}\t{nextthree}')
# for tr in thead:
# print(tr)
# file.write(tr)

# for item in images:
#    print(item['src'])
#    file.write(item['src'])
#file.flush()
#file.close()
###################################

# mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(8)
#first_h1 = soup.select('h1')[0].text
# mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(8)
# mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(9)
# mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(11)
# mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(13)
# mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(14)
# mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(15)
# mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(16)
