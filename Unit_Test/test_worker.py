from unittest.mock import patch
from unittest import TestCase, mock
from Unit_Test.Worker import Worker
from unittest import TestCase





class TestWorker(TestCase):
   @mock.patch('Unit_Test.Worker.Worker', return_value="Roy Segal")

   def test_full_name(self, mock_full_name):
        with patch(Worker.full_name) as mocked_get:




        # job = Worker('Roy', 'Segal')
        # print(job.full_name())
        # self.assertIn(job.full_name(), "Roy Segal")





        # roy = Worker('Roy', 'Segal', 1998, 7, 26, "Ness ziona", 'il')









