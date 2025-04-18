import re
import json

results = []

with open('sa_aSTAvakragItA.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    verse_text = ""
    verse_index = None

    for line in lines:
       
        if not line.strip() or line.startswith("#"):
            continue
        match = re.match(r"(.*)(// Avg_(\d+\.\d+))$", line.strip())

        if match:
            
            verse_text += match.group(1).strip()
            verse_index = match.group(3)
            
            results.append({
                "verse": verse_text.strip(),
                "index": verse_index
            })
            verse_text = ""
            verse_index = None
        else:
            verse_text += line.strip() + " "

with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=2)

