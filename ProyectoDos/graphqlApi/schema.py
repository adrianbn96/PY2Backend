from graphene import ObjectType
from graphene.relay import Node
import graphene
import graphql
import graphql_jwt
from graphene_django.filter import DjangoFilterConnectionField

from temple.models import SolicitudPartida,Usuario

from .data.SolicitudPartida.types import SolicitudPartidaNode
from .data.Usuario.types import UsuarioNode

from .data.Usuario.mutations import CreateUsuario, DeleteManager,UpdateUsuario

class Query(ObjectType):
    """Endpoint para consultar registros"""

    
    solicituPartida = Node.Field(SolicitudPartidaNode)
    usuario = Node.Field(UsuarioNode)
    all_solicitudPartidas = DjangoFilterConnectionField(SolicitudPartidaNode)
    all_usuarios = DjangoFilterConnectionField(UsuarioNode)

class Mutation(ObjectType):

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    create_usuario = CreateUsuario.Field()
    delete_usuario = DeleteManager.Field()
    update_usuario = UpdateUsuario.Field()