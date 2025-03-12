from pydantic.dataclasses import dataclass
from typing import List

@dataclass
class EmailDict:
    email_body: str
    email_subject: str 
    recipients: List[str]