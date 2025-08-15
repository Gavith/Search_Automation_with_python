import webbrowser
import argparse

# CLI argument setup
parser = argparse.ArgumentParser(description="Search on Youtube using CLI")
parser.add_argument("-u", "--url", help="Search query text", required=True)
parser.add_argument("--youtube", action="store_true", help="Search on youtube")

args = parser.parse_args()

# Prepare query varible

query = args.url.strip()

query = query.lower().replace(" ", "+")

    # select platforme
if args.youtube:
        search_url = f"www.youtube.com/results?search_query={query}"
else:
        search_url = f"https://www.google.com/search?q={query}"

webbrowser.open(search_url)
print(f"Searching...  {query.replace("+", " ")}")

