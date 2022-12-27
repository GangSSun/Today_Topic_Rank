# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import datetime
from collections import Counter
import re
import tt
import ban_list as bl


hds = {"User-Agent": "Chrome/108.0.0.0"} # Request 사용을 위한 user-agent 설정
urls = ["https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105",  # IT/과학
        "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100",  # 정치속보
        "https://news.naver.com/main/ranking/popularMemo.nhn",  # 랭킹뉴스 댓글 많은 순
        "https://news.naver.com/main/ranking/popularDay.naver" # 랭킹뉴스 조회 많은 순
        ]
# 참조할 뉴스 사이트 목록
banned = bl.ban_list
# 배제할 키워드 목록

search_list = []
for link in urls:
    baseUrl = urllib.request.Request(link, headers=hds) # link를 user-agent를 통해 URL을 요청 후 저장
    html = urllib.request.urlopen(baseUrl) # Request 객체인 URL을 HTML로 저장
    soup = BeautifulSoup(html, "html.parser") # 파싱하여 변환 후 저장
    if link == "https://news.naver.com/main/ranking/popularMemo.nhn" or "https://news.naver.com/main/ranking/popularDay.naver": 
        for i in soup.find_all(class_="list_title nclicks('RBP.cmtnws')"): 
            # 네이버의 언론사별 랭킹뉴스에서 클래스를 참고해 기사의 제목만 가져옴
            tmp = [word for word in re.sub('[^a-zA-Z0-9가-힣]', " ", i.text).split(" ") if word not in banned]
            # 정규식을 사용해 형태소 분리 후 배제할 키워드를 뺀 후 리스트에 삽입
            search_list += tmp
    else:
        for i in soup.find_all(class_="nclicks(fls.list)"):
            # 언론사별 뉴스를 제외한 사이트들의 클래스는 동일
            tmp = [word for word in re.sub('[^a-zA-Z0-9가-힣]', " ", i.text).split(" ") if word not in banned]
            search_list += tmp
topic_list = []

tmp = ""
for i in range(10): # Counter를 사용해 리스트에서 데이터의 개수가 많은순으로 정렬하여 검색어 순위 출력
    tmp += Counter(search_list).most_common(20)[i][0]
    tmp +=" "
    print(i+1, "위 :", Counter(search_list).most_common(20)[i][0])

topic_list = tmp.split()
tt.UI_tk(topic_list) # GUI 출력