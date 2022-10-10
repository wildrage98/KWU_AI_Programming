import selenium
from selenium import webdriver

import matplotlib.pyplot as plt
from selenium.webdriver.common.by import By
import wordcloud
import time

driver = webdriver.Chrome()

kbonamu = "https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8?from=KBO%EB%A6%AC%EA%B7%B8"

driver.get(kbonamu)
print(driver.current_url)#연 url체크
time.sleep(2)#창을 여는 동안 쉼
body = driver.find_elements(By.CLASS_NAME,"upwzFoAB")
thelist=[]#빈리스트
for text in body:
    print(text.text)
    thelist.append(text.text)#body가 셀레니움의 형태였기 떄문에 body를 텍스트화 시켜서 thelist에 하나씩 넣음
bodyjoin=''.join(thelist)#문자열을 하나로 합침
s_words = wordcloud.STOPWORDS.union({'있다','없다','KBO','때문에','한국','리그','야구','구단','야구장','팀이','중','수','한','더','것은','그','있는','등'})#의미없는 단어 제외
image = wordcloud.WordCloud(font_path='C:/WINDOWS/FONTS/MALGUNSL.TTF',width = 1000, height = 700, stopwords = s_words).generate(bodyjoin)
plt.figure(figsize = (40, 30))
plt.imshow(image)
plt.show()
