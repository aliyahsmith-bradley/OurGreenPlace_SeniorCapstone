import pytest
from website import create_app, db

@pytest.fixture
def app():

    # Creates database in memory for testing purposes 
    app = create_app("sqlite:///:memory:")

    # Puts models into database 
    with app.app_context():
        db.create_all()

    yield app # tear down comes after yield 

@pytest.fixture
def client(app):
    return app.test_client()    