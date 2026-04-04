#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Funksiyanı təhlükəsiz şəkildə icra edir.
    
    Args:
        fct: İcra olunacaq funksiya (pointer).
        *args: Funksiyaya ötürüləcək dəyişən sayda arqumentlər.
        
    Returns:
        Funksiyanın nəticəsi, xəta baş verərsə None.
    """
    try:
        # fct funksiyasını args arqumentləri ilə çağırırıq
        result = fct(*args)
        return result
    except Exception as e:
        # Xətanı stderr-ə çap edirik
        print("Exception: {}".format(e), file=sys.stderr)
        return None
