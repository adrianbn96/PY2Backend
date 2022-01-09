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

from temple.models import SolicitudPartida
from graphqlApi.data.temple.types import SolicitudPartidaNode
from graphqlApi.data.temple.inputs import CreateTempleInput

from graphqlApi.utils import delete_attributes_none
from graphqlApi.utils import transform_global_ids

# Create your mutations here