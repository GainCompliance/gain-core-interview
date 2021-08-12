# Gain Core Team Technical Interview

Before we get too deep though, we should get a few definitions out of the way
## Definitions
---
### --- Sfile ---
An Sfile is simply a data file. For our purposes, we are going to deviate from the actual spec of an Sfile. We are going to define an sfile as a list of sections. A section (as we are going to define it) is two parts:
1. A section header of the form *[Header Text]*
2. A rectangular, white space delimited set of data.
### --- Meta ---
For this exercise, the Meta class will represent two parts. One part is the rule definitions which we will cover shortly. The other is the structure definitions. The structure definitions define the size of what a valid section can be. By proxy, they also define what a valid section header is. The sizes will come as the json mapping {"x": int, "y": int}. This is where x defines the number of values in a row, and y defines the number of rows. 
## Task
---
In the interview folder of this repo, you will find a file called *sfile_parser.py*. This folder currently contains a sckeleton implementation of the abstract map reducer (*found at **interview/MapReduce/map_reduce.py***). 
### Parsing
The goal is to implement this example to take a path to an sfile and output a json file. An example of an sfile can be found in *P2020sfile.txt*. Sections can be found in the brackets of the file, with the data following. This is a whitespace deliniated file. The output file should contain a json dictionary mapping the section to the raw data. 
### Verification
Along with parsing this file, your implementation should verify if the data contained is correct. This will involve using the **Meta** class found at *interview/Meta/meta.py* this will contain the metadata about the defining codes and their structure.
## Running
---
This project has one requirement.  ***Pydantic** version 1.8.2.*
...