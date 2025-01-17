def word_to_number(word):
    digit_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    # Split the word by 'c' and convert each part to a digit
    parts = word.split('c')
    number = ''
    for part in parts:
        if part in digit_map:
            number += digit_map[part]
        else:
            return None  # Invalid word
    return int(number)

def evaluate_expression(tokens):
    operations = {'add', 'sub', 'mul', 'rem', 'pow'}
    stack = []
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token in operations:
            if len(stack) < 2:
                return "expression is not complete or invalid"
            b = stack.pop()
            a = stack.pop()
            
            if token == 'add':
                stack.append(a + b)
            elif token == 'sub':
                stack.append(a - b)
            elif token == 'mul':
                stack.append(a * b)
            elif token == 'rem':
                stack.append(a % b)
            elif token == 'pow':
                stack.append(a ** b)
        else:
            num = word_to_number(token)
            if num is None:
                return "expression evaluation stopped invalid words present"
            stack.append(num)
        
        i += 1
    
    if len(stack) == 1:
        return stack[0]
    else:
        return "expression is not complete or invalid"

def main():
    expression = input().strip().split()
    
    result = evaluate_expression(expression)
    
    print(result)

main()