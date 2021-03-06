from textblob import TextBlob
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

blob = TextBlob(text)
print(blob.tags)

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)

print(blob.ngrams(n=5))