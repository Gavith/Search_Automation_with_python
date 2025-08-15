import webbrowser

# search function 
def search(what):
    what = what.replace(" ", "+")
    webbrowser.open(f"www.youtube.com/results?search_query={what}")
    print(f"Searching...  {what.replace("+", " ")}")

# get user input
what = input("What do you want to search? : ").strip()
# call the search function
search(what)
