from datetime import datetime

odds = list(range(1,60,2)) # alterei o código do livro, ao invés de digitar a lista, gerei os números ímpares de 1 a 60 com essa função. Outra solução é verificar o resto da divisão por 2, que eu implementei no my_odd

right_this_minute = datetime.today().minute
                
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")