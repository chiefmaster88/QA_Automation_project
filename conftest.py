import pytest
from modules.apiclients.github import GitHhub

@pytest.fixture
def  github_api():
    obj = GitHhub()
    yield obj
