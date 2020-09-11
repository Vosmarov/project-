with open('userfile.txt', 'w') as doc:
    user_answer = input('Введите любое утверждение: ')
    doc.write(user_answer)