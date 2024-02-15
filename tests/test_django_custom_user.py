
import pytest
from django_custom_user.django_custom_user import django_custom_user 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = django_custom_user()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = django_custom_user(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

