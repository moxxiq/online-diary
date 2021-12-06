import pytest
from starlette.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy_utils import database_exists, create_database, drop_database
# from alembic import command
# from alembic.config import Config

from app.main import v1
from app.config import DATABASE_URL


# @pytest.fixture(scope="session", autouse=True)
# def create_test_database():
#     url = DATABASE_URL
#     engine = create_engine(url)
#     assert not database_exists(url), 'Test database already exists. Aborting tests.'
#     create_database(url)             # Create the test database.
#     config = Config("alembic.ini")   # Run the migrations.
#     config.set_main_option('sqlalchemy.url', DATABASE_URL)
#     command.upgrade(config, "head")
#     yield                            # Run the tests.
#     drop_database(url)               # Drop the test database.
#     #  https://www.starlette.io/database/#migrations

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(v1)
    yield client  # testing happens here
