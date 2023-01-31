from unittest import mock

import pytest


@mock.patch('api_hoco.models.Activity.Activity.remove')
def test_remove_activity_id_invalido(mock_remove, controller_activity):
    mock_remove.return_value = None
    with pytest.raises(Exception) as excinfo:
        activity_id = 0
        email = "email@"
        controller_activity.del_user_activity(activity_id, email)
    assert str(excinfo.value) == f'Error: activity_id is invalid'


@mock.patch('api_hoco.models.Activity.Activity.remove')
def test_remove_activity_sem_id(mock_remove, controller_activity):
    mock_remove.return_value = None
    with pytest.raises(Exception) as excinfo:
        activity_id = None
        email = "email@"
        controller_activity.del_user_activity(activity_id, email)
    assert str(excinfo.value) == f'Error: activity_id is invalid'


@mock.patch('api_hoco.models.Activity.Activity.remove')
def test_remove_activity_email_invalido(mock_remove, controller_activity):
    mock_remove.return_value = None
    with pytest.raises(Exception) as excinfo:
        activity_id = "ID"
        email = 0
        controller_activity.del_user_activity(activity_id, email)
    assert str(excinfo.value) == f'Error: invalid email'


@mock.patch('api_hoco.models.Activity.Activity.remove')
def test_remove_activity_sem_email(mock_remove, controller_activity):
    mock_remove.return_value = None
    with pytest.raises(Exception) as excinfo:
        activity_id = "ID"
        email = None
        controller_activity.del_user_activity(activity_id, email)
    assert str(excinfo.value) == f'Error: invalid email'


@mock.patch('api_hoco.models.Activity.Activity.remove')
@mock.patch('api_hoco.controllers.activity.get_all_activity')
def test_remove_activity_successful( mock_get_all, mock_remove, controller_activity):
    activity_id = "ID"
    email = "email@"
    expected_return = {'_id':'ID', 'e-mail':'email@'}
    mock_get_all.return_value = expected_return
    mock_remove.return_value = 1
    result = controller_activity.del_user_activity(activity_id, email)
    assert result == expected_return


@mock.patch('api_hoco.models.Activity.Activity.remove')
def test_remove_activity_no_exist(mock_remove,  controller_activity):
    activity_id = "ID nao existe"
    email = "email@"
    mock_remove.return_value = None
    result = controller_activity.del_user_activity(activity_id, email)
    assert result is None


@mock.patch('api_hoco.models.Activity.Activity.update')
@mock.patch('api_hoco.models.Activity.Activity.get_all')
def test_update_activity_successful(mock_get_all, mock_update, controller_activity):
    certificate = None
    data = {"e-mail":"email@", "data":"edit"}
    expected_return = [{"_id":"ATV1", "data":"edit"}, {"_id":"ATV2"}]
    mock_update.return_value = {"_id":"ATV1", "data":"edit"}
    mock_get_all.return_value = expected_return
    result = controller_activity.edit_activity(certificate, data)
    assert result == expected_return


@mock.patch('api_hoco.models.Activity.Activity.update')
def test_update_activity_email_invalido(mock_update, controller_activity):
    mock_update.return_value = None
    with pytest.raises(Exception) as excinfo:
        certificate = None
        data = {"e-mail":0, "data":"edit"}
        controller_activity.edit_activity(certificate, data)
    assert str(excinfo.value) == f'Error: invalid email'

@mock.patch('api_hoco.models.Activity.Activity.update')
def test_update_activity_sem_email(mock_update, controller_activity):
    mock_update.return_value = None
    with pytest.raises(Exception) as excinfo:
        certificate = None
        data = {"data":"edit"}
        controller_activity.edit_activity(certificate, data)
    assert str(excinfo.value) == f'Error: invalid email'
