#!/usr/bin/python3

def safe_print_division(a, b):
    """
    İki tam ədədi bölür və nəticəni 'finally' blokunda çap edir.
    """
    div_result = None
    try:
        div_result = a / b
    except ZeroDivisionError:
        # Sıfıra bölmə xətası baş verərsə, div_result None olaraq qalır
        pass
    finally:
        # Bu hissə xəta olub-olmamasından asılı olmayaraq HƏMİŞƏ işləyir
        print("Inside result: {}".format(div_result))
    
    return div_result
