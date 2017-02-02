"""
requests 를 테스트해본다
"""

import requests

r = requests.get('http://www.naver.com')
print(r.text)
