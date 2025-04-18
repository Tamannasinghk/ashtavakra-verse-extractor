import requests
import re
import json

url = "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_aSTAvakragItA.txt"
response = requests.get(url)

text_content = response.text

lines = text_content.splitlines()

verses = []
for line in lines:
    line = line.strip()  
    
    
    if not line or line.startswith("#") or line.startswith("This file") or line.startswith("##"):
        continue
    
    match = re.search(r'^(.*)//\s*Avg_(\d+\.\d+)', line)
    if match:
        verse_text = match.group(1).strip()
        verse_index = match.group(2).strip()
        
        verses.append({
            "verse": verse_text,
            "index": verse_index
        })


json_output = json.dumps(verses, indent=2, ensure_ascii=False)

with open("ashtavakra_verses.json", "w", encoding="utf-8") as f:
    f.write(json_output)

print("Extraction complete and saved to 'ashtavakra_verses.json'")
