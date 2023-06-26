python_words = {}
python_words['list'] = 'A collection of values that are not connected, but have an order.'
python_words['dictionary'] = 'A collection of key-value pairs.'
python_words['function'] = 'A named set of instructions that defines a set of actions in Python.'
print(python_words)

python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }
print('dictionary: ' + python_words['dictionary'])

python_words['dictionary'] = 'A collection of key-value pairs. Each key can be used to access its corresponding value.'
print('\ndictionary: ' + python_words['dictionary'])

python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }
del python_words['list']
print(python_words)

python_words = {'dict': 'A collection of values that are not connected, but have an order.'}
python_words['list'] = python_words['dict']
del python_words['dict']
print(python_words)
