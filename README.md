## Context Independent Unsupervised Spelling Suggester for misspelled word using Pretrained Character Embeddings

**About**

Application expects word with spelling mistake as input and returns top 5 possible corrections of it. These corrections are ordered in 
decreasing order of their probability of being a correct version of input.

e.g. 

*Input Word* : 
- homogenious

*Suggested Spelling corrections with their probability:*

- homogeneousness, 0.76
- homogeneous, 0.67
- homogenesis, 0.56
- homoecious, 0.45
- honoribus, 0.34

**Reuirements**

Please install libraries using requirements.txt and download dictionaries
- [Unique Bigrams](https://drive.google.com/file/d/1_HaGierUJNIj1fPrW5IjMPIQecNVM_DT/view?usp=sharing)
- [English Word List](https://drive.google.com/file/d/1lprx1kDcERFtokKqQYxpiH_GkS6vn7d4/view?usp=sharing)

**Approach**

Here, I have tried to use word level information that charcter embeddings provide to come up with words which are closer to input word. 
[chars2vec project](https://github.com/IntuitionEngineeringTeam/chars2vec) has trained LSTM based architecture on the pair of similar and non-similar words with objective of having proximal vectors for similar words. Hence I have used it to encode words with their pretrained character embeddings.

**Algorithm**

```

- Build dictionary of English words 
- Create Map which maps character to words that starts with it
- Fetch words from Map starting with first character of input word (candidate words)
- Compute input word embedding using pretrained character embedding model
- Compute embedding for each candidate word
- Compute cosine distance between input word embedding and each candidate word embedding
- Return top 5 candidate words which are closest to input word
```

**How to run**

- Download project
- install dependencies
- download dictionaries
- provide dictionaries and pretrained model path in config.py
- run Spell_Corrector.py with 
```
python Spell_Corrector.py
```
It will run web app at address 
```
localhost:5000
```

**Limitations**
- If first character of input word has spelling mistake, It fails
- If correct word is absent in dictionary, It fails
- Context is not considered, so can not suggest only one exact correction

**Possible Improvements**
- consider all words in dictionary as candidate words(high complexity)
- Use some heuristic to reduce number of candidate (Here, I have used candidate word should start with same char as that of input word as heuristic. 
Other could be edit distance based candidate computation)
- Third limitation could be avoided by using LSTM based Encoder Decoder framework with sentence consisting of mis-spelled words as input and sentence with 
correct words as output. This would enable us to suggest only one correct spelling of input word.

**Acknowledgement**
- I would like to thank [chars2vec project](https://github.com/IntuitionEngineeringTeam/chars2vec) contributors. It prevented one additional task of training character embeddings and helped in building first initial version in really quick time.
- Secondly, I have prepared unique bigrams dictionary using wikipedia based corpus. I somehow lost the link to it, will soon provide it.
- I have taken english word list from [english word list source](http://www-personal.umich.edu/~jlawler/wordlist.html)
