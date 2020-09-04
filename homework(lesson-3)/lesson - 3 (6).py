def lower_func(text):
    text_low = text.lower()
    text_title = text_low.title()
    return text_title
user_answer = input('Введите любые слова через пробел: ')
right_answer = lower_func(user_answer)
print(right_answer)
