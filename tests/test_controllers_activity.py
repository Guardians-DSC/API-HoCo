from unittest import mock

import pytest


@mock.patch('api_hoco.models.Activity.Activity.remove')
def test_remove_activity_id_invalido(mock_comercio_by_name, controller_activity):
    mock_comercio_by_name.return_value = None
    with pytest.raises(Exception) as excinfo:
        activity_id = {"dict": "nao sou uma string"}
        email = "email valido"
        controller_activity.del_user_activity(activity_id, email)
    assert str(excinfo.value) == f'Error: activity_id is invalid'


