from .abc import MoleculeABC
from ..algorithms import Isomorphism


class Molecule(Isomorphism, MoleculeABC):
    def add_atom(self, element: Element, number: int):
        if isinstance(element, str) and isinstance(number, int):
            self._atoms[number] = element
            self._bonds[number] = {}

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        ...



__all__ = ['Molecule']
