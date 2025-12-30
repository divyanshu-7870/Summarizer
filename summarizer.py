myText = input("Put the Blog below :")
splitted_sentences = myText.split(".")

def text_cleaning (sentence): # empty spaces removal
    cleaned = []
    for s in sentence :
      sentence_stripped = s.strip()
      if sentence_stripped != "" :
        cleaned.append(sentence_stripped)
    return cleaned    

cleaned_sentences = text_cleaning(splitted_sentences)

analysis = myText.lower()

signs =[",","-","(",")","'",'"',"."]

for p in signs:
    analysis = analysis.replace(p," ")

words =analysis.split()

stop_words= ["the","is","to","of","and","for","in","on","under","a",'']
without_stopWords =[]
for p in words:
    if p not in stop_words:
        without_stopWords.append(p)


wordcount= {}
for p in without_stopWords:
    if p in wordcount:
        wordcount[p]+=1
    else :
        wordcount[p]=1
worditems=wordcount.items()   

def getcount(wordcount):
    return wordcount[1]

sorted_wordcount = sorted(worditems,key = lambda x: x[1], reverse= True)


sentence_score = {}
for s in cleaned_sentences:
    score=0
    temp= s.lower()
    for k in signs:
        temp= temp.replace(k,"")

    sentencewords = temp.split()

    for a in sentencewords:
        if a in wordcount and a!="":
            score += wordcount[a]
    sentence_score[s] = score        
        

summary_len = max(1, int(len(sentence_score)*0.3))

sorted_sentence_score = sorted(sentence_score.items(),key= lambda x: x[1],reverse=True)

top_sentences = sorted_sentence_score[:summary_len]

final_summary=[]

for s in cleaned_sentences:
    for ts,_ in top_sentences:
        if s == ts:
            final_summary.append(s)

print("\nSummary :\n")
for s in final_summary:
    print(s," ")






