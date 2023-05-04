from functions import functions
from difflib import get_close_matches


def checkInfo(function, functions = functions):
    function = function.lower()
    matches = set(get_close_matches(function, functions, n=1))
    available = False
    if function in matches:
        available = True
        matches = function

    return {'available': available, 'matches': matches}

if __name__ == '__main__':
    print(checkInfo('print'))
    print(checkInfo('intaggdjshgfjgsd'))