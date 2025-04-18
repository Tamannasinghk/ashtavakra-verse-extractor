# Ashtavakra Gita Verse Extractor

This script extracts verses and their corresponding indices from the Sanskrit text of the Ashtavakra Gita, available [here](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_aSTAvakragItA.txt). The goal is to parse and store the verses in a structured JSON format.

## What the script does

- Downloads the raw text file using the requests library.
- Identifies lines that contain complete verses ending with a pattern like `// Avg_1.5`.
- Extracts both the verse text and its index from those lines.
- Saves the final output as a JSON file.

## Handling of edge cases

- Skips empty lines and header lines (metadata from the source).
- Only processes lines that end with the expected `// Avg_x.x` format.
- Uses regular expressions to ensure correct matching.
- Trims unnecessary whitespace from the verse lines.

## Output format

The output is a list of dictionaries in the following structure:

{
  "verse": "na tvaṃ viprādiko varṇo nāśramī nākṣagocaraḥ\nasaṅgo 'si nirākāro viśvasākṣī sukhī bhava",
  "index": "1.5"
}

## How to run

You can run this either in Google Colab or locally with Python 3.

If running locally, make sure you have the `requests` library installed:

pip install requests

Then run the script:

python ashtavakra_extractor.py

## Output

The script will generate a file named `ashtavakra_verses.json` containing the extracted data.