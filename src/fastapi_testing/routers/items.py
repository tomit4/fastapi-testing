from typing import Annotated

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

fake_secret_token = "coneofsilence"


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


router = APIRouter(
    prefix="/items",
    tags=["items"],
)

fake_db: dict[str, Item] = {
    "foo": Item(id="foo", title="Foo", description="There goes my hero"),
    "bar": Item(id="bar", title="Bar", description="The bartenders"),
}


@router.get("/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: Annotated[str, Header()]) -> Item:
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@router.post("/", response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header()]) -> Item:
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=409, detail="Item already exists")
    fake_db[item.id] = item
    return item
