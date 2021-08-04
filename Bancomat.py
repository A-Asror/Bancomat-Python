# class Online_Shopping:
#     def __init__(self):
#         pass
import random
from datetime import datetime
from pymongo import MongoClient

# cluster = MongoClient('mongodb+srv://account:NMsaa2003@cluster0.lcci4.mongodb.net/myFirstDatabase?retryWrites=true
# &w=majority') cluster = MongoClient('mongodb+srv://User:NMsaa2003@cluster0.og4jy.mongodb.net/testdata?retryWrites
# =true&w=majority')
cluster = MongoClient('mongodb+srv://User:NMsaa2003@cluster0.og4jy.mongodb.net/testdata?retryWrites=true&w=majority')
db = cluster['Bancomat']
History = db['History']
Users = db['Users']


class Banc:

    # name_register, frist_name_register, card_number_register, pin_register, balance_register, func
    def __init__(self):
        self.variable = True
        self.printed = {
            'History' :{
                'History_balance_view_history': {
                    'Прорерка_баланса': '- Пользователь\n {} {} \n- Проверка баланса в {}\n',
                },
                'History_deposit_money_errors' : {
                    'Внесение_денег': '\n- Пользователь {} {}\n-Баланс пополнен на {} сум - Дата {}',
                },
                'History_cash_withdrawal': {
                    'Снятие_денег': '- Пользователь {} {}\n - Сумма: {}\n- Снятие денег успешно прошло\n- Дата: {}',
                },
                'History_sending_money_history' : {
                    'Отправка_денег': '- Отпрака денег прошло успешно\n- Карта получателя {}\n- Сумма отправки {}\n- Пользователь {} {}\n - Дата: {}',
                },
                'History_Registration_history': {
                    'Регистрация': '- Пользователь {} {}\n Дата: {}'
                }
            },
            'Print' : {
                'Print_Registration_error': '- \n\nВы ввели не правильные параметры\n- Пожалуйста попробуйте еще раз',
                'Print_Сheck_in_consol': '1 - Регистрация \n 2 - Войти',
                'Print_Сheck_in_error': '- Введите: ',
                'Print_Counter_Falce': '\n\n- Вы использовали все попытки, пожалуйста попробуйте позже',
                'Print_balance': '\n\n- 1 просмотр баланса\n- 2 внесение дене\n- 3 снятие денег\n- 4 отправка денег\n- 0 Выйти',
                'Print_menu_input': '\n\n- Такой функции не существует',
                'Print_error': '\n\n- Вы ввели не правильные данные',
                'Print_error_Check_in': '\n\n- Вы ввели не существующие данные',
                'Print_Registration_chek': '\n\n- Вы истратили все попытки\n-Пожалуйста вернитесь позже',
                'Print_balance_view_error' : '\n\n- Ваш баланс к времени {}, составляет {} сум',
                'Print_deposit_money_errors': '\n\n-Не достаточно средств',
                'Print_deposit_money_print': '\n\n- Пополнение баланса произошло успешно',
                'Print_cash_withdrawal_consol': '\n\n- Введите сумму: ',
                'Print_cash_withdrawal_true': '\n\n- Снятие денег успешно прошло\n- Дата: {}',
                'Print_sending_money_consol': '\n\n- Отпрака денег прошло успешно\n- Дата: {}',

            },
        }

        self.Check_in()

    # ФУНКЦИЯ ПРИНТ
    def Print(self, consol, consol_1):
        x = self.printed[consol][consol_1]
        if consol_1 == 'Print_balance_view_error' or consol_1 == 'Print_cash_withdrawal_true' or consol_1 == 'Print_sending_money_consol':
            f = '' + x
            s = f.format(datetime.now(), self.balance_register)
            print(s)
        else:
            print(x)


    # История
    def History(self, location, key, key1):
        if key1 == 'Прорерка_баланса':
            userr = self.printed[location][key][key1]
            z = userr.format(self.name_register, self.frist_name_register, datetime.now())
            serrr = {key1 : z}
            History.insert_one(serrr)
        elif key1 == 'Внесение_денег':
            userr = self.printed[location][key][key1]
            z = userr.format(self.name_register, self.frist_name_register,self.sum ,datetime.now() )
            serrr = {key1: z}
            History.insert_one(serrr)
        elif key1 == 'Снятие_денег':
            userr = self.printed[location][key][key1]
            z = userr.format(self.name_register, self.frist_name_register, self.balance_cash ,datetime.now())
            serrr = {key1: z}
            History.insert_one(serrr)
        elif key1 == 'Отправка_денег':
            userr = self.printed[location][key][key1]
            z = userr.format(self.sending, self.sending_sum, self.name_register, self.frist_name_register, datetime.now())
            serrr = {key1: z}
            History.insert_one(serrr)
        elif key1 == 'Регистрация':
            userr = self.printed[location][key][key1]
            z = userr.format(self.name_register, self.frist_name_register, datetime.now())
            serrr = {key1: z}
            History.insert_one(serrr)

    # Добавление к пользователям
    def user_database(self):
        users = {
            'name': self.name_register,
            'frist_name': self.frist_name_register,
            'User_name' : self.username,
            'card': self.card_number_register,
            'pincod': self.pin_register,
            'balance': self.balance_register
        }
        Users.insert_one(users)

    # Поиск пользователя и Вход
    def entrance(self):
        i = 1
        while i <= 3:
            i += 1
            try:
                username = input('- Введите username: ')
                pincod = int(input('- Введите пароль: '))
                myquery = {'User_name' : username,'pincod': pincod}
                mydoc = Users.find(myquery)
                for x in mydoc:
                    self.name_register = x['name']
                    self.frist_name_register = x['frist_name']
                    self.balance_register = x['balance']
                    i = 4
                    self.Menu_print()
            except:
                i += 1
            if i == 4:
                i = 3
                self.Check_in()

    # Компилятор для Входа
    def entrance_compiler(self):
        if self.counter <= 3:
            self.entrance()
        else:
            self.Print(consol='Print', consol_1='Print_Counter_Falce')
            self.counter = 1
