from gui.functions import t_popup
from traceback import format_exception


def hook(type_, value, traceback):
    t_popup("Unhandled exception", "An unhandled exception has occurred, \n"
                                   "please check the console for more information.")
    print("[!] Error happened")
    print("Error type: ", type_.__name__)
    print("Error value: ", value)
    print("Error traceback: ", format_exception(type_, value, traceback)[2])
