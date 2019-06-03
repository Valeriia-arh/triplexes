import itertools
import sys
from collections import defaultdict

import common


class BaseGraph(object):
    def __init__(self):
        self.rna_elements = {}
        self.edges = dict()

    def connections(self, bulge):
        def sort_key(x):
            if self.rna_elements[x] and self.rna_elements[x][0] == 1:
                return 0
            return self.define(x)[0]
        connections = list(self.edges[bulge])
        connections.sort(key=sort_key)
        return connections

    def define(self, elem):
        if self.rna_elements[elem] == []:
            return self.define_a_zerolength(elem)
        elem = self.rna_elements[elem]
        new_def = []
        for i in range(0, len(elem), 2):
            new_def.append(max(elem[i] - 1, 1))
            new_def.append(elem[i + 1] + 1)
        return new_def

    def define_range_iterator(self, node):
        define = self.rna_elements[node]
        if define:
            yield [define[0], define[1]]
            if len(define) > 2:
                yield [define[2], define[3]]

    def get_sides(self, s1, bulge):
        if bulge not in self.edges[s1]:
            raise ValueError("Stem should be connected with bulge")
        s1d = self.rna_elements[s1]
        bd = self.rna_elements[bulge]
        if not bd:
            bd = self.define_a_zerolength(bulge)
            bd[0] += 1
            bd[1] -= 1

        if s1d[0] - bd[1] == 1:
            return 0, 1
        if bd[0] - s1d[1] == 1:
            return 1, 0
        if s1d[2] - bd[1] == 1:
            return 2, 1
        if bd[0] - s1d[3] == 1:
            return 3, 0

        raise ValueError('Wrong element')

    def define_a_zerolength(self, elem):
        if self.rna_elements[elem] != []:
            raise ValueError('{} does not have zero length'.format(elem))
        edges = self.edges[elem]
        # hairpin
        if len(edges) == 1:
            stem, = edges
            define = self.rna_elements[stem]
            if define[2] == define[1] + 1:
                return [define[1], define[2]]
        # here are 2 adjacent elements
        if len(edges) == 2:
            stem1, stem2 = edges
            connections = self.edges[stem1] & self.edges[stem2]
            zl_connections = []
            for conn in connections:
                if self.rna_elements[conn] == []:
                    zl_connections.append(conn)
            assert elem in zl_connections
            zl_connections.sort()
            zl_coordinates = set()
            for k, l in itertools.product(range(4), repeat=2):
                if abs(self.rna_elements[stem1][k] - self.rna_elements[stem2][l]) == 1:
                    d = [self.rna_elements[stem1][k], self.rna_elements[stem2][l]]
                    d.sort()
                    zl_coordinates.add(tuple(d))
            zl_coordinates = list(zl_coordinates)
            zl_coordinates.sort()
            i = zl_connections.index(elem)
            return list(zl_coordinates[i])
        raise Exception("wrong")


