import re

text_to_search = '''

qwertyuioplkjhgfdsazxcvbnm
AQWSERFTGYHUJIKOLPMNBVCXZ

332-555-1234
344.555.4312
344*555*4312
800-555-4331
900-545-4012
900-545-4456
800-555-2323

Mr. Scahfer
Mr Smith
Ms Davis
Mrs. Rob
Mr. T

'''
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'and')

matches = pattern.match(sentence)  # findall() finditer()

print(matches)

