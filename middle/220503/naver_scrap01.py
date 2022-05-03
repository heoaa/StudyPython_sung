# 네이버 웹페이지 긁어오기
from urllib.request import Request, urlopen

# 요청
req = Request('https://www.naver.com/')
# 응답
res = urlopen(req)    # url 또는 request 객체 삽입
print(res.status_code))
