from colorama import init, Fore

init()

colors = {
    "GREEN":Fore.GREEN,
    "BLUE":Fore.BLUE,
    "CYAN":Fore.CYAN,
    "RED":Fore.RED,
    "MAGENTA":Fore.MAGENTA,
    "YELLOW":Fore.YELLOW,
    "WHITE":Fore.WHITE
}

#* [+]
success_output =  ""
success_output += colors["WHITE"] + "[" 
success_output +=  colors["GREEN"] + "+"
success_output += colors["WHITE"] + "]"

output_style = {
    "success":success_output
}