from typing import Optional
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup as bs

app = FastAPI()

@app.get("/companies")
def get_companies():
    r = requests.get("https://stockanalysis.com/list/sp-500-stocks/")
    soup = bs(r.content, "html.parser")

    companies = []
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if tds and len(tds) >= 7:
            companies.append({
                "No.": tds[0].text,
                "Symbol": tds[1].text,
                "Company Name": tds[2].text,
                "Market Cap": tds[3].text,
                "Stock Price": tds[4].text,
                "% Change": tds[5].text,
                "Revenue": tds[6].text
            })
    
    return {"companies": companies}
