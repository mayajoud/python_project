def puzzles_solve (file_path):
    # باز کردن فایل معماهای منطقی
    with open (file_path, 'r') as file:
        file_puzzles = file.read ()
    return file_puzzles
for puzzle in puzzles:
    result= []
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
file_path = "txt.puzzles"
puzzle_results = puzzles_solve (file_path)
print ("Puzzle results:", puzzle_results)
