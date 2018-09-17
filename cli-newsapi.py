from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator, style_from_dict, Token

import requests


style = style_from_dict({
   Token.QuestionMark: '#FF9D00 bold',
   Token.Instruction: '',  # default
   Token.Answer: '#5F819D bold',
   Token.Separator: '#cc5454',
   # Token.Separator: '#6C6C6C',
   Token.QuestionMark: '#FF9D00 bold',
   Token.Selected: '',
   Token.Pointer: '#FF9D00 bold',
   Token.Instruction: '',  # default
   Token.Question: '',
})
print('Hi, welcome to News Sources')
question = [
    {
        'type': 'rawlist',
        'name': 'news_source',
        'message': 'what is your favourite news source',
        'choices':['espn', 'abc-news', 'al-jazeera-english', 'cnn']
    }
]
response = prompt(question, style=style)

# getting selected news source 
response_value = response['news_source']
print(response_value)

if response_value:
    url = 'https://newsapi.org/v2/top-headlines?apiKey=8b877ab77a914ef0910d6c5c04d2a4aa&sources='+response_value+'&pageSize=10'
    call = requests.get(url)
    print('status:', call.status_code)
    response_data = call.json()

    headlinearticles = response_data['articles']

y = headlinearticles
for article in y:
    # print("Headline count : ", article_count, "\n")
    print("Title : ", article['title'])
    print("Description : ", article['description'])
    print("url : ", article['url'], "\n")