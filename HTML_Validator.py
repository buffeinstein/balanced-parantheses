#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    tags = _extract_tags(html)
    stack = []
    if len (tags) == 0: 
        return True 
    if len (tags) == 1: 
        return False
    else: 
        for i in range(len(tags)): 
            if tags[i][1] != '/': #not a closing tag
                stack.append(tags[i]) #add it 
            else:  #a closing tag
                if len(stack) == 0:
                     return False #started with a closing tag - cannot be balanced
                if tags[i][2:] == stack[-1][1:]:
                     stack.pop()

    if len (stack) == 0: 
        return True 
    
       
       #for tag in tagslst: 
        

   # stack = []
   # for symbol in text:
   #     if symbol in '([{' :
   #         stack.append(symbol)
   #     else:
   #         if len(stack) == 0:
   #             return False
   #         if (stack[-1] == '(' and symbol == ')') or \
   #            (stack[-1] == '[' and symbol == ']') or \
   #            (stack[-1] == '{' and symbol == '}'):
   #             stack.pop()
   #         else:
   #             return False
   # return len(stack) == 0

def _extract_tags(html):
    '''
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    import re
    return re.findall(r'<.*?>', html)
