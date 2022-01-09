from graphene.relay import Node
from graphene_django import DjangoObjectType


from graphqlApi.connections import TotalCountConnection
from temple.models import SolicitudPartida

# Create your objects types here.

class SolicitudPartidaNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = SolicitudPartida
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection