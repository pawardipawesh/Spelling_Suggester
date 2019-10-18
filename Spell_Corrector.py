from Dictionary_Utils import DictUtils
import numpy as np
import scipy.spatial.distance
import chars2vec
from flask import Flask, request, render_template,jsonify
from keras import backend as K
from config import *

class SpellCorrector:
    
    def create_dict(self, unigrams_bigrams):
        startChar_to_words_dict={}

        for w in unigrams_bigrams:
            w=w.strip().lower()
            if w=='':
                continue
            start_char=w[0]
            if start_char in startChar_to_words_dict and w not in startChar_to_words_dict[start_char]:
                startChar_to_words_dict[start_char].add(w)
            else:
                candidate_words=set()
                candidate_words.add(w)
                startChar_to_words_dict[start_char]=candidate_words
        return startChar_to_words_dict

    def find_nearest_word(self,candidate_words_distances,candidate_words):
        #print('Inside find_nearest_word')
        word_distances_dict=dict(zip(candidate_words, candidate_words_distances))
        word_distances_sorted=sorted(word_distances_dict.items(), key=lambda kv: kv[1])
        #print(word_distances_sorted)
        return word_distances_sorted[0:5]
    
    def compute_distance(self,candidate_word_vectors, input_word_vector):
        v = input_word_vector.reshape(1, -1)
        
        return scipy.spatial.distance.cdist(candidate_word_vectors, v, 'cosine').reshape(-1)

    def compute_correct_word(self,input_word,startChar_to_words_dict,char_emb_model):
        if input_word=='' or input_word==None:
            return 'Input Word is Empty'
        
        input_word=input_word.strip().lower()
        
        input_word_len=len(input_word)
        max_candidate_len=int(1.5*input_word_len)
        min_candidate_len=int(0.5*input_word_len)
        
        input_word_vector=char_emb_model.vectorize_words([input_word])[0]
        
        candidate_words=[w for w in list(startChar_to_words_dict[input_word[0]]) if len(w)<=max_candidate_len and len(w)>=min_candidate_len]
        candidate_words_vectors=[list(v) for v in char_emb_model.vectorize_words(candidate_words)]
        
        

        candidate_words_distances=list(self.compute_distance(candidate_words_vectors,input_word_vector))
        #print('Candidate Words Distances computed')
        #print('You might want to write any of the following:\n')
        
        return '<br>'.join([word_tuple[0] for word_tuple in self.find_nearest_word(candidate_words_distances,candidate_words)])

app = Flask(__name__)
        
@app.route('/spell_suggest', methods=['GET','POST'])
def my_form_post():
    K.clear_session()
    text1 = request.form['text1']
    word = request.args.get('text1')
    possible_spellings= execute_spell_suggester(text1)
    result = {
        "output": possible_spellings
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
    

def execute_spell_suggester(input_word):
    char_emb_model=chars2vec.load_model(model_path)
    return spell_corrector.compute_correct_word(input_word,startChar_to_words_dict,char_emb_model)



@app.route('/')
def home():
    return render_template('home.html')

print('Please hold on....application is loading....')
spell_corrector = SpellCorrector()
dict_utils_obj = DictUtils()
unique_bi_grams_file = dict_utils_obj.load_file(bigram_dict_path)
unique_bi_grams=unique_bi_grams_file.read().split('\n')
eng_words_file=dict_utils_obj.load_file(eng_word_list_path,'r')
eng_words=eng_words_file.read().split('\n')
unique_bi_grams.extend(eng_words)
startChar_to_words_dict = spell_corrector.create_dict(unique_bi_grams)
print('Loading is done....Please hit localhost:5000 in your browser')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
