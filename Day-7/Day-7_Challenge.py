# - Count word frequencies in a text file
f=open("demofile.txt","r")
text=f.read()
f.close()

text=text.lower()
words=text.split()

freq={}

for word in words:
    word=word.strip('.,!?":;')

    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
    for word in freq:
        print(word," ",freq[word])
