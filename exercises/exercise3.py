# 2-3 Personal Message
print('2-3 Personal Message')
name = 'Roger'
message = f'Hello {name}, how are you?\n'
print(message)

# 2-4 Name Cases
print('2-4 Name Cases')
name_other = 'O\'Dell'
print(name_other.lower())
print(name_other.upper())
print(f'{name_other.title()}\n')

# 2-5 Famous Quotes
print('2-5 Famous Quotes')
quote = '''\"Elves are wonderful. They provoke wonder.
 Elves are marvellous. They cause marvels.
 Elves are fantastic. They create fantasies.
 Elves are glamorous. They project glamour.
 Elves are enchanting. They weave enchantment.
 Elves are terrific. They beget terror.
 The thing about words is that meanings can twist just like a snake, and if 
 you want to find snakes look for them behind words that have changed their meaning.
 No one ever said elves are nice.
 Elves are bad.\"'''
print(f'{quote}\n -Terry Pratchet\n')


# 2-6 Famous Quotes 2
print('2-6 Famous Quotes 2')
quote = '''\"Elves are wonderful. They provoke wonder.
 Elves are marvellous. They cause marvels.
 Elves are fantastic. They create fantasies.
 Elves are glamorous. They project glamour.
 Elves are enchanting. They weave enchantment.
 Elves are terrific. They beget terror.
 The thing about words is that meanings can twist just like a snake, and if 
 you want to find snakes look for them behind words that have changed their meaning.
 No one ever said elves are nice.
 Elves are bad.\"'''
famous_person = 'Terry Pratchett'
message = f'{quote}\n -{famous_person}\n'
print(message)

# 2-7 String Names
print('2-7 Stripping Names')
name_strip = '  \tNewberry\n '
print(f'Original:{name_strip}')
print(f'lstrip:{name_strip.lstrip()}')
print(f'rstrip:{name_strip.rstrip()}')
print(f'strip:{name_strip.strip()}')
