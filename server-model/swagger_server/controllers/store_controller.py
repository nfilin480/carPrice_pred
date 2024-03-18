import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server import util


def delete_order(order_id):  # noqa: E501
    """Delete purchase order by ID

    For valid response try integer IDs with value &lt; 1000. Anything above 1000 or nonintegers will generate API errors # noqa: E501

    :param order_id: ID of the order that needs to be deleted
    :type order_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_inventory():  # noqa: E501
    """Returns pet inventories by status

    Returns a map of status codes to quantities # noqa: E501


    :rtype: Dict[str, int]
    """
    return 'do some magic!'


def get_order_by_id(order_id):  # noqa: E501
    """Find purchase order by ID

    For valid response try integer IDs with value &lt;&#x3D; 5 or &gt; 10. Other values will generate exceptions. # noqa: E501

    :param order_id: ID of order that needs to be fetched
    :type order_id: int

    :rtype: Order
    """
    return 'do some magic!'


def place_order(body=None):  # noqa: E501
    """Place an order for a pet

    Place a new order in the store # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Order
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def place_order(id=None, pet_id=None, quantity=None, ship_date=None, status=None, complete=None):  # noqa: E501
    """Place an order for a pet

    Place a new order in the store # noqa: E501

    :param id: 
    :type id: int
    :param pet_id: 
    :type pet_id: int
    :param quantity: 
    :type quantity: int
    :param ship_date: 
    :type ship_date: str
    :param status: 
    :type status: str
    :param complete: 
    :type complete: bool

    :rtype: Order
    """
    ship_date = util.deserialize_datetime(ship_date)
    return 'do some magic!'
