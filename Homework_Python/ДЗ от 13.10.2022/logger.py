from datetime import datetime as dt
import json
import user_interface

def info_data(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{time} совершено действие: {data} = ')
