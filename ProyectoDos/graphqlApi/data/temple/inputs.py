from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean
from graphene_file_upload.scalars import Upload
# Create your inputs types here.


class CreateTempleInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de establecimientos
    """

    name = String(required=True)
    

