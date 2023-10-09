import pytest

from bsc_utils.chat import Messenger

default_skip = pytest.mark.skipif("not config.getoption('nonskip')")


@pytest.fixture
def client():
    return Messenger()


@default_skip
def test_send_message(client):
    client.send_message(
        msg='Test',
        target_id='19:eec1674bb8484fc995a279a082a4e428@thread.skype'
    )


@default_skip
def test_send_attachment(client):
    client.send_attachment(
        image_path='//10.21.184.186/sharefolder/logo BSC 2022.jpg',
        target_id='19:eec1674bb8484fc995a279a082a4e428@thread.skype'
    )
