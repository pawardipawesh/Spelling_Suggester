## Context Independent Unsupervised Spelling Suggestor for misspelled word using Pretrained Character Embeddings

**About**

Application expects word with spelling mistake as input and returns top 5 possible corrections of it. These corrections are ordered in 
decreasiasing order of their probability of correct version of input

e.g. 

*Input Word* : homogenious

*Suggested Spelling corrections:*

- homogeneousness
- homogeneous
- homogenesis
- homoecious
- honoribus

**Reuirements**

Please install libraries using requirements.txt and download dictionaries
- [Unique Bigrams](https://drive.google.com/file/d/1_HaGierUJNIj1fPrW5IjMPIQecNVM_DT/view?usp=sharing)
- [English Word List](https://drive.google.com/file/d/1lprx1kDcERFtokKqQYxpiH_GkS6vn7d4/view?usp=sharing)

**Approach**

Here, I have tried to use word level information that charcter embeddings provide to come up with words which are closer to input word. 
[chars2vec project](https://github.com/IntuitionEngineeringTeam/chars2vec) has trained LSTM based architecture on the pair of similar and non-similar words with objective of having proximal vectors for similar words. Hence I have used it to encode words with their pretrained character embeddings.

**Algorithm**

```

Build dictionary of english words 
Create Map which maps character to words that starts with it
Fetch words from Map which starts with character with which input words starts (candidate words)
Compute input word embedding using pretrained character embedding model
Compute embedding for each candidate word
Compute cosine distance between input word embedding and each candidate word embedding
Ceturn top 5 candidate words which are closest to input word
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
- If input word has spelling mistake at start, It fails
- If correct word is absent in used dictionaries, It fails
- Context is absent so can not suggest exact correct spelling

**Possible Improvements**
- consider all words in dictionary as candidate words( high complexity)
- Use some heuristic to reduce number of candidate ( Here I have used candidate word should start with same char as that of input word. 
Other could be edit distance based candidate computation)
- Third limitation could be avoided by using LSTMs based Encoder Decoder framework with sentence consisting of misspelled words as input and sentence with 
correct words as output. This would enable us to suggest exact correct spelling of input word by considering context in which input word appears.

**Acknowledgement**
- I would like to thank [chars2vec project](https://github.com/IntuitionEngineeringTeam/chars2vec) contributors. This prevented one additional task of training 
character embedding and helped in building first initial version in really quick time.
- Secondly I have prepared unique bigrams dictionary using wikipedia based corpus. I will soon provide link from where I have taken it.
- I have taken english word list from [english word list source](http://www-personal.umich.edu/~jlawler/wordlist.html)
