print('Imported my module...')

test = 'Test String'

def find_index(to_seacrh, target):
    '''Find the index of the vlue in the search'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
    
