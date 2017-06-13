import datetime
import sys
import subprocess
import os
import glob
import time

os.system("clear")
time.sleep(2)

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print " " 
print "RUNNING AT ",
print(nowDatetime)  # 2015-04-19 12:11:32
time.sleep(1)

### Argv checking'

print "-------------------------------------------------------------------------------------"
time.sleep(0.1)
print " " 
time.sleep(0.1)
print "     _    _   _    _    _  __   ______ ___ ____         ____ _____  _    ____ _____  "
time.sleep(0.1)
print "    / \  | \ | |  / \  | | \ \ / / ___|_ _/ ___|       / ___|_   _|/ \  |  _ \_   _| " 
time.sleep(0.1)
print "   / _ \ |  \| | / _ \ | |  \ V /\___ \| |\___ \       \___ \ | | / _ \ | |_) || |   "
time.sleep(0.1)
print "  / ___ \| |\  |/ ___ \| |___| |  ___) | | ___) |       ___) || |/ ___ \|  _ < | |   " 
time.sleep(0.1)
print " /_/   \_\_| \_/_/   \_\_____|_| |____/___|____/       |____/ |_/_/   \_\_| \_\|_|   "
time.sleep(0.1)
print " "
time.sleep(0.1)
print " " 
time.sleep(0.1)
print "-------------------------------------------------------------------------------------"

time.sleep(3)

if len(sys.argv) != 5:
    print "\n------------------------\nUSAGE :: python Denovo_analysis.py [Left.fq] [Right.fq] [CPU] [Memory(Gb)] \n ------------------------"
    exit()


Left_fq = sys.argv[1]
Right_fq = sys.argv[2]
CPU = sys.argv[3]
Memory = sys.argv[4] + "G"

Home = subprocess.check_output("pwd", shell=True)
HomeDir = Home.split()[0]


os.system("mkdir Trim_out")
for i in range(30):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()

print " "
print " GENERATE [Trim_out] DIRECTORY!"
os.system("mkdir Trim_out/unpaired")
time.sleep(1)
for i in range(30):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()

print " "
print " GENERATE [Trim_out/unpaired] DIRECTORY!"
time.sleep(1)
for i in range(30):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()
print " "
print " "
print " "
print "NEXT STEP LOADING.."
time.sleep(3)
os.system("clear")

print "-----------------------------------------------------------------"
print " " 
print "   ___              _ _ _             ____ _               _     "
print "  / _ \ _   _  __ _| (_) |_ _   _    / ___| |__   ___  ___| | __ "
print " | | | | | | |/ _` | | | __| | | |  | |   | '_ \ / _ \/ __| |/ / "
print " | |_| | |_| | (_| | | | |_| |_| |  | |___| | | |  __/ (__|   <  "
print "  \__\_\\__,_|\__,_|_|_|\__|\__, |   \____|_| |_|\___|\___|_|\_\ "
print " "
print " " 
print "-----------------------------------------------------------------"

time.sleep(3)

### Trimmomatic START-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
minLen = 36


# read length estimation
B = subprocess.check_output("head -n 2 " + Left_fq + " |wc " , shell=True)
A = subprocess.check_output("head -n 1 " + Right_fq + " |wc " , shell=True)

readLength = int(B.split()[2]) - int(A.split()[2])

if readLength >= 151:
    minLen = 50

Fs = Left_fq.split("raw/")
Rs = Right_fq.split("raw/")



os.system("java -jar " + HomeDir + "/toolbox/Trimmomatic-0.36/trimmomatic-0.36.jar PE -phred33 " + Left_fq + " " + Right_fq + " Trim_out/Trim_out_paired_" + Fs[1] + " Trim_out/unpaired/Trim_out_unpaired_" + Fs[1] + " Trim_out/Trim_out_paired_" + Rs[1] + " Trim_out/unpaired/Trim_out_unpaired_" + Rs[1] + " ILLUMINACLIP:TruSeq3-PE-2.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:" + str(minLen))
time.sleep(5)

