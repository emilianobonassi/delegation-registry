import pytest

@pytest.fixture()
def deployer(accounts):
    return accounts[0]

@pytest.fixture()
def delegator(accounts):
    return accounts[1]

@pytest.fixture()
def delegate(accounts):
    return accounts[2]

@pytest.fixture()
def registry(deployer, project):
    return deployer.deploy(project.DelegationRegistry)
