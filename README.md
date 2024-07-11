# RotamerGenerator
## This script generates multiple PDB models from a given rotamer library, weighted by the probability of the rotamers, for a specified input protein structure.

## USAGE:

Download the source code or clone it as follows:
```bash
git clone git@github.com:neeleshsoni21/RotamerGenerator.git
```

### Go to the root directory
```bash
cd RotamerGenerator
```

### Use the following command to explore the command line options
```bash
python src/main.py -h
```

### Example Run to generate rotamer 100 models in the output directory from the input pdb (toy_pep_long.pdb) with a threshold probability of 1.0 
```bash
python ./src/main.py -i ./data/toy_pep_long.pdb -l ./data/ALL.bbdep.rotamers.lib -k 100 -t 1.0 -o ./output/
```
