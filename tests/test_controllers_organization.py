from pathlib import Path
from unittest import mock

import pytest

@mock.patch('api_hoco.models.Organization.Organization.save')
def test_register_org_successful(mock_save, controller_organization):
    resources = Path(__file__).parent / "resources"
    expected_return = {
	    "_id": "ID",
	    "name": "ORG",
	    "org_url": "<URL>",
	    "image": (resources / "image.png").open("rb")
    }
    name = "ORG"
    org_url = "<URL>"
    org_image = (resources / "image.png").open("rb")
    mock_save.return_value = expected_return
    result = controller_organization.register_org(name, org_url, org_image)
    assert result == expected_return


@mock.patch('api_hoco.models.Organization.Organization.find_orgs')
def test_get_orgs_successful(mock_find_orgs, controller_organization):
    resources = Path(__file__).parent / "resources"
    expected_return = [{
	    "_id": "ID",
	    "name": "ORG",
	    "org_url": "<URL>",
	    "image": (resources / "image.png").open("rb")
    }]
    mock_find_orgs.return_value = expected_return
    result = controller_organization.get_orgs()
    assert result == expected_return


@mock.patch('api_hoco.models.Organization.Organization.delete_org')
@mock.patch('api_hoco.models.Organization.Organization.find_orgs')
def test_remove_org_successful(mock_find_orgs, mock_delete_org, controller_organization):
    expected_return = []
    id_org = "ID"
    mock_delete_org.return_value = None
    mock_find_orgs.return_value = expected_return
    result = controller_organization.remove_org(id_org)
    assert result == expected_return
    