# Data-Scraping


covering how HTML works, downloading web pages with `requests`, and parsing/extracting data with `BeautifulSoup`.

## Requirements

```bash
pip install requests beautifulsoup4
```

- How HTML structures content (tags like `<h1>`, `<p>`, etc.)
- Downloading a webpage with `requests.get()`
- Understanding HTTP status codes (200, 404, 500...)
- Parsing HTML with `BeautifulSoup`
- Extracting elements with `.find()`
- Saving scraped data to a file

## HTTP Status Codes

| Code | Meaning       |
|------|---------------|
| 200  | Success       |
| 404  | Page Not Found|
| 500  | Server Error  |



## Automation Workflow

```
Website → Download HTML → Parse HTML → Extract Data → Save Results
```
ject is for educational purposes only. Always check a website's `robots.txt` and terms of use before scraping it.
