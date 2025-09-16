import os
import json
from bs4 import BeautifulSoup

# ✅ Configure scan folders
SCAN_FOLDERS = [
    ".",  # root files (index.html, terms.html, etc.)
    "app-files",
    "assets",
    "pages"
]

OUTPUT_FILE = "searchIndex.json"

def extract_text_from_html(file_path, base_dir):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f, "html.parser")

        # Remove scripts, styles, etc.
        for tag in soup(["script", "style", "noscript"]):
            tag.extract()

        title = soup.title.string.strip() if soup.title else os.path.basename(file_path)
        text = soup.get_text(" ", strip=True)

        return {
            "title": title,
            "url": os.path.relpath(file_path, base_dir).replace("\\", "/"),
            "content": text
        }

def build_index():
    index = []

    for folder in SCAN_FOLDERS:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".html"):
                    file_path = os.path.join(root, file)
                    print(f"Indexing: {file_path}")
                    page_data = extract_text_from_html(file_path, ".")
                    index.append(page_data)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        json.dump(index, out, indent=2, ensure_ascii=False)

    print(f"\n✅ Done! Search index saved as {OUTPUT_FILE}")

if __name__ == "__main__":
    build_index()
