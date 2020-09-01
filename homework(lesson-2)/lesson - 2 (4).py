user_sentence = input('Пользователь, введите строку из нескольких слов, запятыми пренебречь')
words_chets = 1
for words in user_sentence.split():
    print(f'[{words_chets}] {words[:10]}')
    words_chets += 1
