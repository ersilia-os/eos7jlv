from bs4 import BeautifulSoup
import requests
import json
import sys

# Input Parameters

input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()
fp     = 'ECfp4'
db     = 'GDBMedChem'
nnc    = '100'



data = []
for input_smiles in Lines:
    input_smiles = input_smiles.strip() 
    url = 'https://gdb-medchem-simsearch.gdb.tools/search?smi=' + input_smiles +  '&fp=' + fp + '&db=' + db + '&nnc=' + nnc
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
    
with open(sys.argv[2], 'w') as f:
    json.dump(data, f)
