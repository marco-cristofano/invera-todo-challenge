from rest_framework import status
from utils.testing.api_test import CustomAPITestCase
from tasks.factories.task import TaskFactory


class APITaskPatchTests(CustomAPITestCase):
    url = '/api/v1/tasks/'
    body = {
        'completed': False
    }

    def setUp(self):
        super().setUp()
        self.task = TaskFactory()

    def test_uptade_not_allowed(self):
        response = self.client.patch(self.url, self.body)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )
