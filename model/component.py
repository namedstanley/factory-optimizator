from dataclasses import dataclass

@dataclass
class Component:

    id: str
    name: str
    price: float
    assembly_time: float