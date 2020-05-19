from .abc import MoleculeABC
from ..algorithms import Isomorphism, Components


class Molecule(Isomorphism, Components, MoleculeABC):
    __slots__ = ()

    def get_atom(self, number: int):
        return self._atoms[number]

    def get_bond(self, start_atom: int, end_atom: int):
        return self._bonds[start_atom][end_atom]

    def add_atom(self, element: Element, number: int, charge: int = 0):
        if number in self._atoms:
            raise KeyError
        else:
            self._atoms[number] = element
            self._bonds = {}

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if not isinstance(start_atom, int) and not isinstance(end_atom, int) and not isinstance(bond_type, int):
            raise TypeError
        elif start_atom not in self._atoms:
            raise KeyError
        elif end_atom not in self._atoms:
            raise KeyError
        elif start_atom == end_atom:
            raise KeyError
        else:
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[end_atom][start_atom] = bond_type

    def delete_atom(self, number: int):
        del self._atoms[number]
        del self._bonds[number]

    def delete_bond(self, start_atom: int, end_atom: int):
        del self._bonds[start_atom][end_atom]
        del self._bonds[end_atom][start_atom]

    def update_atom(self, element: Element, number: int):
        if number in self._atoms:
            self._atoms[number] = element
        else:
            raise KeyError

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom in self._bonds and end_atom in self._bonds:
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[end_atom][start_atom] = bond_type
        else:
            raise KeyError

    def enter(self):
        self._backup_atoms = self._atoms.copy()
        self._backup_bonds = dict()
        for i, j in self._bonds.items():
            self._backup_bonds[i] = j

    def exit(self, exc_type, exc_val, exc_tb):
        self._atoms = self._backup_atoms
        self._bonds = self._backup_bonds
        del self._backup_atoms
        del self._backup_bonds
        if exc_val is None:
            del self._backup_atoms
            del self._backup_bonds
        else:
            self._atoms = self._backup_atoms
            self._bonds = self._backup_bonds
            del self._backup_atoms
            del self._backup_bonds

    def str(self):
        ...


__all__ = ['Molecule']
