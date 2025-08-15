import webbrowser
import argparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# CLI argument setup
parser = argparse.ArgumentParser(description=Fore.CYAN + "Search on Youtube using CLI" + Style.RESET_ALL)
parser.add_argument("url", help=Fore.YELLOW + "Search query text" + Style.RESET_ALL)
parser.add_argument("--youtube", action="store_true", help=Fore.MAGENTA + "Search on youtube" + Style.RESET_ALL)

args = parser.parse_args()

def url():
    match args.url.strip():
        case "youtube":
            search_url = "www.youtube.com"
        case "chatgpt":
            search_url = "www.chatgpt.com"
        case "deepseek":
            search_url = "https://chat.deepseek.com/"
        case "mail":
            search_url = "www.mail.google.com"
        case "github":
            search_url = "https://github.com/"
        case "w3school":
            search_url = "www.w3schools.com"
        case "aplus":
            search_url = "https://apluseducation.lk/"
        case "echem":
            search_url = "https://student.echem.lk/student/my_courses"
        case _: 
            # Prepare query variable
            query = args.url.strip()
            query = query.lower().replace(" ", "+")
            
            if args.youtube:
                search_url = f"https://www.youtube.com/results?search_query={query}"
            else:
                search_url = f"https://www.google.com/search?q={query}"
    
    webbrowser.open(search_url)
    
    print(Fore.CYAN +  f"Opening... {args.url.strip()}") 

# Open browser
url()

# Done message
print(Fore.LIGHTMAGENTA_EX + "[✔] Search opened in browser.")
