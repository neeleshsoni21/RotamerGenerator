# RotamerGenerator
## This script generates multiple PDB models from a given rotamer library, weighted by the probability of the rotamers, for a specified input protein structure.

## USAGE:

Download the source code or clone it as follows:
```bash
git clone git@github.com:neeleshsoni21/RotamerGenerator.git
```

### Extract the rotamer library file from the zip file
```bash
cd RotamerGenerator/rotamergenerator/data/
unzip ALL.bbdep.rotamers.lib.zip
cd ../..
```


### Use the following command to explore the command line options
```bash
python rg_test.py -h
```

### Run with default arguments.
```bash
python
>>> import rotamergenerator as rg
>>> args = rg.LoadArguments()
>>> rg_obj = rg.RotamerGenerator(args)
```
### OR
```bash
python rg_test.py
```

### Example Run to generate rotamer 100 models in the output directory from the input pdb (toy_pep_long.pdb) with a threshold probability of 1.0 


### Run with command line arguments in python shell
```bash
python
>>> import rotamergenerator as rg
>>> args = rg.LoadArguments()
>>> rg_obj = rg.RotamerGenerator(args)
```
### OR
```bash
python rg_test.py -i ./rotamergenerator/data/toy_pep_long.pdb -l ./rotamergenerator/data/ALL.bbdep.rotamers.lib -k 100 -t 1.0 -o ./rotamergenerator/output/
```


### ---------------------------
### Run with input arguments
### USAGE: python rg_test.py 
### rg_test.py should contain the following lines
### ---------------------------
```bash
python
>>> input_pdb='./rotamergenerator/data/toy_pep_long.pdb'
>>> input_lib='./rotamergenerator/data/ALL.bbdep.rotamers.lib'
>>> threshold=1.0
>>> num_models=10
>>> output_dir='./rotamergenerator/output/'

>>> import rotamergenerator as rg
>>> args = rg.LoadArguments(input_pdb, input_lib, threshold, num_models, output_dir)
>>> rg_obj = rg.RotamerGenerator(args)
```