import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.category import Category  # noqa: E501
from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server import util


def add_pet(body):  # noqa: E501
    """Add a new pet to the store

    Add a new pet to the store # noqa: E501

    :param body: Create a new pet in the store
    :type body: dict | bytes

    :rtype: Pet
    """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_pet(id, name, category, photo_urls, tags, status):  # noqa: E501
    """Add a new pet to the store

    Add a new pet to the store # noqa: E501

    :param id: 
    :type id: int
    :param name: 
    :type name: str
    :param category: 
    :type category: dict | bytes
    :param photo_urls: 
    :type photo_urls: List[str]
    :param tags: 
    :type tags: list | bytes
    :param status: 
    :type status: str

    :rtype: Pet
    """
    if connexion.request.is_json:
        category = Category.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        tags = [Tag.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_pet(pet_id, api_key=None):  # noqa: E501
    """Deletes a pet

    delete a pet # noqa: E501

    :param pet_id: Pet id to delete
    :type pet_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def find_pets_by_status(status=None):  # noqa: E501
    """Finds Pets by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Pet]
    """
    return 'do some magic!'


def find_pets_by_tags(tags=None):  # noqa: E501
    """Finds Pets by tags

    Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[Pet]
    """
    return 'do some magic!'


def get_pet_by_id(pet_id):  # noqa: E501
    """Find pet by ID

    Returns a single pet # noqa: E501

    :param pet_id: ID of pet to return
    :type pet_id: int

    :rtype: Pet
    """
    return 'do some magic!'


def update_pet(body):  # noqa: E501
    """Update an existing pet

    Update an existing pet by Id # noqa: E501

    :param body: Update an existent pet in the store
    :type body: dict | bytes

    :rtype: Pet
    """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_pet(id, name, category, photo_urls, tags, status):  # noqa: E501
    """Update an existing pet

    Update an existing pet by Id # noqa: E501

    :param id: 
    :type id: int
    :param name: 
    :type name: str
    :param category: 
    :type category: dict | bytes
    :param photo_urls: 
    :type photo_urls: List[str]
    :param tags: 
    :type tags: list | bytes
    :param status: 
    :type status: str

    :rtype: Pet
    """
    if connexion.request.is_json:
        category = Category.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        tags = [Tag.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def update_pet_with_form(pet_id, name=None, status=None):  # noqa: E501
    """Updates a pet in the store with form data

     # noqa: E501

    :param pet_id: ID of pet that needs to be updated
    :type pet_id: int
    :param name: Name of pet that needs to be updated
    :type name: str
    :param status: Status of pet that needs to be updated
    :type status: str

    :rtype: None
    """
    return 'do some magic!'


def upload_file(pet_id, body=None, additional_metadata=None):  # noqa: E501
    """uploads an image

     # noqa: E501

    :param pet_id: ID of pet to update
    :type pet_id: int
    :param body: 
    :type body: dict | bytes
    :param additional_metadata: Additional Metadata
    :type additional_metadata: str

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
