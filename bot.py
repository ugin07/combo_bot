# Importowanie wymaganych modułów z biblioteki Telegram
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

    # Funkcja obsługująca komendę /start
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Największy wspólny dzielnik (NWD)", callback_data='gcd'),
        ],
        [
            InlineKeyboardButton("Flaga Holenderska (sortowanie)", callback_data='sort'),
        ],
        [
            InlineKeyboardButton("Flaga Francji (sortowanie)", callback_data='f_sort'),
        ],
        [
            InlineKeyboardButton("Sortowanie bąbelkowe", callback_data='b_sort'),
        ],
        [
            InlineKeyboardButton("Sortowanie przez wybieranie", callback_data='s_sort'),
        ],
        [
            InlineKeyboardButton("Wyszukiwanie binarne", callback_data='b_search'),
        ],
        [
            InlineKeyboardButton("Wydawanie reszty", callback_data='change'),
        ],
        [
            InlineKeyboardButton("Szyfr Cezara", callback_data='caesar'),
        ],
        [
            InlineKeyboardButton("Algorytm Luhna", callback_data='luhn'),
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Wybierz algorytm:', reply_markup=reply_markup)
    
    # Funkcja obsługująca naciśnięcie przycisku
def button(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    query.answer()

    if query.data == 'gcd':
        query.edit_message_text(text="Wprowadź komendę w formacie /gcd a b (np. /gcd 2 5) w celu obliczenia NWD.")
    elif query.data == 'sort':
        query.edit_message_text(text="Wprowadź komendę w formacie /sort ciąg (np. /sort RBRW) w celu posortowania.")
    elif query.data == 'f_sort':
        query.edit_message_text(text="Wprowadź komendę w formacie /f_sort ciąg (np. /f_sort RWBRG) w celu posortowania.")
    elif query.data == 'b_sort':
        query.edit_message_text(text="Wprowadź komendę w formacie /b_sort liczby (np. /b_sort 5 3 2 4) w celu posortowania przez sortowanie bąbelkowe.")
    elif query.data == 's_sort':
        query.edit_message_text(text="Wprowadź komendę w formacie /s_sort liczby (np. /s_sort 5 3 2 4) w celu posortowania przez sortowanie przez wybieranie.")
    elif query.data == 'change':
        query.edit_message_text(text="Wprowadź komendę w formacie /change kwota (np. /change 167) w celu wydania reszty.")
    elif query.data == 'caesar':
        query.edit_message_text(text="Wprowadź komendę w formacie /caesar przesunięcie tekst (np. /caesar 3 hello) w celu zaszyfrowania przy pomocy Szyfru Cezara.")
    elif query.data == 'luhn':
        query.edit_message_text(text="Wprowadź komendę w formacie /luhn numer (np. /luhn 49927398716) w celu sprawdzenia liczby przy pomocy algorytmu Luhna.")
    else:
        query.edit_message_text(text="Wprowadź komendę w formacie /b_search lista_liczb szukana_liczba (np. /b_search 1 2 3 4 5 3) w celu przeprowadzenia wyszukiwania binarnego.")

    # Funkcja obsługująca komendę /gcd
def gcd(update: Update, context: CallbackContext) -> None:
    numbers = context.args
    if len(numbers) != 2:
        update.message.reply_text('Proszę wprowadzić dokładnie dwie liczby.')
        return

    a, b = map(int, numbers)
    result = calculate_gcd(a, b)
    update.message.reply_text(f'NWD liczb {a} i {b} wynosi {result}.')

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def dutch_flag_sort(chars):
    low = 0
    mid = 0
    high = len(chars) - 1

    while mid <= high:
        if chars[mid] == 'R':
            chars[low], chars[mid] = chars[mid], chars[low]
            low += 1
            mid += 1
        elif chars[mid] == 'W':
            mid += 1
        else:
            chars[mid], chars[high] = chars[high], chars[mid]
            high -= 1

    return ''.join(chars)

# Funkcja obsługująca komendę /sort
def sort(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text('Proszę wprowadzić ciąg składający się ze znaków R, W i B.')
        return

    chars = list(context.args[0])
    sorted_chars = dutch_flag_sort(chars)
    update.message.reply_text(f'Posortowany ciąg: {sorted_chars}')


def french_flag_sort(chars):
    red, white, blue, green = 0, 0, len(chars) - 1, len(chars) - 1

    while white <= blue:
        if chars[white] == 'R':
            chars[red], chars[white] = chars[white], chars[red]
            red += 1
            white += 1
        elif chars[white] == 'W':
            white += 1
        elif chars[white] == 'B':
            chars[white], chars[blue] = chars[blue], chars[white]
            blue -= 1
        else:
            chars[blue], chars[green] = chars[green], chars[blue]
            blue -= 1
            green -= 1

    return ''.join(chars)
# Funkcja obsługująca komendę /f_sort
def f_sort(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text('Proszę wprowadzić ciąg składający się ze znaków R, W, B i G.')
        return

    chars = list(context.args[0])
    sorted_chars = french_flag_sort(chars)
    update.message.reply_text(f'Posortowany ciąg: {sorted_chars}')


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# Funkcja obsługująca komendę /b_sort
def b_sort(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text('Proszę wprowadzić listę liczb do posortowania.')
        return

    nums = list(map(int, context.args))
    sorted_nums = bubble_sort(nums)
    update.message.reply_text(f'Posortowana lista: {" ".join(map(str, sorted_nums))}')


def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
                
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

# Funkcja obsługująca komendę /s_sort
def s_sort(update: Update, context: CallbackContext) -> None:

    if not context.args:
        update.message.reply_text('Proszę wprowadzić listę liczb do posortowania.')
        return

    nums = list(map(int, context.args))
    sorted_nums = selection_sort(nums)
    update.message.reply_text(f'Posortowana lista: {" ".join(map(str, sorted_nums))}')


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Funkcja obsługująca komendę /b_search
def b_search(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 2:
        update.message.reply_text('Proszę wprowadzić listę liczb, a następnie liczbę, której szukasz.')
        return

    nums = list(map(int, context.args[:-1]))
    target = int(context.args[-1])
    position = binary_search(nums, target)
    if position == -1:
        update.message.reply_text(f'Liczba {target} nie została znaleziona na liście.')
    else:
        update.message.reply_text(f'Liczba {target} została znaleziona na pozycji {position}.')


def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result

    # Funkcja obsługująca komendę /caesar
def caesar(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 2:
        update.message.reply_text('Proszę wprowadzić przesunięcie i tekst do zaszyfrowania metodą Szyfru Cezara.')
        return

    shift = int(context.args[0])
    text = " ".join(context.args[1:])
    cipher_text = caesar_cipher(text, shift)
    update.message.reply_text(f'Zaszyfrowany tekst: {cipher_text}.')


    # Funkcja obsługująca komendę /change
def change(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text('Proszę wprowadzić kwotę do wydania jako reszty.')
        return

    amount = int(context.args[0])
    change = calculate_change(amount)
    update.message.reply_text(f'Resza: {" ".join(map(str, change))}.')

def calculate_change(amount):
    coins = [100, 50, 20, 10, 5, 2, 1]
    change = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)

    return change


def luhn_checksum(id_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(id_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(id_number):
    return luhn_checksum(id_number) == 0

# Funkcja obsługująca komendę /luhn
def luhn(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text('Proszę wprowadzić liczbę do sprawdzenia metodą Luhna.')
        return

    id_number = int(context.args[0])
    if is_luhn_valid(id_number):
        update.message.reply_text(f'Liczba {id_number} jest poprawna według metody Luhna.')
    else:
        update.message.reply_text(f'Liczba {id_number} jest niepoprawna według metody Luhna.')


def main() -> None:
    updater = Updater("token")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler("gcd", gcd))
    dispatcher.add_handler(CommandHandler("sort", sort))
    dispatcher.add_handler(CommandHandler("f_sort", f_sort))
    dispatcher.add_handler(CommandHandler("b_sort", b_sort))
    dispatcher.add_handler(CommandHandler("s_sort", s_sort))
    dispatcher.add_handler(CommandHandler("b_search", b_search))
    dispatcher.add_handler(CommandHandler("change", change))
    dispatcher.add_handler(CommandHandler("caesar", caesar))
    dispatcher.add_handler(CommandHandler("luhn", luhn))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
