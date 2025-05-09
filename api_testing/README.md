# Task instructions
Develop a few tests for the given endpoint using Python library - requests.

Endpoint rules: https://http.cat/[status_code]  \
Example endpoint:  https://http.cat/status/407 

Create 5 API tests for 1xx, 2xx, 3xx, 4xx, 5xx group (for example https://http.cat/status/407 is for group 4xx). 
1. Using the requests method GET check that: \
Status Code - 200 \
Content-Type - text/html \
H1 header is 407 Proxy Authentication Required in html response (you can use BeautifulSoup python package)

2. Using the requests method GET check the endpoint: https://http.cat/status/ \
Status Code - 403 \
Content-Type - text/html \
H1 header is 403 Forbidden