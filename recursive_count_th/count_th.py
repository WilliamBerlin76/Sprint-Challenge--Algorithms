'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) <= 1:
        return 0
    th_count = []
    def inner_recurse(word):
        if len(word) == 1:
            return
        if word[0] + word[1] == 'th':
            th_count.append('th')
            if len(word) > 2:
                inner_recurse(word[2:])
            else:
                inner_recurse(word[1:])
        else:
            inner_recurse(word[1:])
  
    inner_recurse(word)
    return len(th_count)