for i in range(50):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()

print " "
print " "
print " "
print "NEXT STEP LOADING .."
time.sleep(3)
time.sleep(1)
os.system("clear")

### Trimmomatic END-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


print "------------------------------------------------------------------------------"
print " " 
print "  _____     _       _ _           ____                ____  _             _   "
print " |_   _| __(_)_ __ (_) |_ _   _  |  _ \ _   _ _ __   / ___|| |_ __ _ _ __| |_ "
print "   | || '__| | '_ \| | __| | | | | |_) | | | | '_ \  \___ \| __/ _` | '__| __|"
print "   | || |  | | | | | | |_| |_| | |  _ <| |_| | | | |  ___) | |_ (_| | |  | |_ "
print "   |_||_|  |_|_| |_|_|\__|\__, | |_| \_\\__,_|_| |_| |____/ \__\__,_|_|   \__|"
print "                          |___/                                               "
print " " 
print "------------------------------------------------------------------------------"

time.sleep(5)

### Trinity START----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


os.system(HomeDir + "/toolbox/trinityrnaseq-Trinity-v2.4.0/Trinity --seqType fq --left Trim_out/Trim_out_paired_" + Fs[1] + " --right Trim_out/Trim_out_paired_" + Rs[1] + " --output trinity_output --CPU " + CPU + " --max_memory " + Memory + " --bypass_java_version_check")


time.sleep(5)

for i in range(50):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()

print " "
print " "
print " "
print "NEXT STEP LOADING .."
time.sleep(3)
os.system("clear")

### Trinity END------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


print "---------------------------------------------------------------------------------------------------------------"
print " " 
print "  _____                    ____                     _             ____                ____  _             _   "
print " |_   _| __ __ _ _ __  ___|  _ \  ___  ___ ___   __| | ___ _ __  |  _ \ _   _ _ __   / ___|| |_ __ _ _ __| |_ "
print "   | || '__/ _` | '_ \/ __| | | |/ _ \/ __/ _ \ / _` |/ _ \ '__| | |_) | | | | '_ \  \___ \| __/ _` | '__| __|"
print "   | || | | (_| | | | \__ \ |_| |  __/ (__ (_) | (_| |  __/ |    |  _ <| |_| | | | |  ___) | |_ (_| | |  | |_ "
print "   |_||_|  \__,_|_| |_|___/____/ \___|\___\___/ \__,_|\___|_|    |_| \_\\__,_|_| |_| |____/ \__\__,_|_|   \__|"
print " " 
print " " 
print "--------------------------------------------------------------------------------------------------------------"

# making directory TransDeocoder and moving
os.system("mkdir TransDecoder")
for i in range(30):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()

print " "
print " GENERATE [TransDecoder] DIRECTORY!"
time.sleep(1)

time.sleep(5)

### TransDecoder START----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# LongestORF
os.system(HomeDir + "/toolbox/TransDecoder-3.0.0/TransDecoder.LongOrfs -t " + HomeDir + "/trinity_output/Trinity.fasta")

# Homology Search
os.system(HomeDir + "/toolbox/ncbi-blast-2.6.0+/bin/blastp -query " + HomeDir + "/Trinity.fasta.transdecoder_dir/longest_orfs.pep -db " + HomeDir + "/DB/uniprot_sprot.fasta -evalue 1e-5 -num_threads " + CPU + " -max_target_seqs 1 -outfmt 6 > " + HomeDir + "/Trinity.fasta.transdecoder_dir/blastp.outfmt")

# Prediction
os.system(HomeDir + "/toolbox/TransDecoder-3.0.0/TransDecoder.Predict -t " + HomeDir + "/trinity_output/Trinity.fasta --retain_blastp_hits " + HomeDir + "/Trinity.fasta.transdecoder_dir/blastp.outfmt --single_best_orf --cpu " + CPU)

### TransDecoder END------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



### CD-HIT START----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

