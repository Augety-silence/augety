import csv
import re

file_path = "./comment.txt"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

pattern = re.compile(r"([\S]+)\n\n([\s\S]+?)\n(\d{4}-\d{2}-\d{2} \d{2}:\d{2})")
matches = pattern.findall(content)

csv_path = "./comment.csv"

with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["姓名", "正文", "时间"]) 
    writer.writerows(matches)

csv_path
