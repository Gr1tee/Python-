# try:
# 	float('abc123')
# except:
# 	import sys
# 	exc_tuple=sys.exc_info()

# print exc_tuple

# for eachItem in exc_tuple:
# 	print eachItem

# import requests
# r=requests.get('http://www.baidu.com')
# print (r.status_code)
# print r.encoding
# print r.apparent_encoding
# r.encoding='utf-8'
# print r.text

# requests.ConnectionError
# requests.HTTPError
# requests.URLRequired
# requests.TooManyRedirects
# requests.ConnectTimeout
# requests.Timeout

# import requests

# def getHTMLText(url):
# 	try:
# 		r=requests.get(url,timeout=30)
# 		r.raise_for_status()
# 		r.encoding=r.apparent_encoding
# 		return r.text
# 	except:
# 		return 'Error exsists!'

# if __name__ == '__main__':
# 	url='http://www.baidu.com'
# 	print getHTMLText(url)

# import requests

# r=requests.get('https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B01ION3VWI/ref=sr_1_1?s=books&ie=UTF8&qid=1500255041&sr=1-1&keywords=python')

# r.encoding=r.apparent_encoding
# print r.text
# print r.request.headers
# import requests
# kv={'user-agent':'Mozilla/5.0'}
# url="https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B01ION3VWI/ref=sr_1_1?s=books&ie=UTF8&qid=1500255041&sr=1-1&keywords=python"
# r=requests.get(url,headers=kv)
# print r.status_code
# print r.text[1000:2000]
# import requests
# kv={'wd':'python'}
# r=requests.get('http://www.baidu.com/s',params=kv)
# print r.status_code

# print r.request.url
# print len(r.text)









