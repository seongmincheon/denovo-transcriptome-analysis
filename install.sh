mkdir toolbox
mkdir DB
cd ./toolbox
#install Trimmomatic
wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
#install Trinity
wget https://github.com/trinityrnaseq/trinityrnaseq/archive/Trinity-v2.4.0.tar.gz
#install Transdecoder
wget https://github.com/TransDecoder/TransDecoder/archive/v3.0.0.tar.gz
#install CD-hit
wget https://github.com/weizhongli/cdhit/releases/download/V4.6.7/cd-hit-v4.6.7-2017-0501-Linux-binary.tar.gz
#install blast
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-blast-2.6.0+-x64-linux.tar.gz
#download blastDB(Uniprot)
wget -P ../DB ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz



#unzip
unzip Trimmomatic-0.36.zip
tar -xf Trinity-v2.4.0.tar.gz
tar -xf v3.0.0.tar.gz
tar -xf cd-hit-v4.6.7-2017-0501-Linux-binary.tar.gz
tar -xf ncbi-blast-2.6.0+-x64-linux.tar.gz
gzip -d ../DB/uniprot_sprot.fasta.gz


#making blast DB from Protein database
ncbi-blast-2.6.0+/bin/makeblastdb -in ../DB/uniprot_sprot.fasta -out ../DB/uniprot_sprot.fasta -dbtype prot -parse_seqids


#compile tools
cd ./TransDecoder-3.0.0
make
cd ../trinityrnaseq-Trinity-v2.4.0
make
cd ./trinity-plugins
make




