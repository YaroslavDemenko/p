import telebot
import random

bot = telebot.TeleBot('6246805629:AAEOCEZW5mIFSjS9EJpK1FuP51n4Wc2YO9U')
def reset_test():
    global tasks, user_scores, user_answers, tasks2

tasks = [
    {
        'type': 'геометрия',
        'question': 'Высота равностороннего треугольника равна 59√3 . Найдите его периметр.',
        'choices': {'a': '625', 'b': '970', 'c': '142', 'd': '354'},
        'correct': 'd',
    },
    {
        'type': 'алгебра',
        'question': 'Решите уравнение: 2x - 3 = 9',
        'choices': {'a': 'x=3', 'b': 'x=-3', 'c': 'x=6', 'd': 'x=-6'},
        'correct': 'c',
    },
    {
        'type': 'тригонометрия',
        'question': 'В треугольнике ABC угол C прямой, BC=3 , cosB = 0,6. Найдите AB.',
        'choices': {'a': '5', 'b': '2.5', 'c': '7.5', 'd': '10'},
        'correct': 'a',
    },
    {
        'type': 'алгебра',
        'question': 'При каких значениях x значение выражения 9x + 7 меньше значения выражения 8x − 3?',
        'choices': {'a': 'x > 4', 'b': 'x < 4', 'c': 'x > − 10', 'd': 'x < − 10'},
        'correct': 'd',
    },
    {
        'type': 'геометрия',
        'question': 'В прямоугольнике одна сторона равна 10, другая сторона равна 12. Найдите площадь прямоугольника.',
        'choices': {'a': '140', 'b': '120', 'c': '100', 'd': '80'},
        'correct': 'b',
    },
    {
        'type': 'тригонометрия',
        'question': 'Боковая сторона равнобедренного треугольника равна 4. Угол при вершине, противолежащий основанию, равен 120°. Найдите диаметр окружности, описанной около этого треугольника.',
        'choices': {'a': '8', 'b': '10', 'c': '3', 'd': '14'},
        'correct': 'a',
    },
    {
        'type': 'алгебра',
        'question': 'В фирме такси в данный момент свободно 20 машин: 9 черных, 4 желтых и 7 зеленых. По вызову выехала одна из машин, случайно оказавшаяся ближе всего к заказчику. Найдите вероятность того, что к нему приедет желтое такси.?',
        'choices': {'a': '0,2', 'b': '0,4', 'c': '0,8', 'd': '0,3'},
        'correct': 'a',
    },
    {
        'type': 'тригонометрия',
        'question': 'В треугольнике ABC угол C равен 90 °, BC = 6, sin A = 0,3. Найдите AB.',
        'choices': {'a': '80', 'b': '300', 'c': '20', 'd': '50'},
        'correct': 'c',
    },
    {
        'type': 'геометрия',
        'question': 'В прямоугольном треугольнике ABC с прямым углом C известны катеты: AC=6, BC=8. Найдите медиану CK этого треугольника.',
        'choices': {'a': '9', 'b': '8', 'c': '3', 'd': '5'},
        'correct': 'd',
    },
    {
        'type': 'алгебра',
        'question': 'В амфитеатре 13 рядов. В первом ряду 17 мест, а в каждом следующем на 2 места больше, чем в предыдущем. Сколько всего мест в амфитеатре?',
        'choices': {'a': '225', 'b': '377', 'c': '688', 'd': '465'},
        'correct': 'b',
    },
    {
        'type': 'тригонометрия',
        'question': 'В треугольнике ABC угол C прямой, AC=8 , cos A=0,4. Найдите AB.',
        'choices': {'a': '30', 'b': '20', 'c': '40', 'd': '3,2'},
        'correct': 'b',
    },
    {
        'type': 'геометрия',
        'question': 'На прямой AB взята точка M. Луч MD — биссектриса угла CMB. Известно, что ∠DMC=60°. Найдите угол CMA. Ответ дайте в градусах.',
        'choices': {'a': '80', 'b': '120', 'c': '60', 'd': '30'},
        'correct': 'c',
    },
]
tasks2 = [
    {
        'type': 'геометрия',
        'question': 'Высота равностороннего треугольника равна 59√3 . Найдите его периметр.',
        'choices': {'a': '625', 'b': '970', 'c': '142', 'd': '354'},
        'correct': 'd',
    },
    {
        'type': 'алгебра',
        'question': 'Решите уравнение: 2x - 3 = 9',
        'choices': {'a': 'x=3', 'b': 'x=-3', 'c': 'x=6', 'd': 'x=-6'},
        'correct': 'c',
    },
    {
        'type': 'тригонометрия',
        'question': 'В треугольнике ABC угол C прямой, BC=3 , cosB = 0,6. Найдите AB.',
        'choices': {'a': '5', 'b': '2.5', 'c': '7.5', 'd': '10'},
        'correct': 'a',
    },
    {
        'type': 'алгебра',
        'question': 'При каких значениях x значение выражения 9x + 7 меньше значения выражения 8x − 3?',
        'choices': {'a': 'x > 4', 'b': 'x < 4', 'c': 'x > − 10', 'd': 'x < − 10'},
        'correct': 'd',
    },
    {
        'type': 'геометрия',
        'question': 'В прямоугольнике одна сторона равна 10, другая сторона равна 12. Найдите площадь прямоугольника.',
        'choices': {'a': '140', 'b': '120', 'c': '100', 'd': '80'},
        'correct': 'b',
    },
    {
        'type': 'тригонометрия',
        'question': 'Боковая сторона равнобедренного треугольника равна 4. Угол при вершине, противолежащий основанию, равен 120°. Найдите диаметр окружности, описанной около этого треугольника.',
        'choices': {'a': '8', 'b': '10', 'c': '3', 'd': '14'},
        'correct': 'a',
    },
    {
        'type': 'алгебра',
        'question': 'В фирме такси в данный момент свободно 20 машин: 9 черных, 4 желтых и 7 зеленых. По вызову выехала одна из машин, случайно оказавшаяся ближе всего к заказчику. Найдите вероятность того, что к нему приедет желтое такси.?',
        'choices': {'a': '0,2', 'b': '0,4', 'c': '0,8', 'd': '0,3'},
        'correct': 'a',
    },
    {
        'type': 'тригонометрия',
        'question': 'В треугольнике ABC угол C равен 90 °, BC = 6, sin A = 0,3. Найдите AB.',
        'choices': {'a': '80', 'b': '300', 'c': '20', 'd': '50'},
        'correct': 'c',
    },
    {
        'type': 'геометрия',
        'question': 'В прямоугольном треугольнике ABC с прямым углом C известны катеты: AC=6, BC=8. Найдите медиану CK этого треугольника.',
        'choices': {'a': '9', 'b': '8', 'c': '3', 'd': '5'},
        'correct': 'd',
    },
    {
        'type': 'алгебра',
        'question': 'В амфитеатре 13 рядов. В первом ряду 17 мест, а в каждом следующем на 2 места больше, чем в предыдущем. Сколько всего мест в амфитеатре?',
        'choices': {'a': '225', 'b': '377', 'c': '688', 'd': '465'},
        'correct': 'b',
    },
    {
        'type': 'тригонометрия',
        'question': 'В треугольнике ABC угол C прямой, AC=8 , cos A=0,4. Найдите AB.',
        'choices': {'a': '30', 'b': '20', 'c': '40', 'd': '3,2'},
        'correct': 'b',
    },
    {
        'type': 'геометрия',
        'question': 'На прямой AB взята точка M. Луч MD — биссектриса угла CMB. Известно, что ∠DMC=60°. Найдите угол CMA. Ответ дайте в градусах.',
        'choices': {'a': '80', 'b': '120', 'c': '60', 'd': '30'},
        'correct': 'c',
    },
]

