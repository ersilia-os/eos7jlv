from bs4 import BeautifulSoup
import requests
import csv
import sys
import urllib

# Input Parameters
input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()[1:]
fp     = 'ECfp4'
db     = 'GDBMedChem'
nnc    = '100'

data = []
for input_smiles in Lines:
    input_smiles = input_smiles.strip() 
    url_encoded_smiles = urllib.parse.quote(input_smiles)
    url = 'https://gdb-medchem-simsearch.gdb.tools/search?smi=' + url_encoded_smiles +  '&fp=' + fp + '&db=' + db + '&nnc=' + nnc
    r = requests.get(url)
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
        similarity_indices.append(x[3].strip('\"'))    
    data+= [[smiles_list, similarity_indices]]
    
header = ["sim-{0}".format(i+1) for i in range(len(smiles_list))]
with open(sys.argv[2], "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for d in data:
        writer.writerow(d[0])
