from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from workflowsproject.workflows.models import Workflow, Step, Comment
from workflowsproject.workflows.serializers import WorkflowSerializer, CommentSerializer


# Create your views here.

class WorkflowList(APIView):
    def get(self,request):
        """
        List All Workflows
        """
        _workflow = Workflow.objects.all()
        _serializer = WorkflowSerializer(_workflow, many=True)
        return Response(_serializer.data)

    def post(self, request):
        """
        Create A New Workflow
        """
        _serializer = WorkflowSerializer(data=request.data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(_serializer.data, status=status.HTTP_201_CREATED)
        return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkflowDetails(APIView):
    def get_workflow(self, id):
        try:
            return Workflow.objects.get(pk=id)
        except Workflow.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """
        Get Workflow object by ID
        """
        _workflow = self.get_workflow(id)
        _serializer = WorkflowSerializer(_workflow)
        return Response(_serializer.data)

    def put(self, request, id, format=None):
        """
        Update workflow for the given ID
        :param request:
        :param id:
        :param format:
        :return:
        """
        _workflow = self.get_workflow(id)
        _serializer = WorkflowSerializer(_workflow, data=request.data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(_serializer.data)
        return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        """
        Delete a Workflow
        :param request:
        :param id:
        :param format:
        :return:
        """
        _workflow = self.get_workflow(id)
        _workflow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):

    def get_workflow(self, workflow_id):
        try:
            return Workflow.objects.get(pk=workflow_id)
        except Workflow.DoesNotExist:
            raise Http404

    def get(self, request, workflow_id, format=None):
        """
        List all Comments for a workflow
        :param request:
        :param workflow_id:
        :param format:
        :return:
        """
        _workflow = self.get_workflow(workflow_id)
        _comment = Comment.objects.all().filter(workflow=_workflow)
        _serializer = CommentSerializer(_comment, many=True)
        return Response(_serializer.data)

    def post(self, request, workflow_id, format=None):
        """
        Create a new Comment for a Workflow
        :param request:
        :param workflow_id:
        :param format:
        :return:
        """
        _workflow = self.get_workflow(workflow_id)
        _serializer = CommentSerializer(data=request.data)
        if _serializer.is_valid():
            _serializer.save(workflow=_workflow)
            return Response(_serializer.data, status=status.HTTP_201_CREATED)
        return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetails(APIView):
    """
    Retrieve, update or delete a Comment instance.
    """
    def get_comment(self , id, workflow):
        try:
            return Comment.objects.get(pk=id, workflow=workflow)
        except Comment.DoesNotExist:
            raise Http404

    def get_workflow(self, workflow_id):
        try:
            return Workflow.objects.get(pk=workflow_id)
        except Workflow.DoesNotExist:
            raise Http404

    def get(self, request, workflow_id, id):
        _workflow = self.get_workflow(workflow_id)
        _comment = self.get_comment(id, _workflow)
        _serializer = CommentSerializer(_comment)
        return Response(_serializer.data)

    def put(self, request, workflow_id, id):
        _workflow = self.get_workflow(workflow_id)
        _comment = self.get_comment(id, _workflow)
        _serializer = CommentSerializer(_comment, data=request.data)
        if _serializer.is_valid():
            _serializer.save(workflow=_workflow)
            return Response(_serializer.data)
        return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, workflow_id, id):
        _workflow = self.get_workflow(workflow_id)
        _comment = self.get_comment(id, _workflow)
        _comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


