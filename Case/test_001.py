import pytest

@pytest.fixture()
def test_xx():
    print("@@@@@@")

@pytest.mark.usefixtures("test_xx")
class Test001:
    def test_aa(self):
        print("#######")

    def test_bb(self):
        print("*******")


