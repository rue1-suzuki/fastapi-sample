from fastapi import APIRouter

from .views.create import create
from .views.delete import delete
from .views.get import get
from .views.list import list
from .views.update import update

router = APIRouter(tags=['Item'])
router.add_api_route(methods=['POST'], path='/', endpoint=create)
router.add_api_route(methods=['GET'], path='/', endpoint=list)
router.add_api_route(methods=['GET'], path='/{item_id}', endpoint=get)
router.add_api_route(methods=['PUT'], path='/{item_id}', endpoint=update)
router.add_api_route(methods=['DELETE'], path='/{item_id}', endpoint=delete)
