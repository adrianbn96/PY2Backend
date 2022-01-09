from graphene import Schema

from graphqlApi.schema import Query,Mutation

# Schema definition


schema = Schema(query=Query,mutation=Mutation)