import pytest
import time
from base.DriverClass import Driver


@pytest.fixture(scope='class')
def beforeClass(request):
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()

