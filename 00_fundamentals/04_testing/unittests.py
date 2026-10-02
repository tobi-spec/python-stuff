from unittest import TestCase, mock

def get_list() -> list:
    return ["apple", "banana", "cherry"]

def wrap_list() -> list:
    return get_list()


class TestExamples(TestCase):

    def test_get_list(self):
        assert get_list() == ["apple", "banana", "cherry"]

    def test_wrap_list(self):
        assert wrap_list() == ["apple", "banana", "cherry"]

    @mock.patch("basic.testing.unittests.get_list",  return_value=["decorator", "mock"])
    def test_get_list_mock_decorator(self, mock_get_list):
        assert get_list() == ["decorator", "mock"]

    def test_get_list_mock_context_manager(self):
        with mock.patch("basic.testing.unittests.get_list", return_value=["manager", "mock"]):
            assert get_list() == ["manager", "mock"]

    def test_get_list_mock_inline(self):
        self.patcher = mock.patch("basic.testing.unittests.get_list", return_value=["inline", "mock"])
        self.patcher.start()
        assert get_list() == ["inline", "mock"]
        self.patcher.stop()

    @mock.patch("basic.testing.unittests.get_list", return_value=["decorator", "mock"])
    def test_wrap_list_mock_get_list(self, mock_get_list):
        assert wrap_list() == ["decorator", "mock"]