#            self.Menu_print()

    # РЕГИСТРАЙИЯ ЛИБО ВХОД
    def Check_in(self):
        try:
            self.Print(consol= 'Print',consol_1= 'Print_Сheck_in_consol')
            self.registration = int(input('- Введите: '))
            self.Check_registration()
        except:
            self.Print(consol='errors', consol_1='error')
            self.Check_in()

    # ПРОВЕРКА ФУНКЦИИ РЕГИСТРАЙИЯ ЛИБО ВХОД
    def Check_registration(self):
        if self.registration == 1:
            return self.Registration()
        elif self.registration == 2:
            return self.entrance()
        elif self.registration > 2:
            self.Print(consol='error', consol_1='error_Check_in')

    # КОМПИЛЯТОР
    def Compiler(self):
        if self.counter <= 3:
            self.counter += 1
        else:
            self.counter = 1


    # Под КОМПИЛЯТОР
    def compiler_Registration(self, location, key):
        if self.counter <= 3:
            self.Check_registration()
        else:
            self.Print(consol=location, consol_1=key)
            self.Check_in()
            self.counter = 1

    # КОМПИЛЯТОР ВНЕСЕНИЕ ДЕНЕГ
    def Compiler_func(self, printed, printed_1):
        if self.counter <= 3:
            self.Menu_input()
        else:
            self.Print(consol='Print', consol_1='Print_Counter_Falce')
            self.counter = 1
            self.Menu_print()

