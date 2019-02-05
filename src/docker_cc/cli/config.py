import dataclasses
from typing import List


@dataclasses.dataclass
class Configuration:
    path: str
    name: str
    includes: List[str]

    @property
    def main_file(self):
        for
