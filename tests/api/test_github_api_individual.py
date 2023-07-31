import pytest

@pytest.mark.api_indi
def test_existed_commits(github_api):
    r = github_api.get_list_commits('olena-yerkovich','yerkovich_qa')
    assert r[0]['commit']['author']['name'] == 'Olena Yerkovich' 


@pytest.mark.api_indi
def test_not_existed_commits(github_api):
    r = github_api.get_list_commits('olena-yerkovich','yerkovich_qa')
    assert r[3]['commit']['author']['name'] != 'Sergii Butenko' 


@pytest.mark.api_indi
def test_existed_commits2(github_api):
    r = github_api.get_list_commits('olena-yerkovich','yerkovich_qa')
    assert 'Olena' in r[0]['commit']['author']['name']  


@pytest.mark.api_indi
def test_commits_email(github_api):
    r = github_api.get_list_commits('olena-yerkovich','yerkovich_qa')
    assert r[0]['commit']['committer']['email'] == 'olenka.yerkovich@gmail.com' 