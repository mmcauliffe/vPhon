import pytest
import os


@pytest.fixture(scope='session')
def test_dir():
    base = os.path.dirname(os.path.abspath(__file__))
    generated = os.path.join(base, 'data', 'generated')
    if not os.path.exists(generated):
        os.makedirs(generated)
    return os.path.join(base, 'data')


@pytest.fixture(scope='session')
def south_kwargs():
    return {'dialect': 's', 'pham': False, 'cao': False, 'palatals': False, 'glottal': False}
