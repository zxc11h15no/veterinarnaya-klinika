from fastapi import APIRouter
from sql_base.models import animals
import resolvers.animals

animals_router = APIRouter()


@animals_router.get('/')
def get_animals():
    return f'Response:{{text:Страница со списком животных}}'


@animals_router.post("/")
def new_animals(animals: animals, ):
    new_id = resolvers.animals.new_animals(animals)
    return f"{{code: 201, id: {new_id}}}"
