# denovo-transcriptome-analysis
one-shot  Denovo transcriptome analysis in Linux OS 








We using open source Program
Trinity
TransDecoder
CD-hit
Blast
Unifrot swissprot protein.fasta

and our some parsing scripts







##Reference
https://github.com/trinityrnaseq/trinityrnaseq/wiki
Haas, Brian J., et al. "De novo transcript sequence reconstruction from RNA-seq using the Trinity platform for reference generation and analysis." Nature protocols 8.8 (2013): 1494-1512.












######USAGE#######
Using by Linux shell & Python 2.7


Install
%>sh install.sh


Analysis
%> python Denovo_analysis.py [Left.fq] [Right.fq] [CPU] [Memory]
CPU & Memory is int format




