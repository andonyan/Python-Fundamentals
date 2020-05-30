def loading_bar(n):
    if n != 100:
        print(f'{n}% ' + '[' + '%' * (n // 10) + '.' * (10 - (n // 10)) + ']\nStill loading...')

    else:
        print('100% Complete!\n[%%%%%%%%%%] ')


a = int(input())
loading_bar(a)
