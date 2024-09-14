from dotenv import load_dotenv
import os
import requests


load_dotenv()

username = os.getenv('GITHUB_USERNAME')
token_api = os.getenv('GITHUB_TOKEN')
name_repository = os.getenv('NAME_REPO')

github_api_url = 'https://api.github.com'

def test_avalible():
    site = requests.get(github_api_url)
    assert(site.status_code == 200)

def test_auth():
    site = requests.get(f'{github_api_url}/user',auth=(username, token_api))
    assert(site.status_code == 200)


def test_create_repository():
    payload = {
            'name':name_repository,
            'private':False
            }
    site = requests.post(f'{github_api_url}/user/repos',json=payload, auth=(username, token_api) )
    assert(site.status_code == 201 )


def test_check_repository():
    site = requests.get(f'{github_api_url}/users/{username}/repos')
    assert( any(repo['name'] == name_repository for repo in site.json()))

def test_delete_repository():
    site = requests.delete(f'{github_api_url}/repos/{username}/{name_repository}',auth=(username, token_api))
    assert(site.status_code == 204)