os.system(HomeDir + "/toolbox/cd-hit-v4.6.7-2017-0501/cd-hit -i " + HomeDir + "/Trinity.fasta.transdecoder.pep -o "  + HomeDir + "/Trinity.fasta.transdecoder.pep.cdhit -c 0.99 -n 5 -T " + CPU)

### CD-HIT END-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


time.sleep(5)

for i in range(50):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()
time.sleep(1)
time.sleep(1)
print " "
print " "
print " "
print "NEXT STEP LOADING .."
time.sleep(3)
os.system("clear")



### Annotation START-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print "------------------------------------------------"
print " " 
print "  ____  ____    ____                      _     "
print " |  _ \| __ )  / ___|  ___  __ _ _ __ ___| |__  "
print " | | | |  _ \  \___ \ / _ \/ _` | '__/ __| '_ \ "
print " | |_| | |_) |  ___) |  __/ (_| | | | (__| | | |"
print " |____/|____/  |____/ \___|\__,_|_|  \___|_| |_|"
print " " 
print " " 
print "------------------------------------------------"

time.sleep(5)
print "DATABASE UPLOADING"
os.system(HomeDir + "/toolbox/ncbi-blast-2.6.0+/bin/blastp -query " + HomeDir + "/Trinity.fasta.transdecoder.pep.cdhit -db " + HomeDir + "/DB/uniprot_sprot.fasta -evalue 1e-10 -num_threads " + CPU + " -max_target_seqs 1 -outfmt 7 > " + HomeDir + "/Annotation_blastp_out_7")

time.sleep(5)

for i in range(50):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()



### Annotation END--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### BLAST_Parsing
import sys
import glob
import subprocess
import os

BLAST_out7 = HomeDir + "/Annotation_blastp_out_7"

f = open(BLAST_out7, 'r')
o = open(BLAST_out7.split("7")[0] + "6", 'w')
line = f.readline()
while 1:
	if not line:
		break
	if line.count('#') ==0:
		o.write(line)
		while 1:
			line = f.readline()
			if line.count('#') ==1:
				line = f.readline
			else : break
	else:
		line = f.readline()

f.close()
o.close()

# Hits and No hits separation

A = open(BLAST_out7 , 'r')
B = open(BLAST_out7.split("7")[0] + "hits", 'w')
C = open(BLAST_out7.split("7")[0] + "nohits", 'w')

Aline = A.readline()
N = '\n'

while 1:
	if not Aline:
		break
	
	if Aline.count("# " + sys.argv[2]) ==1:
		AlineQ = A.readline()
		AQs = AlineQ.split()
		ID = AQs[2]
		AlineD = A.readline()
		AlineH = A.readline()
		
		
		
		if AlineH.count("# 0 hits found") ==1:
			C.write(ID)
			C.write(N)
			Aline = A.readline()		
	
		else:
			B.write(ID)
			B.write(N)
			Aline = A.readline()
			



	else:
		Aline = A.readline()

A.close()
B.close()
C.close()


#hits_DB_ID

A = open(BLAST_out7 , 'r')
o = open(BLAST_out7.split("7")[0] + "hits_DB_ID", 'w')

while 1:
    Aline = A.readline()
    if not Aline:
        break
    if Aline.count(" hits found") != 0:

        if Aline.count("# 0 hits found") == 1:
            continue
        else:
            Aline = A.readline()
            o.write(Aline)

A.close()
o.close()

# hits_DB_ID File + Add_ORF_Length

F = glob.glob("*.transdecoder.pep.cdhit")

if len(F) != 1:
        print " WARNING: There is NO or Multi [Trinity.fasta.transdecoder.pep.cdhit] File "
        exit()


os.system("cat " + F[0] + " |grep " + '">"' + " > " + F[0] + "_ID")    # cdhit > cdhit_ID


A = open(F[0] + "_ID" , 'r') # cdhit_ID

Adic = {}

while 1:
        Aline = A.readline()
        if not Aline:
                break
        
        TrinityID = Aline.split(":")[2]
        ORF_Length = Aline.split()[4].split(":")[1]

        Adic[TrinityID] = ORF_Length

