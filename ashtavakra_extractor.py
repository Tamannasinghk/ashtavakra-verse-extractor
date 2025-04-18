import requests
import re
import json

url = "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_aSTAvakragItA.txt"
response = requests.get(url)

text_content = response.text

lines = text_content.splitlines()

verses = []
current_verse = []
verse_index = None

for line in lines:
    line = line.strip()

    if not line or line.startswith("{") or line.startswith("#"):
        continue

    match = re.search(r'^(.*)//\s*Avg_(\d+\.\d+)', line)
    if match:
        if current_verse and verse_index:
            verses.append({
                "verse": "\n".join(current_verse),
                "index": verse_index
            })
        
        current_verse = [match.group(1).strip()]
        verse_index = match.group(2).strip()
    else:
        if current_verse:
            current_verse.append(line.strip())

if current_verse and verse_index:
    verses.append({
        "verse": "\n".join(current_verse),
        "index": verse_index
    })

json_output = json.dumps(verses, indent=2, ensure_ascii=False)

with open("ashtavakra_verses.json", "w", encoding="utf-8") as f:
    f.write(json_output)

print("Extraction complete and saved to 'ashtavakra_verses.json'")