class GraphConstruction(BaseGraph):
    def __init__(self, tuples):
        super().__init__()
        self.rna_elements = {}
        self.edges = defaultdict(set)
        self.weights = {}
        self._name_counter = 0
        self.from_tuples(tuples)

    def from_tuples(self, tuples):
        stems = list()
        bulges = list()
        tuples.sort()
        tuples = iter(tuples)
        (t1, t2) = next(tuples)

        prev_from = t1
        prev_to = t2
        start_from = prev_from
        start_to = prev_to
        last_paired = prev_from

        for t1, t2 in tuples:
            (from_bp, to_bp) = (t1, t2)
            if abs(to_bp - prev_to) == 1 and prev_to != 0:
                # stem
                if (((prev_to - prev_from > 0 and to_bp - from_bp > 0) or
                     (prev_to - prev_from < 0 and to_bp - from_bp < 0)) and
                        (to_bp - prev_to) == -(from_bp - prev_from)):
                    (prev_from, prev_to) = (from_bp, to_bp)
                    last_paired = from_bp
                    continue

            if to_bp == 0 and prev_to == 0:
                (prev_from, prev_to) = (from_bp, to_bp)
                continue
            else:
                if prev_to != 0:
                    new_stem = tuple(sorted([tuple(sorted([start_from - 1, start_to - 1])),
                                             tuple(sorted([prev_from - 1, prev_to - 1]))]))
                    if new_stem not in stems:
                        stems += [new_stem]
                    last_paired = from_bp
                    start_from = from_bp
                    start_to = to_bp
                else:
                    new_bulge = ((last_paired - 1, prev_from - 1))
                    bulges += [new_bulge]
                    start_from = from_bp
                    start_to = to_bp

            prev_from = from_bp
            prev_to = to_bp

        if prev_to != 0:
            new_stem = tuple(sorted([tuple(sorted([start_from - 1, start_to - 1])),
                                     tuple(sorted([prev_from - 1, prev_to - 1]))]))
            if new_stem not in stems:
                stems += [new_stem]
        if prev_to == 0:
            new_bulge = ((last_paired - 1, prev_from - 1))
            bulges += [new_bulge]
        self.from_stems_and_bulges(stems, bulges)

    def from_stems_and_bulges(self, stems, bulges):
        len_bulges = len(bulges)
        len_stems = len(stems)
        for i in range(len_stems):
            ss1 = stems[i][0][0] + 1
            ss2 = stems[i][0][1] + 1
            se1 = stems[i][1][0] + 1
            se2 = stems[i][1][1] + 1

            self.rna_elements['y{}'.format(i)] = [min(ss1, se1), max(ss1, se1),
                                         min(ss2, se2), max(ss2, se2)]
            self.weights['y{}'.format(i)] = 1
        for i in range(len_bulges):
            bulge = bulges[i]
            self.rna_elements['b{}'.format(i)] = sorted([bulge[0] + 1, bulge[1] + 1])
            self.weights['b{}'.format(i)] = 1
        for i in range(len_stems):
            stem = stems[i]
            for j in range(len(bulges)):
                bulge = bulges[j]
                for stem_part in stem:
                    for part in stem_part:
                        for bulge_part in bulge:
                            if abs(bulge_part - part) == 1:
                                self.edges['y{}'.format(i)].add('b{}'.format(j))
                                self.edges['b{}'.format(j)].add('y{}'.format(i))

        for i, j in itertools.combinations(range(len_stems), 2):
            for k1, k2, l1, l2 in itertools.product(range(2), repeat=4):
                s1 = stems[i][k1][l1]
                s2 = stems[j][k2][l2]
                if k1 == 1 and stems[i][0][l1] == stems[i][1][l1]:
                    continue
                if k2 == 1 and stems[j][0][l2] == stems[j][1][l2]:
                    continue
                if abs(s1 - s2) == 1:
                    bn = 'b{}'.format(len_bulges)
                    self.rna_elements[bn] = []
                    self.weights[bn] = 1

                    self.edges['y{}'.format(i)].add(bn)
                    self.edges[bn].add('y{}'.format(i))

                    self.edges['y{}'.format(j)].add(bn)
                    self.edges[bn].add('y{}'.format(j))
                    len_bulges += 1

        for d in list(self.rna_elements.keys()):
            if d[0] != 'y':
                continue

            (s1, e1, s2, e2) = self.rna_elements[d]
            if abs(s2 - e1) == 1:
                bn = 'b{}'.format(len_bulges)
                self.rna_elements[bn] = []
                self.weights[bn] = 1
                self.edges[bn].add(d)
                self.edges[d].add(bn)
                len_bulges += 1
        new_vertex = True
        while new_vertex:
            new_vertex = False
            bulges = [k for k in self.rna_elements if k[0] != 'y']

            for (b1, b2) in itertools.combinations(bulges, r=2):
                if self.edges[b1] == self.edges[b2] and len(self.edges[b1]) == 2:
                    connections = self.connections(b1)

                    all_connections = [sorted((self.get_sides(connections[0], b1)[0],
                                               self.get_sides(connections[0], b2)[0])),
                                       sorted((self.get_sides(connections[1], b1)[0],
                                               self.get_sides(connections[1], b2)[0]))]

                    if all_connections == [[1, 2], [0, 3]]:
                        # interior loop
                        self.merge_vertices([b1, b2])
                        new_vertex = True
                        break
        self.sort_rna_elements()
        self.nucleotide_labels()
        to_remove = []
        for d in self.rna_elements:
            if d[0] == 'h' and len(self.rna_elements[d]) == 0:
                to_remove += [d]
        for r in to_remove:
            remove_vertex(self, r)

    def sort_rna_elements(self):
        for k in self.rna_elements.keys():
            d = self.rna_elements[k]
            if len(d) == 4:
                if d[0] > d[2]:
                    new_d = [d[2], d[3], d[0], d[1]]
                    self.rna_elements[k] = new_d

    def merge_vertices(self, vertices):
        new_vertex = 'x{}'.format(self._name_counter)
        self._name_counter += 1
        self.weights[new_vertex] = 0
        connections = set()

        for v in vertices:
            for item in self.edges[v]:
                connections.add(item)
            if v[0] == 's':
                self.rna_elements[new_vertex] = self.rna_elements.get(new_vertex, []) + \
                                                [self.rna_elements[v][0], self.rna_elements[v][2]] + \
                                                [self.rna_elements[v][1], self.rna_elements[v][3]]
            else:
                self.rna_elements[new_vertex] = self.rna_elements.get(
                    new_vertex, []) + self.rna_elements[v]
            self.weights[new_vertex] += 1
            remove_vertex(self, v)
            for key in self.rna_elements.keys():
                if key[0] != 's':
                    assert (len(self.rna_elements[key]) % 2 == 0)
                    new_j = 0

                    while new_j < len(self.rna_elements[key]):
                        j = new_j
                        new_j += j + 2
                        (f1, t1) = (int(self.rna_elements[key][j]), int(
                            self.rna_elements[key][j + 1]))
                        if f1 == -1 and t1 == -2:
                            del self.rna_elements[key][j]
                            del self.rna_elements[key][j]
                            new_j = 0
                            continue

                        for k in range(j + 2, len(self.rna_elements[key]), 2):
                            if key[0] == 'y':
                                continue

                            (f2, t2) = (int(self.rna_elements[key][k]), int(
                                self.rna_elements[key][k + 1]))

                            if t2 + 1 != f1 and t1 + 1 != f2:
                                continue

                            if t2 + 1 == f1:
                                self.rna_elements[key][j] = str(f2)
                                self.rna_elements[key][j + 1] = str(t1)
                            elif t1 + 1 == f2:
                                self.rna_elements[key][j] = str(f1)
                                self.rna_elements[key][j + 1] = str(t2)
                            del self.rna_elements[key][k]
                            del self.rna_elements[key][k]
                            new_j = 0; break

        for connection in connections:
            self.edges[new_vertex].add(connection)
            self.edges[connection].add(new_vertex)
        return new_vertex

    def nucleotide_labels(self):
        stem = []
        interior_loop = []
        multiloop = []
        hairpin = []
        five = []
        three = []
        seq_length = 0
        for d in self.rna_elements:
            for r in self.define_range_iterator(d):
                seq_length += r[1] - r[0] + 1

        for d in self.rna_elements.keys():
            if d[0] == 'y' or d[0] == 's':
                stem += [d]
                continue

            if len(self.rna_elements[d]) == 0 and len(self.edges[d]) == 1:
                hairpin += [d]
                continue

            if len(self.rna_elements[d]) == 0 and len(self.edges[d]) == 2:
                multiloop += [d]
                continue

            if len(self.edges[d]) <= 1 and self.rna_elements[d][0] == 1:
                five += [d]
                continue

            if len(self.edges[d]) == 1 and self.rna_elements[d][1] == seq_length:
                three += [d]
                continue

            if (len(self.edges[d]) == 1 and
                self.rna_elements[d][0] != 1 and
                    self.rna_elements[d][1] != seq_length):
                hairpin += [d]
                continue

            if d[0] == 'm' or (d[0] != 'i' and len(self.edges[d]) == 2 and
                                       self.weights[d] == 1 and
                                       self.rna_elements[d][0] != 1 and
                                       self.rna_elements[d][1] != seq_length):
                multiloop += [d]
                continue

            if d[0] == 'i' or self.weights[d] == 2:
                interior_loop += [d]

        stem.sort(key=self.compare_stems)
        hairpin.sort(key=self.compare_hairpins)
        multiloop.sort(key=self.compare_bulges)
        interior_loop.sort(key=self.compare_stems)

        if five:
            d, = five
            nucleotide_lable(self, d, 'n0')
        if three:
            d, = three
            nucleotide_lable(self, d, 'n0')
        for i, d in enumerate(stem):
            nucleotide_lable(self, d, 's{}'.format(i))
        for i, d in enumerate(interior_loop):
            nucleotide_lable(self, d, 'i{}'.format(i))
        for i, d in enumerate(multiloop):
            nucleotide_lable(self, d, 'j{}'.format(i))
        for i, d in enumerate(hairpin):
            nucleotide_lable(self, d, 'h{}'.format(i))

    def compare_stems(self, b):
        return self.rna_elements[b][0], 0

    def compare_bulges(self, b):
        return self.define(b)

    def compare_hairpins(self, b):
        connections = self.connections(b)
        return self.rna_elements[connections[0]][1], sys.maxsize


