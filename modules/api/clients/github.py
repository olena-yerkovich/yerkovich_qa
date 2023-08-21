import requests
from config.config import Config


class GitHub:

   
   base_url = "https://api.github.com"
   
   
   def get_user(self, username):
      r = requests.get(f'{self.base_url}/{username}')
      body = r.json()

      return body

   def search_repo(self,name):
      r = requests.get(f"{self.base_url}/search/repositories", params = {"q": name})
      body = r.json()

      return body
   
   def get_list_commits(self, owner,repo):
      r = requests.get(f'{self.base_url}/repos/{owner}/{repo}/commits')
      body = r.json()

      return body
   
   def create_issue(self, owner, repo, issue_data):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + Config.ACCESS_TOKEN,
            "X-GitHub-Api-Version": "2022-11-28" 
        }
        response = requests.post(url, headers=headers, json=issue_data)
        
        if response.status_code == 201:
            return response.json()
        
        else:
            raise Exception(f"Error creating issue. Status code: {response.status_code}, Message: {response.text}")
        
        