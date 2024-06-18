import requests
from bs4 import BeautifulSoup


url = f'https://www.google.com/search?q={input()}'

response = requests.get(url)

if response.status_code == 200:
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Sample HTML</title>
</head>
<body>
    <h1 id="main-title">Welcome to the Sample Page</h1>
    <div class="content">
        <p class="description">This is a simple HTML page for Selenium testing.</p>
        <ul>
            <li class="item">Item 1</li>
            <li class="item">Item 2</li>
            <li class="item">Item 3</li>
        </ul>
    </div>
    <footer>
        <p>Contact us at <a href="mailto:example@example.com">example@example.com</a></p>
    </footer>
</body>
</html>

"""
    soup = BeautifulSoup(html, 'html.parser')
    #1
    ul = soup.find("h1", id = "main-title").text
    print(ul)
    #2
    ul = soup.find("p", "description").text
    print(ul)
    #3
    ul = soup.find_all("li")
    print(ul)
    #4
    ul = soup.select_one('#main-title')
    print(ul.text)
