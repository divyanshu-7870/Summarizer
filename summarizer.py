myText= "The Madras High Court has suggested to the Centre explore the possibility of passing Australia-like legislation banning social media for children under the age of 16. The Madurai bench of the High Court also directed the authorities concerned to accelerate their awareness campaign more effectively and take the message to the vulnerable group through all available media till such a law comes into effect. Australia, on December 10, became the first country in the world to ban social media for children under 16, a decision welcomed by many parents and child rights groups. A bench comprising Justice G Jayachandran and Justice KK Ramakrishnan suggested this to the Centre while disposing of a Public Interest Litigation (PIL) raising the issue of easy availability of pornographic content to children on social media and seeking a direction to the authorities to implement the direction of the Centre to the internet service providers for providing “Parental Window” service and create awareness among the children."
splitted_sentences = myText.split(".")
cleaned_sentences = []
for s in splitted_sentences :
    cleaned = s.strip()
    if cleaned != "" :
        cleaned_sentences.append(cleaned)
#analysis = "The Madras High Court has suggested to the Centre explore the possibility of passing Australia-like legislation banning social media for children under the age of 16. The Madurai bench of the High Court also directed the authorities concerned to accelerate their awareness campaign more effectively and take the message to the vulnerable group through all available media till such a law comes into effect. Australia, on December 10, became the first country in the world to ban social media for children under 16, a decision welcomed by many parents and child rights groups. A bench comprising Justice G Jayachandran and Justice KK Ramakrishnan suggested this to the Centre while disposing of a Public Interest Litigation (PIL) raising the issue of easy availability of pornographic content to children on social media and seeking a direction to the authorities to implement the direction of the Centre to the internet service providers for providing “Parental Window” service and create awareness among the children."
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

#print(cleaned_sentences)
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
        

summary_len = max(1, int(len(sentence_score))*0.3)

sorted_sentence_score = sorted(sentence_score.items(),key= lambda x: x[1],reverse=True)

print(sorted_sentence_score)







#print(cleaned_sentences)
