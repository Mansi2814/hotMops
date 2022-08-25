from nrclex import NRCLex
import os
import numpy as np
import pandas as pd
import re
import nltk
# nltk.download('punkt')
from nltk.tokenize import RegexpTokenizer
# from nltk import tokenizers
import spacy
import string
import re
import vaderSentiment
# For viz
import seaborn as sns
from collections import Counter

# calling SentimentIntensityAnalyzer object
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

remove_emotions = set(['anticipation', 'trust', 'surprise', 'positive', 'joy'])

danger_level = {'negative': 'less_immediate', 'fear': 'immediate', 'anger': 'slightly_minor', 'sadness': 'very_minor',
                'disgust': 'moderate'}

priority_level = {'negative': 4, 'fear': 5, 'anger': 2, 'sadness': 1, 'disgust': 3}


def priority(x):
    text = NRCLex(x)
    return_val = None
    for emote in text.top_emotions:
        if emote[0] in remove_emotions:
            continue
        elif emote[0] == 0.0:
            return_val = "No emotion"
        else:
            return_val = priority_level[emote[0]] + emote[1]
    if return_val is None:
        return 1
    return return_val


def complaintAnalyzer(sentence):
    text = NRCLex(sentence)
    text.top_emotions = [('fear', 0.0), ('anger', 0.0), ('anticip', 0.0), ('sadness', 0.0), ('disgust', 0.0)]
    priority_no = priority(sentence)
    priority_no = round(priority_no, 2)
    return priority_no
