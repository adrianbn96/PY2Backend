from django.db.models.fields.files import ImageField
from graphene import Field
from graphene import Mutation
from graphene.types.scalars import (
    ID,
    String,
    Boolean
)
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from temple.models import Usuario
from graphqlApi.data.Usuario.types import UsuarioNode
from graphqlApi.data.Usuario.inputs import CreateUserInput
from graphqlApi.data.Usuario.inputs import UpdateUserInput

from graphqlApi.utils import delete_attributes_none
from graphqlApi.utils import transform_global_ids

# Create your mutations here

class CreateUsuario(Mutation):
    """Clase para crear Manager"""

    usuario = Field(UsuarioNode)

    class Arguments:
        input = CreateUserInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        usuario = Usuario.objects.create(**input)

        return CreateUsuario(usuario=usuario)

class UpdateUsuario(Mutation):
    """Clase para actualizar establecimientos"""

    usuario = Field(UsuarioNode)

    class Arguments:
        input = UpdateUserInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        usuario = Usuario.objects.get(pk=input.get('id'))
        Usuario.objects.filter(pk=input.get("id")).update(**input)
        return UpdateUsuario(usuario=usuario)


class DeleteManager(Mutation):
    """Clase para eliminar establecimientos"""

    usuario = Field(UsuarioNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]

        try:
            usuario = Usuario.objects.get(pk=input)
            Usuario.objects.filter(pk=input).delete()
        except Usuario.DoesNotExist:
            raise GraphQLError('Manager does not delete')

        return CreateUsuario(usuario=Usuario)
