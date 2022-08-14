from pyfiglet import Figlet
from colorama import Fore, init
init()

f = Figlet(font='doom')
print(Fore.RED + f.renderText('python apps'))

print(f'{Fore.RED}1. {Fore.CYAN}Weather{"": <{10}}', end="\t")
print(f'{Fore.RED}2. {Fore.CYAN}Calender{"": <{10}}', end="\t")
print(f'{Fore.RED}3. {Fore.CYAN}Coins', end="\n")

print(f'{Fore.RED}4. {Fore.CYAN}Screenshot{"": <{10}}', end="\t")
print(f'{Fore.RED}5. {Fore.CYAN}Screen recorder{"": <{6}}', end="")
print(f'{Fore.RED}6. {Fore.CYAN}Whatsapp message', end="\n")

print(f'{Fore.RED}7. {Fore.CYAN}Email{"": <{10}}', end="\t")
print(f'{Fore.RED}8. {Fore.CYAN}Calculator{"": <{10}}', end="\t")
print(f'{Fore.RED}9. {Fore.CYAN}Ip address', end="\n")

print(f'{Fore.RED}10. {Fore.CYAN}Alarm{"": <{10}}', end="\t")
print(f'{Fore.RED}11. {Fore.CYAN}Clock{"": <{10}}', end="\t")
print(f'{Fore.RED}12. {Fore.CYAN}Corona statistics', end="\n")

print(f'{Fore.RED}13. {Fore.CYAN}Base converter{"": <{1}}', end="\t")
print(f'{Fore.RED}14. {Fore.CYAN}Text to morse code{"": <{0}}', end="\t")
print(f'{Fore.RED}15. {Fore.CYAN}Convert images to pdf', end="\n")

print(f'{Fore.RED}16. {Fore.CYAN}Random number{"": <{2}}', end="\t")
print(f'{Fore.RED}17. {Fore.CYAN}Text to speech{"": <{2}}', end="\t")
print(f'{Fore.RED}18. {Fore.CYAN}Internet connection', end="\n")

print(f'{Fore.RED}19. {Fore.CYAN}Hangman{"": <{10}}', end="\t")
print(f'{Fore.RED}20. {Fore.CYAN}Notes{"": <{10}}', end="\t")
print(f'{Fore.RED}21. {Fore.CYAN}Convert to zip file', end="\n")

print(f'{Fore.RED}22. {Fore.CYAN}Calculate age{"": <{1}}', end="\t")
print(f'{Fore.RED}23. {Fore.CYAN}Password generator{"": <{0}}', end="\t")
print(f'{Fore.RED}24. {Fore.CYAN}Tic Tac Toe', end="\n")

print(f'{Fore.RED}25. {Fore.CYAN}BMI{"": <{10}}', end="\t")
print(f'{Fore.RED}26. {Fore.CYAN}Image to ascii{"": <{0}}', end="\t")
print(f'{Fore.RED}24. {Fore.CYAN}Read text', end="\n")
print()