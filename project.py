import string 
sonnet = [
    'Shall I compare thee to a summer’s day?',
    'Thou art more lovely and more temperate:',
    'Rough winds do shake the darling buds of May,',
    'And summer’s lease hath all too short a date:',
    'Sometime too hot the eye of heaven shines,',
    'And often is his gold complexion dimmed,',
    'And every fair from fair sometime declines,',
    'By chance, or nature’s changing course untrimmed:',
    'But thy eternal summer shall not fade,',
    'Nor lose possession of that fair thou ow’st,',
    'Nor shall death brag thou wand’rest in his shade,',
    'When in eternal lines to time thou grow’st,',
    'So long as men can breathe or eyes can see,',
    'So long lives this, and this gives life to thee.'
]

new_list=[]
words = []
trans = str.maketrans('','',string.punctuation + "’")
for line in sonnet:
    new_list = line.lower().translate(trans)
    
    for w in new_list.split():
        words.append(w)
print(words)

positive_words = ['more',
    'lovely',
    'darling',
    'fair',
    'eternal',
    'lives',
    'life',
    'gold',
    'shines' 
]

negative_words = [
    'rough',
    'dimmed',
    'declines',
    'lose',
    'death'
]


score = 0

for X in words:
    if X in positive_words:
        score +=1
    elif X in negative_words:
        score -=1


if score > 0:
    print(f"the score {score} is positive")
elif score < 0:
    print(f"the score {score} is negative")
else:
    print(f"the score {score} is Neutral")