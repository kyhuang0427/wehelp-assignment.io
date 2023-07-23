import requests
import csv

region_mapping = [
    "中正區",
    "萬華區",
    "中山區",
    "大同區",
    "大安區",
    "松山區",
    "信義區",
    "士林區",
    "文山區",
    "北投區",
    "內湖區",
    "南港區"
]



url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
response = requests.get(url)
data = response.json()

def extract_region(address):
    for district in region_mapping:
        if district in address:
            return district
    return ""


with open("attraction.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
   
    for item in data["result"]["results"]:
        name = item["stitle"]
        address = item["address"]
        region = extract_region(address)
        lat = item["latitude"]
        lng = item["longitude"]
        if lat and lng:
            writer.writerow([item["stitle"], region, lat, lng, item["file"].split(";")[0]])

mrt_dict = {}
for item in data["result"]["results"]:
    mrt = item["MRT"]
    if mrt not in mrt_dict:
        mrt_dict[mrt] = []
    mrt_dict[mrt].append(item["stitle"])

with open("mrt.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for mrt, attractions in mrt_dict.items():
        writer.writerow([mrt] + attractions)
