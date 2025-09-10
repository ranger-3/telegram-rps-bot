import pytest


@pytest.fixture
def fake_update(mocker):
    def _make(text=None):
        update = mocker.Mock()
        message = mocker.Mock()
        message.text = text
        message.reply_text = mocker.AsyncMock()
        update.message = message
        return update

    return _make


@pytest.fixture
def fake_context(mocker):
    return mocker.Mock()
