import pytest

owner = 'olena-yerkovich'
repo = 'yerkovich_qa'

@pytest.mark.api_indi
def test_existed_commits(github_api):
    commits = github_api.get_list_commits(owner, repo)
    
    assert commits[0]['commit']['author']['name'] == 'Olena Yerkovich' 

@pytest.mark.api_indi
def test_not_existed_commits(github_api):
    commits = github_api.get_list_commits(owner, repo)
    
    assert commits[3]['commit']['author']['name'] != 'Sergii Butenko' 

@pytest.mark.api_indi
def test_existed_commits2(github_api):
    commits = github_api.get_list_commits(owner, repo)
    
    assert 'Olena' in commits[0]['commit']['author']['name']  

@pytest.mark.api_indi
def test_commits_email(github_api):
    commits = github_api.get_list_commits(owner, repo)
    
    assert commits[0]['commit']['committer']['email'] == 'olenka.yerkovich@gmail.com' 