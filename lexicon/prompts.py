import random

adjectives = ['креативный', 'смешной', 'развернутый', 'нереалистичный', 'тупой', 'мудрый', 'необычный', 'дурацкий']
PROMPTS={
    'get_advice': f"Дай {random.choice(adjectives)} совет чем заняться сегодня",
    'get_advice_2':'Представь, что твои друзья работают на тяжёлой работе, а ты счастливый безработный человек, который круто проводит время каждый день, каким бы классным делом ты занимался, пока твои друзья на работе? Ответь на русском в одном предложении.',
    'predictions': ['Напиши мне короткую частушку с предсказанием',
                    'Напиши шутку Луи Си Кея про будущее ',
                    'Напиши мне хокку с предсказанием на сегодня',
                    'Напиши мне предсказание на сегодня в стиле татарского анектода',
                    ]

}

