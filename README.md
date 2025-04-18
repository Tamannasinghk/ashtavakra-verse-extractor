
# 🕉️ Ashtavakra Gita Verse Extractor

This project parses the Sanskrit verses from the [GRETIL Ashtavakra Gita text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_aSTAvakragItA.txt) and extracts each verse along with its reference index (e.g. `1.5`) into a structured JSON format.

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/Tamannasinghk/ashtavakra-verse-extractor.git
cd ashtavakra-verse-extractor
```

2. Install dependencies (only `requests`):
```bash
pip install requests
```

3. Run the script:
```bash
python ashtavakra_verses.py
```

4. Output will be saved to:
```
ashtavakra_verses.json
```

---

## 🧠 Edge Cases Handled

| Case | Solution |
|------|----------|
| Header info | Skipped content before `aṣṭāvakragītā` |
| Multiline verses | Used regex with `re.DOTALL` |
| Non-standard verse endings | Used pattern with `// Avg_x.x` |
| Unicode Sanskrit | Used `ensure_ascii=False` |
| Clean formatting | Applied `.strip()` and `.replace("
", "")` |

---

## ✅ Output Format

Each item in the JSON looks like:

```json
{
    "verse": "kathaṃ jñānam avāpto 'ti kathaṃ muktir bhaviṣyati \nvairāgyaṃ ca kathaṃ prāptam etad brūhi mama prabho",
    "index": "1.1"
  },
  {
    "verse": "muktim icchasi cet tāta viṣayān viṣavat tyaja \nkṣamārjavadayātoṣasatyaṃ pīyūṣavad bhaja",
    "index": "1.2"
  },
  {
    "verse": "na pṛthvī na jalaṃ nāgnir na vāyur dyaur na vā bhavān \neṣāṃ sākṣiṇam ātmānaṃ cidrūpaṃ viddhi muktaye",
    "index": "1.3"
  },
...............
```

---
