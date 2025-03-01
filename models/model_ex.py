from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(..., description="유저 아이디", example="iamdoctor")
    name: str = Field(..., description="유저 이름", example="홍길동")
    phoneNumber: str = Field(..., description="유저 휴대전화번호", example="01012345678")