user_scores = []
user_answers = {}

@bot.message_handler(commands=['task'])
def send_task(message):
    chat_id = message.chat.id
    if len(tasks) == 0 and len(tasks2) == 0:
        bot.send_message(chat_id, 'Задания закончились! Напиши /results, чтобы узнать свой результат!')
        return

    if len(tasks) > 0:
        task_list = tasks
    else:
        task_list = tasks2

    random_task = random.choice(task_list)

    question = random_task['question']
    choices = random_task['choices']

    choices_str = '\n'.join([f'{key}. {value}' for key, value in choices.items()])

    bot.reply_to(message, f'{random_task["type"]}:\n{question}\nВарианты ответов:\n{choices_str}')

    task_list.remove(random_task)

    user_answers[chat_id] = {
        'task': random_task,
        'answer': '',
    }
    
@bot.message_handler(commands=['results'])
def show_results(message):
    chat_id = message.chat.id
    score = sum(user_scores)
    total = len(user_scores)
    bot.send_message(chat_id, f'У тебя {score} правильных ответов из {total} заданий!')
    user_scores.clear()
    user_answers.clear()
    if len(tasks) > 0:
        reset_test()
        bot.send_message(chat_id, 'Хотите пройти этот тест еще раз? Напишите /task')
    else:
        tasks.clear()
        bot.send_message(chat_id, 'Второй тест закончился! Напишите /results, чтобы узнать свой финальный результат')

@bot.message_handler(func=lambda message: True)
def check_answer(message):
    chat_id = message.chat.id
    if chat_id not in user_answers:
        bot.send_message(chat_id, 'Напиши /task, чтобы получить новое задание!')
        return

    user_task = user_answers[chat_id]['task']
    task_correct_answer = user_task['correct']
    user_choice = message.text.lower()

    if user_choice.startswith('/'):
        return

    if user_choice != 'a' and user_choice != 'b' and user_choice != 'c' and user_choice != 'd':
        bot.send_message(chat_id, 'Некорректный ввод! Введи букву варианта ответа: a, b, c или d')
        return
    
    user_answers[chat_id]['answer'] = user_choice

    if user_choice == task_correct_answer:
        bot.send_message(chat_id, 'Правильно!')
        user_scores.append(1)
    else:
        bot.send_message(chat_id, f'Неправильно! Правильный ответ: {user_task["choices"][task_correct_answer]}')
        user_scores.append(0)

    send_task(message)


bot.polling()