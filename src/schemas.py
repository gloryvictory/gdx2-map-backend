from datetime import datetime

from pydantic import BaseModel


class BaseTable(BaseModel):
    class Config:
        from_attributes = True


class S_TEST(BaseTable):
    id: int
    