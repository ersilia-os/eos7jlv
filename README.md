# GDBMedChem similarity search

The model looks for 100 nearest neighbors of a given molecule, according to ECFP4 Tanimoto similarity, in the GDBMedChem database. GDBMedChem is a 10M molecule-sampling from GDB17, a database containing all the enumerated molecules of up to 17 atoms heavy atoms (166.4B molecules). GDBMedChem compounds have reduced complexity and better synthetic accessibility than GDB17 but retain high sp3 carbon fraction and natural product likeness, providing a database of diverse molecules for drug design. The whole GDBMedChem database is not downloaded with the model, by using it you post queries to an online server external to Ersilia.

This model was incorporated on 2022-08-18.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7jlv`
- **Slug:** `gdbmedchem-similarity`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Similarity search`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Similarity`, `ChEMBL`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `100`
- **Output Consistency:** `Fixed`
- **Interpretation:** List of 100 nearest neighbors

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smiles_00 | string |  | Sampled smiles 0 from a similarity search in GDBMedChem |
| smiles_01 | string |  | Sampled smiles 1 from a similarity search in GDBMedChem |
| smiles_02 | string |  | Sampled smiles 2 from a similarity search in GDBMedChem |
| smiles_03 | string |  | Sampled smiles 3 from a similarity search in GDBMedChem |
| smiles_04 | string |  | Sampled smiles 4 from a similarity search in GDBMedChem |
| smiles_05 | string |  | Sampled smiles 5 from a similarity search in GDBMedChem |
| smiles_06 | string |  | Sampled smiles 6 from a similarity search in GDBMedChem |
| smiles_07 | string |  | Sampled smiles 7 from a similarity search in GDBMedChem |
| smiles_08 | string |  | Sampled smiles 8 from a similarity search in GDBMedChem |
| smiles_09 | string |  | Sampled smiles 9 from a similarity search in GDBMedChem |

_10 of 100 columns are shown_
### Source and Deployment
- **Source:** `Online`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7jlv](https://hub.docker.com/r/ersiliaos/eos7jlv)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7jlv.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7jlv.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `248`
- **Image Size (Mb):** `210.25`


### References
- **Source Code**: [https://gdb-medchem-simsearch.gdb.tools/](https://gdb-medchem-simsearch.gdb.tools/)
- **Publication**: [https://onlinelibrary.wiley.com/doi/abs/10.1002/minf.201900031](https://onlinelibrary.wiley.com/doi/abs/10.1002/minf.201900031)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7jlv
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7jlv
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
