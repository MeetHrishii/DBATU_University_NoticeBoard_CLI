import requests
from bs4 import BeautifulSoup
from rich import style
from rich.console import Console


headers = dict()
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36."
# URL = "https://dbatu.ac.in/category/notices/"
URL = "https://dbatu.ac.in/category/notices/"


console = Console()
console.print("[link=https://dbatu.ac.in/category/notices/]DBATU UNIVERSITY NOTICE BOARD[/link] [blink]:red_heart-emoji:[/blink]",style="bold blue underline") 

try:
    response = requests.get(URL)
    # print("debugging\n")
except(ConnectionError,ConnectionAbortedError,ConnectionRefusedError,ConnectionResetError):
    response = requests.get(URL)
    # print("debugging\n")

soup = BeautifulSoup(response.content, "html.parser")
results = soup.find(class_="site-main")
articles = results.findAll("article", class_ ="category-notices")



for article in articles:
    try:
        issue_date = article.find(class_="entry-date published").text.strip()
    except (AttributeError):
        issue_date = article.find(class_="entry-date published updated").text.strip()

    Title = article.find(class_="entry-title").text.strip()
    description = article.find(class_="entry-content").text.strip()
    
    console.print(f"\n{issue_date}",style="")
    console.print(f"[bold red]Notice [/bold red]: [bold white]{Title}[/bold white]")
    if description:
        console.print(f"[bold green]Description [/bold green]: [italic]{description}[/italic]")
