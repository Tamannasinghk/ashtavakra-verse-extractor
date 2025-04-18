import re
import requests
import json

# Step 1: Download the text file and saving variablle "data" .
url = "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_aSTAvakragItA.txt"
response = requests.get(url)
data = response.text

# Step 2: Start reading after "aṣṭāvakragītā" , as we only want the verses and index but there is other info also in text .
if "aṣṭāvakragītā" in data:
    data = data.split("aṣṭāvakragītā", 1)[1]

# Step 3: Use re module (regex) to extract verses and indices .
pattern = r"(.*?)//\s*Avg_(\d+\.\d+)"
matches = re.findall(pattern, data, re.DOTALL)

# Step 4: Structure the output into JSON format .
verses = []
for verse_text, verse_index in matches:
    clean_verse = verse_text.strip().replace("\r", "")
    verses.append({
        "verse": clean_verse,
        "index": verse_index
    })

# Saving the json file .
with open("ashtavakra_verses.json", "w", encoding="utf-8") as f:
    json.dump(verses, f, ensure_ascii=False, indent=2)

print("JSON file saved as 'ashtavakra_verses.json'")

