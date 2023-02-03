from unittest import mock

import pytest

from mongomock.gridfs import enable_gridfs_integration
import mongomock

enable_gridfs_integration()

DB_TEST = mongomock.MongoClient().tests_solanches


@pytest.fixture(scope='session', autouse=True)
def teardown():
    mock.patch('api_hoco.connect2db.DB', DB_TEST).start()
    mock.patch('api_hoco.models.Activity.DB', DB_TEST).start()
    mock.patch('api_hoco.models.Question.DB', DB_TEST).start()
    yield


@pytest.fixture
def controller_activity():
    from api_hoco.controllers import activity
    yield activity
    from api_hoco.models import Activity
    Activity.DB.activity.delete_many({})


@pytest.fixture
def controller_questions():
    from api_hoco.controllers import questions
    yield questions
    from api_hoco.models import Question
    Question.DB.question.delete_many({})