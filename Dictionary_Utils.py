#!/usr/bin/env python
# coding: utf-8

# In[16]:


import sys
from nltk.util import ngrams
from nltk.corpus import stopwords
from IPython.display import clear_output

class DictUtils():
    
    def load_file(file_path,mode='r',encoding='utf8'):
        i=0
        while True:
            try:
                file=open(file_path,mode,encoding=encoding,errors='ignore')
                return file
            except IOError:
                if i<5:
                    i+=1
                else:
                    raise IOError("Your main directory is not consisting of file: "+file_path)
    
    def write_file(file,content,sep):
        i=0
        while i<5:
            try:
                file.write(content+sep)
                return
            except IOError:
                i+=1
                pass
            
    def close_file(file):
        i=0
        while True:
            try:
                file.close()
                return
            except IOError:
                    if i<5:
                        i+=1
                    else:
                        raise IOError("Unable to close file: "+file_path)
                
        

    def get_line_bigrams(line,stop_words):
        tokenized_clean_line=[w for w in line.split() if w.isalpha()]
        valid_ngrams=set([ngram for ngram in set([ng[0]+' '+ng[1] for ng in ngrams(tokenized_clean_line,2)])if ngram.split()[0] 
                      not in stop_words and ngram.split()[1] not in stop_words])
        return valid_ngrams
    
    def write_bigrams(input_file,output_file):
        
        wikidata_file=load_file(input_file,'r')
        bigram_file=load_file(output_file,'w')

        stop_words=set(stopwords.words('english'))
        lines=wikidata_file.readlines()
        no_lines=len(lines)
        no_lines_processed=0
        
        for line in lines:
            line_bigrams=get_line_bigrams(line,stop_words)

            write_file(bigram_file,bg,'\n')

            no_lines_processed+=1
            if no_lines_processed%1000==0:
                bigram_file.flush()

                clear_output()
                print('No Of Lines Processed: '+str(no_lines_processed))
                print('Percentage Of task completed: '+str((no_lines_processed/30749930)*100))
        close_file(bigram_file)


# In[ ]:





# In[ ]:




