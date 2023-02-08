#!/bin/python3
import re


def validate_html(html):
    '''
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    tags = _extract_tags(html)
    stack = []
    if len(tags) <= 1 and len(html) > 0:
        return False
    else:
        for i in range(len(tags)):
            if tags[i][1] != '/':
                stack.append(tags[i])
            else:
                if len(stack) == 0:
                    return False
                if tags[i][2:] == stack[-1][1:]:
                    stack.pop()
    print("stack = ", stack)
    if len(stack) == 0:
        return True


def _extract_tags(html):
    '''
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = re.findall('<([^ >]+)', html)
    return list(map(lambda tag: "<" + tag + ">", tags))
