# Develop a few tests for the given endpoint using Python library - requests.
#
# Endpoint rules: https://http.cat/[status_code]
# Example endpoint:  https://http.cat/status/407
#
# Create 5 API tests for 1xx, 2xx, 3xx, 4xx, 5xx group (for example https://http.cat/status/407 is for group 4xx).
# 1. Using the requests method GET check that:
# Status Code - 200
# Content-Type - text/html
# H1 header is 407 Proxy Authentication Required in html response (you can use BeautifulSoup python package)
#
# 2. Using the requests method GET check the endpoint: https://http.cat/status/
# Status Code - 403
# Content-Type - text/html
# H1 header is 403 Forbidden
import requests
from bs4 import BeautifulSoup as bS


def check_status_code(url: str, expected_status_code: int):
    response = requests.get(url)
    text_body = bS(response.text, "html.parser")
    header_text = text_body.find('main').find('h1').text.strip() if response.status_code == 200 else text_body.find('h1').text.strip()

    print(f"URL: {url}")
    print(f"Status code: {response.status_code}")
    print(f"Content-type: {response.headers['content-type']}")
    print(f"Header: {header_text}")
    print()
    assert response.status_code == expected_status_code

def main():
    test_urls = [
        ("https://http.cat/status/101", 200),
        ("https://http.cat/status/204", 200),
        ("https://http.cat/status/301", 200),
        ("https://http.cat/status/400", 200),
        ("https://http.cat/status/500", 200),
        ("https://http.cat/status/", 403)
    ]

    for url, code in test_urls:
        try:
            check_status_code(url, code)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()