import graphene

from graphene_django.types import DjangoObjectType

from django_graphene.graphene_app.models import ExampleResource


class ExampleResourceType(DjangoObjectType):
    class Meta:
        model = ExampleResource


class Query(object):
    all_example_resources = graphene.List(ExampleResourceType)

    example_resource = graphene.Field(ExampleResourceType, id=graphene.UUID())

    def resolve_example_resource(self, info, **kwargs):

        id = kwargs.get('id')

        if id is not None:
            return ExampleResource.objects.get(id=id)

    def resolve_all_example_resources(self, info, **kwargs):
        return ExampleResource.objects.all()
