import gspread

gc = gspread.service_account(filename='key.json')
sh = gc.open_by_url(
    "https://docs.google.com/spreadsheets/d/16JbE2bMyrs61opmm7No8PrdDDbN3-4lvJbekqS1ix9o/edit?usp=sharing")
worksheet = sh.worksheet("Лист1")
data = sh.sheet1.get()
for i in data:
    print(*i)
print(data)
cell = "A" + str(data[0][0])
# worksheet.update('A1', cell + 'Свекла')
