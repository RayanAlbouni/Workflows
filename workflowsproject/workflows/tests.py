from django.test import TestCase, Client
from rest_framework import status
from .models import Workflow, Comment, Step
from .serializers import WorkflowSerializer


# initialize the APIClient app
client = Client()

valid_workflow = {
            'name': 'How to nail something',
            'description': 'Basic instructions to nail something',
            'steps': [
                {
                    'name': 'Place nail',
                    'description': 'Hold nail on top the thing to be nailed'
                },
                {
                    'name': 'Hit nail',
                    'description': 'Hit the nail repeatedly with a hammer'
                }
            ]
        }
invalid_workflow = {
            'name': '',
            'description': 'Basic instructions to nail something',
            'steps': [
                {
                    'name': 'Place nail',
                    'description': 'Hold nail on top the thing to be nailed'
                },
                {
                    'name': 'Hit nail',
                    'description': 'Hit the nail repeatedly with a hammer'
                }
            ]
        }

valid_comment = {
            'name': 'Concerned  person',
            'text': 'On the step Hit Nail be careful to not hit your hand!'
}
invalid_comment = {
            'name': '',
            'text': 'On the step Hit Nail be careful to not hit your hand!'
}



# Create your tests here.
class WorkflowTest(TestCase):
    """ Test module for Workflow API"""

    def setUp(self):
        """ Create initial valid workflow before """
        response = self.client.post('/workflow/', valid_workflow, content_type='application/json')

    def test_create_valid_workflow(self):
        response = self.client.post('/workflow/', valid_workflow, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_workflow(self):
        response = self.client.post('/workflow/', invalid_workflow, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_workflow(self):
        response = self.client.get('/workflow/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_first_workflow(self):
        response = self.client.get('/workflow/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nor_exist_workflow(self):
        response = self.client.get('/workflow/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_workflow(self):
        response = self.client.put('/workflow/1/', valid_workflow, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_workflow(self):
        response = self.client.delete('/workflow/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CommentTest(TestCase):
    """ Test module for Workflow API"""

    def setUp(self):
        """ Create initial valid workflow and a valid comment"""
        workflow = self.client.post('/workflow/', valid_workflow, content_type='application/json')
        comment = self.client.post('/comment/1/', valid_comment, content_type='application/json')

    def test_create_valid_comment(self):
        response = self.client.post('/comment/1/', valid_comment, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_comment(self):
        response = self.client.post('/comment/1/', invalid_comment, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_comment_for_workflow(self):
        response = self.client.get('/comment/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_first_comment(self):
        response = self.client.get('/comment/1/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nor_exist_workflow(self):
        response = self.client.get('/comment/1/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_comment(self):
        response = self.client.put('/comment/1/1/', valid_comment, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_workflow(self):
        response = self.client.delete('/comment/1/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



