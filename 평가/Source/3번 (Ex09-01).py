import time
import bs4
import urllib.request

# 파일에 저장할 데이터를 담을 문자열 초기화
data_to_save = ""

nateUrl = "https://news.nate.com/recent?mid=n0100"
while True:
    htmlObject = urllib.request.urlopen(nateUrl)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag_list = bsObject.findAll('div', {'class': 'mlt01'})

    data_to_save += '###### 실시간 뉴스 속보 #######\n'
    num = 1
    for tag in tag_list:
        subject = tag.find('h2', {'class': 'tit'}).text
        link = tag.find('a', {'class': 'lt1'})['href']
        pressAndDate = tag.find('span', {'class': 'medium'}).text
        pressAndDate.replace('\t', ' ')
        pressAndDate.replace('\n', '')

        if len(pressAndDate.split()) == 3:
            press, pDate, pTime = pressAndDate.split()
        elif len(pressAndDate.split()) == 4:
            press1, press2, pDate, pTime = pressAndDate.split()
            press = press1 + press2
        else:
            continue

        data_to_save += '(' + str(num) + ')' + subject + '\n'
        data_to_save += '\t https:' + link + ' ' + press + ' ' + pDate + ' ' + pTime + '\n'
        num += 1

    # 데이터를 파일에 저장
    with open("nate_news.txt", "w", encoding="utf-8") as file:
        file.write(data_to_save)

    time.sleep(120)
