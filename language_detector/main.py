# -*- coding: utf-8 -*-
"""
    1. We create a dictionay to keep the common word count for each of the languages
       scan_result = { language : common_words_cumulative_count }
       
    2. we have another dictionary to keep the count of common words found in the text
       language_result = {common_word_for_the_language: count]
       
    3. we select a language, one by one get  the common words for the language and 
      for each common word find how many times it appears in the text. Add the 
      key (in this case the common word) and the value (the count) into the language result 
      dictionary. 
      Once we have gone thorugh all the common words we add all counts to get the 
      cumulative count for that language. Add this entry to the scan result dictionary
      
    4. Repeat step 3 for all languages
    
    5. Now fromthe scan_result disctionary find the language with the highest cumulative count.
"""
import operator
"""This is the entry point of the program."""
from language_detector.languages import LANGUAGES

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    scan_result = {}#{ language : common_words_cumulative_count }
    for lng in LANGUAGES:
        common_cnt = 0 
        for common_word in lng['common_words']:
           cnt = text.split().count(common_word)
           if cnt > 0:
               common_cnt+=cnt
        scan_result[lng['name']]= common_cnt
    language = sorted(scan_result.iteritems(),key=operator.itemgetter(1),reverse=True)[0][0]
    return language