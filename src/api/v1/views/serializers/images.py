import datetime

from pydantic import BaseModel


class Images(BaseModel):
    id: int
    image_datetime: datetime.datetime
