import os
from pyfiglet import Figlet
from colorama import Fore, init
from PyInquirer import style_from_dict, Token, prompt

os.system("cls")
init()


def start():
    f = Figlet(font='doom')
    print(Fore.GREEN + f.renderText('python apps'))

    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}1. {Fore.WHITE}Weather', f'{Fore.GREEN}2. {Fore.WHITE}Calender', f'{Fore.GREEN}3. {Fore.WHITE}Coins'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}4. {Fore.WHITE}Screenshot', f'{Fore.GREEN}5. {Fore.WHITE}Screen recorder', f'{Fore.GREEN}6. {Fore.WHITE}Whatsapp message'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}7. {Fore.WHITE}Email', f'{Fore.GREEN}8. {Fore.WHITE}Calculator', f'{Fore.GREEN}9. {Fore.WHITE}Ip address'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}10. {Fore.WHITE}Alarm', f'{Fore.GREEN}11. {Fore.WHITE}Clock', f'{Fore.GREEN}12. {Fore.WHITE}Corona statistics'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}13. {Fore.WHITE}Base converter', f'{Fore.GREEN}14. {Fore.WHITE}Text to morse code', f'{Fore.GREEN}15. {Fore.WHITE}Convert images to pdf'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}16. {Fore.WHITE}Random number', f'{Fore.GREEN}17. {Fore.WHITE}Text to speech', f'{Fore.GREEN}18. {Fore.WHITE}Internet connection'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}19. {Fore.WHITE}Hangman', f'{Fore.GREEN}20. {Fore.WHITE}Notes', f'{Fore.GREEN}21. {Fore.WHITE}Convert to zip file'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}22. {Fore.WHITE}Calculate age', f'{Fore.GREEN}23. {Fore.WHITE}Password generator', f'{Fore.GREEN}24. {Fore.WHITE}Tic Tac Toe'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}25. {Fore.WHITE}BMI', f'{Fore.GREEN}26. {Fore.WHITE}Image to ascii', f'{Fore.GREEN}27. {Fore.WHITE}Read text'))
    print()


def choose():
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#f70000 bold',
        Token.Answer: '#00f700 bold',
        Token.Question: '',
    })


    questions = [
        {
            'type': 'input',
            'message': 'Choose one program:',
            'name': 'programs',
        }
    ]

    return prompt(questions, style=style)["programs"]


start()
choose()