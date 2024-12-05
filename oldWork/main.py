from urllib.request import urlopen, Request

# URL of website
# url = "http://olympus.realpython.org/profiles/aphrodite"
url = "https://www.thecragandcanyon.ca/"

#This makes it seem like its coming from a website
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.3"}

# Create a Request object with the specified URL and headers
req = Request(url, headers=headers)

# Open the URL with the Request object
page = urlopen(req)

# Read and decode the HTML content
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# This will print all HTML of the website
#print(html)

# Extract the title from the HTML
title_index = html.find("<p>")
start_index = title_index + len("<p>")
end_index = html.find("</p>")
title = html[start_index:end_index]

print(title)


#<a aria-label="Calgary Police Service badge stolen near Canmore hiking trail" class="article-card__link" href="/news/local-news/calgary-police-service-badge-stolen-near-canmore-hiking-trail/wcm/7918a499-3bc7-4216-85cc-32490ba223b5"> <h2 class="article-card__headline text-size--massive--sm-up text-size--huge--sm-down" title="Calgary Police Service badge stolen near Canmore hiking trail"><span class="article-card__headline-clamp">Calgary Police Service badge stolen near Canmore hiking trail</span></h2> <p class="article-card__excerpt first">Calgary police are asking the public to help locate a stolen police badge that was taken from a parked vehicle outside Canmore.</p> </a>