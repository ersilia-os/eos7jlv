from bs4 import BeautifulSoup
import requests
import csv
import os
import sys
import urllib.parse

# Input Parameters
fp     = 'ECfp4'
db     = 'GDBMedChem'
nnc    = '100'

# The output contract (number, names and order of columns) is declared in
# columns/run_columns.csv and does not depend on what the server returns.
ROOT = os.path.dirname(os.path.abspath(__file__))
COLUMNS_FILE = os.path.join(ROOT, "..", "columns", "run_columns.csv")


def read_header():
    with open(COLUMNS_FILE, "r", newline="") as f:
        return [row["name"] for row in csv.DictReader(f)]


def fetch_neighbours(input_smiles):
    """Return the neighbours of a query, sorted by decreasing similarity."""
    url_encoded_smiles = urllib.parse.quote(input_smiles)
    url = 'https://gdb-medchem-simsearch.gdb.tools/search?smi=' + url_encoded_smiles +  '&fp=' + fp + '&db=' + db + '&nnc=' + nnc
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, features = 'html.parser')
    results = soup.find_all('script')
    T = str(results[-1]).splitlines()
    T = [i for i in T if not ('IDX' not in i)]
    smiles_list = []
    similarity_indices = []
    for i in T:
        x = i.split('+\"')
        x1 = x[1].split("IDX")
        x2 = x1[0]
        smiles_list.append(x2.strip(' '))
        similarity_indices.append(float(x[3].strip('\"')))
    paired = list(zip(smiles_list, similarity_indices))
    paired.sort(key=lambda x: (-x[1], x[0]))
    return [smi for smi, _ in paired]


def fit_row(neighbours, n_columns):
    """Pad with empty cells (or truncate) so the row has exactly n_columns."""
    row = list(neighbours[:n_columns])
    return row + [""] * (n_columns - len(row))


def main(input_path, output_path):
    header = read_header()

    with open(input_path, 'r') as input_file:
        Lines = input_file.readlines()[1:]

    data = []
    for input_smiles in Lines:
        input_smiles = input_smiles.strip()
        try:
            neighbours = fetch_neighbours(input_smiles)
        except Exception as e:
            # Invalid SMILES (the server answers with an error), no result or
            # network failure: report an entirely empty row for this molecule
            # instead of aborting the whole batch.
            print("No result for %r: %s" % (input_smiles, e), file=sys.stderr)
            neighbours = []
        data += [fit_row(neighbours, len(header))]

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
