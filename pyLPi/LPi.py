from ppl import Variable, Linear_Expression, Constraint
# from RankConfig import getLPMod
import LPppl
import LPz3


class C_Polyhedron:
    _poly = None

    def __init__(self, cons, dim=-1, lplib=None):
        if lplib is None:
            lplib = "ppl"  # get_LP_lib_name()
        if lplib == "ppl":
            self._poly = LPppl.C_Polyhedron(cons, dim)
        elif lplib == "ppl":
            self._poly = LPppl.C_Polyhedron(cons, dim)

    def add_constraint(self, constraint):
        self._poly.add_constraint(constraint)

    def add_constraints(self, constraints):
        self._poly.add_constraints(constraints)

    def get_dimension(self):
        return self._poly.get_dimension()

    def get_constraints(self):
        return self._poly.get_constraints()

    def minimize(self):
        return self._poly.minimize()

    def maximize(self):
        return self._poly.maximize()

    def is_empty(self):
        return self._poly.is_empty()

    def get_point(self):
        return self._poly.get_point()

    def is_implied(self, constraint):
        return self._poly.is_implied(constraint)

    def is_disjoint_from(self, polyhedron):
        return self._poly.is_disjoint_from(polyhedron)

    def __repr__(self):
        return self._poly.__repr__()

    def get_generators(self):
        return self._poly.get_generators()

    def int_minimize(self, something):
        return self._poly.int_minimize(something)

    def int_maximize(self, something):
        return self._poly.int_maximize(something)

    def is_bounded(self):
        return self._poly.is_bounded()

    def get_integer_point(self):
        return self._poly.get_integer_point()

    def get_relative_interior_point():
        return self._poly.get_relative_interior_point()

    def minimize_constraint_system():
        return self._poly.minimize_constraint_system()