B = open(BLAST_out7.split("7")[0] + "hits_DB_ID" , 'r') # hits_DB_ID
o = open(BLAST_out7.split("7")[0] + "hits_DB_ID_Add_Length" , 'w') # hits_DB_ID_Add_Length

while 1:
        Bline = B.readline()
        if not Bline:
                break
        o.write(Adic[Bline.split(":")[2]] + '\t' + Bline)

A.close()
B.close()
o.close()

os.system("cat " + HomeDir + "/Annotation_blastp_out_hits_DB_ID")
time.sleep(10)
for i in range(50):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()

print " "
print " "
print " "
print "NEXT STEP LOADING .."
print " " 
time.sleep(3)
os.system("clear")

"""

# hits_DB_ID_Add_Length >>> hits_DB_ID_Add_Length_SortN
os.system("cat " + BLAST_out7.split("7")[0] + "hits_DB_ID_Add_Length |sort -k 1 -n -r > " + BLAST_out7.split("7")[0] + "hits_DB_ID_Add_Length_SortN")


# hits_DB_ID_Add_Length_SortN  >>> hits_DB_ID_Sort_Gene
os.system("cat " + BLAST_out7.split("7")[0] + "hits_DB_ID_Add_Length_SortN |cut -f 3 |cut -d " + '"|"' + " -f 3 |cut -d " + '"_"' + " -f 1 |sort -u > " + BLAST_out7.split("7")[0] + "hits_DB_ID_Sort_Gene")
        
# LongestORF!!

A = open(BLAST_out7.split("7")[0] + "hits_DB_ID_Sort_Gene", 'r')
o = open(BLAST_out7.split("7")[0] + "hits_DB_ID_LongestORF", 'w')
while 1:
        Aline = A.readline()
        if not Aline:
                break

        B = open(BLAST_out7.split("7")[0] + "hits_DB_ID_Add_Length_SortN" , 'r')

        while 1:
                Bline = B.readline()
                if not Bline:
                        break

                if Aline.split()[0] == Bline.split()[2].split("|")[2].split("_")[0]:
                        o.write(Bline)
                        break
"""
print "---------------------------------------"
print " " 
print "  _____ _       _     _              _ "
print " |  ___(_)_ __ (_)___| |__   ___  __| |"
print " | |_  | | '_ \| / __| '_ \ / _ \/ _` |"
print " |  _| | | | | | \__ \ | | |  __/ (_| |"
print " |_|   |_|_| |_|_|___/_| |_|\___|\__,_|"
print " "
print " " 
print "---------------------------------------"

time.sleep(5)
for i in range(50):
    dot = "."
    sys.stdout.write("\r" +  dot*i)
    time.sleep(0.02)
    sys.stdout.flush()

print " "
print " "
print " "
print "WRITING FILES .."
print " " 
time.sleep(3)
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print "FINISHED",
print(nowDatetime)  # 2015-04-19 12:11:32
time.sleep(3)
print "  ____                                                                     ___                                          _       "
print " | __ ) _   _     ___ _   _ _ __   __ _        __ ___      _____  _ __    ( _ )    ___  ___  ___  _ __   __ _ _ __ ___ (_)_ __  "
print " |  _ \| | | |   / __| | | | '_ \ / _` |_____ / _` \ \ /\ / / _ \| '_ \   / _ \/\ / __|/ _ \/ _ \| '_ \ / _` | '_ ` _ \| | '_ \ "
print " | |_) | |_| |   \__ \ |_| | | | | (_| |_____| (_| |\ V  V / (_) | | | | | (_>  < \__ \  __/ (_) | | | | (_| | | | | | | | | | |"
print " |____/ \__, |   |___/\__,_|_| |_|\__, |      \__, | \_/\_/ \___/|_| |_|  \___/\/ |___/\___|\___/|_| |_|\__, |_| |_| |_|_|_| |_|"
print "        |___/                     |___/       |___/                                                     |___/"




