# GDBMedChem similarity search

The model looks for 100 nearest neighbors of a given molecule, according to ECFP4 Tanimoto similarity, in the GDBMedChem database. GDBMedChem is a 10M molecule-sampling from GDB17, a database containing all the enumerated molecules of up to 17 atoms heavy atoms (166.4B molecules). GDBMedChem compounds have reduced complexity and better synthetic accessibility than GDB17 but retain high sp3 carbon fraction and natural product likeness, providing a database of diverse molecules for drug design. The whole GDBMedChem database is not downloaded with the model, by using it you post queries to an online server external to Ersilia.

## Identifiers

* EOS model ID: `eos7jlv`
* Slug: `gdbmedchem-similarity`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Similarity`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: List of 100 nearest neighbors

## References

* [Publication](https://onlinelibrary.wiley.com/doi/abs/10.1002/minf.201900031)
* [Source Code](https://gdb-medchem-simsearch.gdb.tools/)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Citation

If you use this model, please cite the [original authors](https://onlinelibrary.wiley.com/doi/abs/10.1002/minf.201900031) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!