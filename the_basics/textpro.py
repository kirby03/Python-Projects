def sentence_maker(phrase):
    sentence = phrase.capitalize()
    questions = ('how', 'what', 'where', 'when', 'why', 'who', 'is', 'are')
    if phrase.startswith(questions):
        return(f"{sentence}?")
    else:
        return(f"{sentence}.")

result = []

while True:
    user_input = input('Say something: ')
    if user_input == '\end':
        break
    else:
        result.append(sentence_maker(user_input))

print(' '.join(result))