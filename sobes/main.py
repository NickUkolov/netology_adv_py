from defs import bracket_checker


if __name__ == '__main__':
    bal = '[([({}())])]'
    unbal = '{}[][[(())]]}'

    print(bracket_checker(bal))
    print(bracket_checker(unbal))
