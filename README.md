# MiniProject-Comp383-


**Before you start, have these installed**

1. Python3
2. SRA Tool Kit 3.0.0
3. SPAdes 3.15.4
4. Prokka

This is a Github Repo for py script. It functions as python wrapper to automate execution of software tools, in which the Ecoli K-12 strains will be sequenced again and assembled by runing the script. Resequencing is done to see the change in time from the original K-12 strain. 

The py script will automate and product output file to "miniproject.log" and files in a folder named "results". All results generated will be written to this folder. This folder will be created via an os.system call. 

**This python script will solve these problems **

1. Retrieve the Illumina reads for the resequencing of K-12 project: https://www.ncbi.nlm.nih.gov/sra/SRX5005282. These are single-end Illumina reads. Your code will retrieve this file; i.e., you cannot just retrieve it.
2. Using SPAdes, assemble the genome. Write the SPAdes command to the log file.
3. Calculate the number of contigs with a length > 1000 and write the # out to the log file as follows:
   
There are # contigs > 1000 in the assembly.
From here on out, you will only consider those contigs > 1000 bp in length.


4. Calculate the length of the assembly (the total number of bp in all of the contigs > 1000 bp in length) and write this # out to the log file as follows:
There are # bp in the assembly.


5. Use GeneMarkS-2 to predict coding regions. You can download this software from: http://exon.gatech.edu/GeneMark/license_download.cgi. You will be given access to two gz files, one is the code, which you should move into your home directory and unpack tar -xf filename.tar.gz. You will also get a key. You need to gunzip filename.gz. Then copy this file to your home directory (command: cp gm_key_64 ~/.gmhmmp2_key). (Note, this key file has to be named gmhmmp2_key and it has to be in your home directory.) Using GeneMarkS-2, output the predicted protein sequences for the identified genes. (If you’re doing #9, you’ll need another file too.).                 


6. GeneMarkS-2 identifies coding regions but doesn’t predict what they are. I’ve created a multi-FASTA format file of E. coli protein sequences. (Actually, I stole it from Prokka.) Query your predicted amino acid sequences (from #5) against these sequences to predict their function. You can find this multi- FASTA format file at: /home/aene/Ecoli.fasta. You can copy it from her folder into yours. Query via BLAST your predicted amino acid sequences in order to identify the predicted function of each. BLAST+ (and all its functions) are accessible to you already. In other words, you don’t have to install anything. Produce an output file called “predicted_functionality.csv”. It should be a csv file formatted as follows: Query sequence ID, Subject sequence ID, % Identity, % Query Coverage
Note, only report the best hit for each of your predicted sequences.

7. The assembled genome in RefSeq for E. coli K-12 (NC_000913) has 4140 CDS and 89 tRNAs annotated. Write to the log file the discrepancy (if any) found. For instance, if my GeneMark annotation predicted 4315 CDS, I would write,
GeneMarkS found 175 additional CDS than the RefSeq.
