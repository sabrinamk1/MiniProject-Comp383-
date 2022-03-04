from Bio import SeqIO
from Bio.Sequencing import Ace
import subprocess


from pathlib import Path

# home would contain something like "/Users/jame"
home = str(Path.home())

path = home + "/Desktop/MiniProject/Results/"




sra_number = "SRR8185310"


print ("Currently downloading: " + sra_number)
prefetch = "prefetch " + sra_number
print ("The command used was: " + prefetch)
subprocess.call(prefetch, shell=True)


print ("Generating fastq for: " + sra_number)


#non hard coded 

fastQFile= home

fastq_dump = "fastq-dump --outdir /Users/sabrinalutfiyeva/Desktop/MiniProject/Results/ --gzip --skip-technical  --readids --read-filter pass --dumpbase --split-3 /Users/sabrinalutfiyeva/Desktop/MiniProject/SRAdata/sra/" + sra_number + ".sra"
print ("The command used was: " + fastq_dump)
subprocess.call(fastq_dump, shell=True)
#got this off of internet



getAssembly = "/Users/sabrinalutfiyeva/Downloads/SPAdes-3.15.4-Darwin/bin/spades.py	-k	55,77,99,127	-t	2	--only-assembler	-s/Users/sabrinalutfiyeva/Desktop/MiniProject/SRAdata/SRR8185310_pass.fastq.gz	-o	/Users/sabrinalutfiyeva/Desktop/MiniProject/SRAdata/SRA_assembly"
subprocess.call(getAssembly, shell =True)


contigList1000= []


with open("/Users/sabrinalutfiyeva/Desktop/MiniProject/Results/contigs.fasta") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        if len(record.seq) > 1000:
            contigList1000.append(record)

number1000 = ("There are %i contigs > 1000 in the assembly" % len(contigList1000))
print(number1000)

