from modules.api.clients.github import GitHub
import pytest


owner = 'olena-yerkovich'
repo = 'yerkovich_qa'
expected_commit_email = 'olenka.yerkovich@gmail.com'
expected_commit_author_name = 'Olena Yerkovich'
unexpected_commit_author_name = 'Sergii Butenko123'


@pytest.mark.api_indi
def test_existed_commits(github_api):
    commits = github_api.get_list_commits(owner, repo)
    
    assert commits[-1]['commit']['author']['name'] == expected_commit_author_name

@pytest.mark.api_indi
def test_not_existed_commits(github_api):
    commits = github_api.get_list_commits(owner, repo)
    
    assert commits[3]['commit']['author']['name'] != unexpected_commit_author_name 

@pytest.mark.api_indi
def test_existed_commits2(github_api):
    commits = github_api.get_list_commits(owner, repo)
    
    assert 'Olena' in commits[-1]['commit']['author']['name']  

@pytest.mark.api_indi
def test_commits_email(github_api):
    commits = github_api.get_list_commits(owner, repo)
    
    assert commits[-1]['commit']['committer']['email'] == expected_commit_email 

@pytest.mark.api_indi
def test_create_issue(github_api):
    issue_data = {
        "title": "Test Issue1",
        "body": "This is a test issue1",
        "assignee": None,
        "milestone": None,
        "labels": ["bug", "enhancement"]
    }
    created_issue = github_api.create_issue(owner, repo, issue_data)
    print("Issue created successfully. Issue number:", created_issue["number"])
    
