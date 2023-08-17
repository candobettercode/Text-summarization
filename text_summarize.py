import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation 
from heapq import nlargest

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    tokens = [token.text for token in doc]
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    max_freq = max(word_freq.values())
    # calculate normalize frequency
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq
    sent_tokens = [sent for sent in doc.sents]
    sent_score = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = word_freq[word.text]
                else:
                    sent_score[sent] += word_freq[word.text]
    select_len = int(len(sent_tokens) *0.3)
    summary = nlargest(select_len,sent_score, key=sent_score.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    return summary, rawdocs, len(summary.split(' ')), len(rawdocs.split(' '))