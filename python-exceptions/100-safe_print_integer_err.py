#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Tam ədədi çap edir, xəta olduqda isə stderr-ə xəbərdarlıq göndərir.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        # Xətanı stderr-ə "Exception: message" formatında çap edirik
        print("Exception: {}".format(e), file=sys.stderr)
        return False
