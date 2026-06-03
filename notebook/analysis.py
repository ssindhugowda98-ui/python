# -----------------------------------------
# Create visuals folder if not exists
# -----------------------------------------

os.makedirs("../visuals", exist_ok=True)

# -----------------------------------------
# Extract ZIP File
# -----------------------------------------

zip_path = "../archive.zip"

extract_path = "../data"

# Create data folder if not exists
os.makedirs(extract_path, exist_ok=True)

# Unzip archive.zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("\n========== ZIP FILE EXTRACTED ==========\n")
