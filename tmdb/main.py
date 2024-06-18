import requests
import time

import openpyxl as xl
wb = xl.Workbook()
ws = wb.active
filename = "tmdb/data.xlsx"
ws.append(['id','국가', '언어', '원제목', '영어제목','장르', '인기도', '개봉일', '런타임', '평점', '투표수'])

api_key = "a1232fe9acbc1e835c06033ecaa83080"

total = 0
scores = 0
for i in range(int(input("시작 ID: ")), int(input("마지막 ID: ")) + 1 , int(input("주기: "))):

    url = f"https://api.themoviedb.org/3/movie/{i}?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        row = [
                i,
                data['origin_country'][0] if len(data['origin_country']) != 0 else "NONE",
                data["original_language"],
                data["original_title"],
                data["title"],
                " ".join([data["genres"][x]["name"] for x in range(len(data["genres"]))]),
                data["popularity"],
                data["release_date"],
                data["runtime"],
                data["vote_average"],
                data["vote_count"]
                ]
        print(f"success on {i}")
        ws.append(row)
        time.sleep(0.1)
        total += 1
        scores += data["vote_average"]
    else:
        print(f"ERROR_code on {i}: {response.status_code} - {"movie not found" if response.status_code == 404 else "I dont know why"}")
wb.save(filename)
wb.close()
print(round((scores / total), 2))