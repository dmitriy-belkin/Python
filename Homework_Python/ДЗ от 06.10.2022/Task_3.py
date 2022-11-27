# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

original_sentence = 'Неужели Абвер жив? Укрывшийся на помойках Зимбабве достоин забвения женщины!'
offer = original_sentence.lower().split(' ')
offer = [word for word in offer if not 'абв' in word]
print(' '.join(offer))