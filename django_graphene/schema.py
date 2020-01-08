

import graphene

import django_graphene.graphene_app.schema


class Query(django_graphene.graphene_app.schema.Query, graphene.ObjectType):

    pass


schema = graphene.Schema(query=Query)
