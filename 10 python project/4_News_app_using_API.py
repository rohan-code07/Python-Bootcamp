import requests

# Ask the user what type of news they want to search for
date = input("Enter the date from you want articles[not more than 1 month prior](20XX-Month-Day): ")
query = input("What type of news are you interested in today?\n")

# Your personal API key (keep it private!)
api = "bdc838081f6c42c08c42a533c8d0c093"            

# Build the API URL by inserting the user's search query and API key
url = f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey={api}" 

# Print the complete URL (useful for debugging)
print(url) 

# Send a GET request to the NewsAPI server
r = requests.get(url)

# Convert the JSON response into a Python dictionary
data = r.json()

# Extract only the list of news articles from the dictionary
articles = data['articles'] 
result = data['totalResults']
print("\n" , result , "\n")

# Loop through every article one by one
for index, article in enumerate(articles, start=1):
    # Print the article number, title and URL
    print(f"{index}. {article["title"]} : {article["url"]}")
    print("\n", "="*90, "\n")