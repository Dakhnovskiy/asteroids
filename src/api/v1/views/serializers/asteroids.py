from typing import List

from pydantic import BaseModel


class OrbitClass(BaseModel):
    orbit_class_type: str
    orbit_class_description: str
    orbit_class_range: str


class OrbitalData(BaseModel):
    orbit_id: str
    orbit_class: OrbitClass


class Asteroids(BaseModel):
    id: str
    neo_reference_id: str
    name: str
    designation: str
    nasa_jpl_url: str
    absolute_magnitude_h: float

    orbital_data: OrbitalData

    images_links: List[str] = []
