import pytest

existing_username = 'defunkt'
not_existing_username = 'butenkosergii'
existing_repo = 'become-qa-auto'
not_existing_repo = 'sergiibutenko_repo_non_exist123'

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user(existing_username)
    
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user(not_existing_username)
    
    assert user['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo(existing_repo)
    
    assert repo['total_count'] == 43
    assert 'become-qa-auto' in repo['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo = github_api.search_repo(not_existing_repo)
    
    assert repo['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo = github_api.search_repo('s')
    
    assert repo['total_count'] != 0