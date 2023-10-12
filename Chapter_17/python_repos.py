import requests

# Make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dicts = r.json()
print(f"Total repositories: {response_dicts['total_count']}")

# Explore information about the repositories
response_dicts 
# Process results
print(response_dicts.keys())