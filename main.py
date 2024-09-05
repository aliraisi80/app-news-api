import requests
from send_email import send_email

qpi_key="bc16ed21dfd948069633edc0a8db947a"

url="https://newsapi.org/v2/everything?q=tesla&\
from=2024-08-05&sortBy=publishedAt&\
apiKey=bc16ed21dfd948069633edc0a8db947a"

kesponse=requests.get(url)

content=kesponse.json()

body="Subject:Today's new\n\n"

for article in content["articles"][:20]:
    if article["title"]is not None and article["description"] is not None:
        body=body+article["title"] + "\n" \
              +article["description"]\
              +"\n" + article["url"]+2*"\n"
body=body.encode("utf-8")
send_email(message=body)
