from app import app
import api
import unittest


class FlaskTest(unittest.TestCase):
    def runTest_update_text(self):
        tester = app.test_client(self)
        resp, response_status = api.get_data_from_api()
        status_code = response_status
        self.assertEqual(status_code, 200)
        print("test case 1 completed")


if __name__ == "__main__":
    tester = FlaskTest()
    tester.runTest_update_text()