def remove_vertex(bg, v):
    for key in bg.edges[v]:
        bg.edges[key].remove(v)
    for edge in bg.edges:
        if v in bg.edges[edge]:
            bg.edges[edge].remove(v)
    del bg.edges[v]
    del bg.rna_elements[v]


def nucleotide_lable(bg, old_name, new_name):
    define = bg.rna_elements[old_name]
    del bg.rna_elements[old_name]
    bg.rna_elements[new_name] = define
    edge = bg.edges[old_name]
    del bg.edges[old_name]
    bg.edges[new_name] = edge
    for k in bg.edges.keys():
        new_edges = set()
        for e in bg.edges[k]:
            if e == old_name:
                new_edges.add(new_name)
            else:
                new_edges.add(e)
        bg.edges[k] = new_edges


class Graph(BaseGraph):
    def __init__(self, graph_construction, len_rna):
        super().__init__()
        self.rna_elements = dict(graph_construction.rna_elements)
        self.len_rna = len_rna

    @staticmethod
    def from_init_seq(dotbracket_str):
        table = common.dotbracket_to_pairtable(dotbracket_str)
        pt = iter(table)
        next(pt)
        tuples = []
        for i, p in enumerate(pt):
            tuples += [(i + 1, p)]
        graph = Graph(GraphConstruction(tuples), len(dotbracket_str))
        return graph

    def get_stems_coordinates(self):
        only_stem_coordinates = {'stems': []}
        for elem in self.rna_elements.keys():
            if elem[0] == 's':
                plain_stem = list(map(lambda x: x - 1, self.rna_elements[elem]))
                new_stem = [(plain_stem[0], plain_stem[1] + 1), (plain_stem[2], plain_stem[3] + 1)]
                only_stem_coordinates['stems'].append(new_stem)
        return only_stem_coordinates

    def get_elements(self):
        print("RNA elements:", self.rna_elements)
        strg = [' '] * (self.len_rna + 1)
        levels = strg.copy()
        for elem in self.rna_elements.keys():
            for visited in self.visited_iterator(elem):
                levels[visited] = elem[-1]
                strg[visited] = elem[0]
        return strg, levels, self.rna_elements

    def visited_iterator(self, node):
        visited = set()
        for r in self.define_range_iterator(node):
            for i in range(r[0], r[1] + 1):
                if i not in visited:
                    visited.add(i)
                    yield i
