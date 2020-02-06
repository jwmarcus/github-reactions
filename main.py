import urllib3

import json

### Reactions can be attached to:
# - commit comment
# - issue
# - issue comment
# - pull request review comment
# - team discussion
# - team discussion comment

# Example pull request review comment with reaction
owner = "urllib3"
repo = "urllib3"
comment_id = "550887874"
endpoint = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"

# Common endpoint-calling code

headers = {
    "Accept": "application/vnd.github.squirrel-girl-preview+json",
    "User-Agent": "jwmarcus",
}

http = urllib3.PoolManager()
r = http.request("GET", f"https://api.github.com{endpoint}", headers=headers)

if r.status == 200:
    reactions_json = json.loads(r.data.decode("utf-8"))
    print(json.dumps(reactions_json, indent=2, sort_keys=true))
else:
    print(r.status)
    print(r.data)