# КОМПИЛЯТОР БАНКОМАТА
    def Menu_print_comiler(self):
        if self.counter <= 3:
            self.Menu_print()
        else:
            self.Print(consol='Print', consol_1='Print_Counter_Falce')
            self.counter = 1
            self.Check_in()

    # РЕГИСТРАЦИЯ
    def Registration(self):
        try:
            self.name_register = str(input('\n\n- Имя: '))
            self.frist_name_register = str(input('- Фамилия: '))
            self.username = input('- Введите Username: ')
            self.card_number_register = random.randrange(150000000, 99999999999999)
            self.pin_register = int(input('- Пароль: '))
            self.balance_register = int(input('- Введите баланс: '))
            self.counter = 1
            self.user_database()
            self.History(location='History', key='History_Registration_history', key1='Регистрация')
            self.Menu_print()
        except:
            self.Print(consol='Print', consol_1='Print_error')
            self.Compiler()
            self.compiler_Registration(location='Print', key='Print_Registration_chek')


    # МЕНЮ БАНКОМАТА
    def Menu_print(self):
        try:
            self.Print(consol='Print', consol_1='Print_balance')
            self.menu = int(input('- Введите: '))
            self.counter = 1
            self.Menu_input()
        except:
            self.Print(consol='Menu', consol_1='menu_input')
            self.Compiler()
            self.Menu_print_comiler()

    # ПРОВЕРКА МЕНЮ БАНКОМАТА
    def Menu_input(self):
        if self.menu == 1:
            return self.balance_view()
        elif self.menu == 2:
            return self.deposit_money()
        elif self.menu == 3:
            return self.cash_withdrawal()
        elif self.menu == 4:
            self.sending_money()
        elif self.menu == 0:
            self.Check_in()
        else:
            self.Print(consol='Print', consol_1='Print_menu_input')

    # ПРОВЕРКА БАЛАНСА
    def balance_view(self):
        self.Print(consol='Print', consol_1='Print_balance_view_error')
        self.History(location='History',key='History_balance_view_history', key1='Прорерка_баланса')
        self.Menu_print()

    # ВНЕСЕНИЕ ДЕНЕГ
    def deposit_money(self):
        try:
            self.sum = int(input('- Введите сумму депозита: '))
            self.deposit_money_errors()
        except:
            self.Print(consol='Print', consol_1='Print_menu_input')
            self.Compiler()
            self.Compiler_func(printed='Print', printed_1='Print_Counter_Falce')

    # ПОПОЛНЕНИЕ СЧЕТА
    def deposit_money_errors(self):
        self.balance_register += self.sum - 0.5
        self.History(location='History', key='History_deposit_money_errors', key1='Внесение_денег')
        self.Print(consol='Print', consol_1='Print_deposit_money_print')
        self.counter = 1
        self.Menu_print()

    # СНЯТМЕ ДЕНЕГ
    def cash_withdrawal(self):
        try:
            self.Print(consol='Print',consol_1='Print_cash_withdrawal_consol')
            self.balance_cash = int(input(': '))
            self.cash_withdrawal_error()
        except:
            self.Print(consol='Print', consol_1='Print_error')
            self.Compiler()
            self.Compiler_func(printed='Print', printed_1='Print_Counter_Falce')

# ПРОВЕРКА ФУНКЦИИ СНЯТИЕ ДЕНЕГ
    def cash_withdrawal_error(self):
        if self.balance_cash < self.balance_register* 1.01:
            self.balance_register -= self.balance_cash * 1.01
            print(self.balance_register, self.balance_cash)
            self.Print(consol='Print', consol_1='Print_cash_withdrawal_true')
            self.History(location='History', key='History_cash_withdrawal', key1='Снятие_денег')
            self.counter = 1
            self.Menu_print()
        else:
            self.Print(consol='Print',consol_1='Print_deposit_money_errors')
            self.Compiler()
            self.Compiler_func(printed='Print', printed_1='Print_Counter_Falce')

    # ОТПРАВКА ДЕНЕГ
    def sending_money(self):
        try:
            self.sending = int(input('- Введите серию карты: '))
            self.sending_sum = int(input('- Введите сумму: '))
            self.sending_money_error()
        except:
            self.Print(consol='Print', consol_1='Print_error')
            self.Compiler()
            self.Compiler_func(printed='Print', printed_1='Print_Counter_Falce')

    # ПРОВЕРКА ФУНКЦИИ ОТПРАВКА ДЕНЕГ
    def sending_money_error(self):
        if self.balance_register > self.sending_sum:
            self.balance_register -= self.sending_sum * 1.01
            self.Print(consol='Print',consol_1='Print_sending_money_consol')
            self.History(location='History', key='History_sending_money_history', key1='Отправка_денег')
            self.counter = 1
            self.Menu_print()
        else:
            self.Print(consol='Print', consol_1='Print_deposit_money_errors')
            self.Compiler_func(printed='Print', printed_1='Print_Counter_Falce')


ak = Banc()