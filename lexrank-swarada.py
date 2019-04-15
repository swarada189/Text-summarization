from lexrank.algorithms.summarizer import LexRank 
from lexrank.mappings.stopwords import STOPWORDS
from nltk.tokenize import sent_tokenize
from path import Path

documents = []
sentences = []
doc = []

#for file naming conventions
filename = input("Enter file name : ")                                  	#assign topic no. acc to topic                        
if filename == 'England_pensioners.txt':
    topic_no =1
elif filename == 'England_strike_miner-1.txt':
    topic_no =2
elif filename == 'Scotland_peterhead.txt':
    topic_no =3
else:
    topic_no =4
    
documents_dir = Path('./Documents')
for file_path in documents_dir.files(filename):

    with file_path.open(mode='rt', encoding='utf-8') as fp:
        for line in fp.readlines():
            if line == '\n':                                                             #in given txt file, new article(doc) starts after newline
                doc = []
            if len(line)>100:                                                            #skip adding heading of articles
                documents.append(sent_tokenize(line))
#print(documents)


for doc in documents:
    for sent in doc:
        sentences.append(sent)
#print(sentences)


lxr = LexRank(documents, stopwords=STOPWORDS['en'])

# get summary with classical LexRank algorithm
summary = lxr.get_summary(sentences, summary_size=5, threshold=.1)
print(summary)

n=str(topic_no)
filename = './topic'+n+'_system1.txt'                                           #name file according to topic no. assigned
with open(filename,mode="w",encoding='utf-8') as fp:
    for sent in summary:                                                        #format output file (1 sentence of summary in 1 line)
        fp.write(sent)
        fp.write('\n')

# get summary with continuous LexRank
summary_cont = lxr.get_summary(sentences, threshold=None)
print(summary_cont)



# get LexRank scores for sentences
# 'fast_power_method' speeds up the calculation, but requires more RAM
scores_cont = lxr.rank_sentences(
    sentences,
    threshold=None,
    fast_power_method=False,
)
print(scores_cont)

