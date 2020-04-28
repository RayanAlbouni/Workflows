from rest_framework import serializers
from workflowsproject.workflows.models import Workflow, Step, Comment

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('name', 'description')

class WorkflowSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = Workflow
        fields = ('id', 'name', 'description', 'steps')

    def create(self, validated_data):
        steps = validated_data.pop('steps', [])
        workflow = Workflow.objects.create(**validated_data)
        index = 0
        for step_data in steps:
            index = index + 1
            Step.objects.create(workflow=workflow, order=index, **step_data)
        return workflow

    def update(self, workflow, validated_data):
        # Update the workflow properties
        workflow.name = validated_data.get('name', workflow.name)
        workflow.description = validated_data.get('description', workflow.description)
        workflow.save()

        # Update the workflow Steps
        # First delete all old steps for this workflow
        workflow_steps = dict((i.id, i) for i in workflow.steps.all())
        for item in workflow_steps.values():
            item.delete()

        # Then add the new Steps
        steps = validated_data.pop('steps', [])
        index = 0
        for step_data in steps:
            index = index + 1
            step = Step.objects.create(workflow=workflow, name=step_data['name'], description=step_data['description'],
                                       order=index)
            workflow.steps.add(step)
        return workflow

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'name', 'text')













