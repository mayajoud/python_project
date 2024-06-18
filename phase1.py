import random
import string
# ماموریت اول: پیدا کردن اولین سرنخ
def clue_decrypt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        found_keywords = []
        for word in text.split():
            if is_python_keyword(word):
                found_keywords.append(word)
    return found_keywords
def is_python_keyword(word):
    python_keywords = ["and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except",
                       "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not",
                       "or", "pass", "raise", "return", "try", "while", "with", "yield"]
    return word in python_keywords
def puzzles_solve (file_path):
    # باز کردن فایل معماهای منطقی
    with open(file_path, 'r') as file:
        puzzles = file.readlines ()
    results = []
    for puzzle in puzzles:
        # حذف فاصله‌های اضافی و کاراکترهای خالی
        puzzle = puzzle.strip ()
        # جدا کردن عبارات بولی
        expressions = puzzle.split (',')
        # حل هر عبارت بولی و محاسبه نتیجه
        expression_values = []
        for exp in expressions:
            exp_result = eval (exp)
            expression_values.append (exp_result)
        results.append (expression_values)
    return results
# فرض کنید فایل txt.puzzles موجود است و مسیر آن به عنوان ورودی به تابع داده می‌شود
file_path = "puzzles"
puzzle_results = puzzles_solve (file_path)
print("Puzzle results:", puzzle_results)
def numbers_magic_calculate(start, end):
    # پیاده‌سازی تابع تولید اعداد جادویی در بازه معین
    magic_numbers = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            magic_numbers.append(i * 2)
        else:
            magic_numbers.append(i + 1)
    return magic_numbers

def numbers_exam():
    # پیاده‌سازی تابع نمایش اعداد دودویی به صورت رندوم و دریافت ورودی از کاربر
    binary_numbers = [''.join(random.choice('01') for _ in range(4)) for _ in range(10)]
    for binary_number in binary_numbers:
        print(binary_number)
        user_input = input("Enter the decimal equivalent: ")
        # ارزیابی پاسخ کاربر
        # محدودیت زمانی بررسی نمی‌شود، اما می‌توانید از time ماژول استفاده کنید
        # برای محدود کردن زمان ورودی کاربر
    return

def pass_check(users):
    # پیاده‌سازی تابع بررسی رمز عبورها بر اساس شرایط مورد نظر
    valid_passwords = []
    for username, password in users:
        if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char in string.punctuation for char in password):
            valid_passwords.append((username, password))
    return valid_passwords

# مثالی از فراخوانی توابع:
# مثال برای numbers_magic_calculate:
start = 1
end = 10
magic_numbers = numbers_magic_calculate(start, end)
print("Magic numbers:", magic_numbers)

# مثال برای numbers_exam:
numbers_exam()

# مثال برای pass_check:
users = [("user1", "Passw0rd!"), ("user2", "password"), ("user3", "Password123")]
valid_passwords = pass_check(users)
print("Valid passwords:", valid_passwords)
