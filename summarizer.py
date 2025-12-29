myText= "The Madras High Court has suggested to the Centre explore the possibility of passing Australia-like legislation banning social media for children under the age of 16. The Madurai bench of the High Court also directed the authorities concerned to accelerate their awareness campaign more effectively and take the message to the vulnerable group through all available media till such a law comes into effect. Australia, on December 10, became the first country in the world to ban social media for children under 16, a decision welcomed by many parents and child rights groups. A bench comprising Justice G Jayachandran and Justice KK Ramakrishnan suggested this to the Centre while disposing of a Public Interest Litigation (PIL) raising the issue of easy availability of pornographic content to children on social media and seeking a direction to the authorities to implement the direction of the Centre to the internet service providers for providing “Parental Window” service and create awareness among the children."
splitted_sentences = myText.split(".")
cleaned_sentences = []
for s in splitted_sentences :
    cleaned = s.strip()
    if cleaned != "" :
        cleaned_sentences.append(cleaned)

print(cleaned_sentences)
