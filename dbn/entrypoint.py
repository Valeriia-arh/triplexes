import argparse
import itertools

from create_features import features
from graph.graph import Graph
from parse_sequence import Parser


class RNA(Graph):
    def __init__(self, graph_construction, sequence):
        super().__init__(graph_construction, sequence)


parser = argparse.ArgumentParser(description='Description of arguments')
parser.add_argument('-r','--rna', help='File with RNA and bracket sequence', required=True)
parser.add_argument('-t','--triplexes', help='File with triplexes', required=False)
args = vars(parser.parse_args())


if __name__ == '__main__':
    seq = open(args['rna'], 'r')
    rna = seq.readline()
    seq = seq.readline()
    print("RNA: ", rna)
    print("Bracket sequence: ", seq)
    if args['triplexes']:
        pass
    len_rna = len(seq)

    parsing = Parser(0)
    classification = parsing.preprocess_and_parse(seq)
    print(classification)

    loops_coordinates = parsing.loops_type1
    print("Loops coordinates", loops_coordinates)

    parsing2 = Parser(1)
    classification2 = parsing2.preprocess_and_parse(seq)
    print(classification2)

    go = RNA.from_init_seq(seq)
    stems_coordinates = Graph.get_stems_coordinates(go)

    all_elements = {**loops_coordinates, **stems_coordinates}
    print("Elements", all_elements)

    rna_triplexes = []
    for i in range(len(rna)):
        rna_triplexes.append(i)
    combinations = list(itertools.combinations(rna_triplexes, 3))

    features(rna, classification, classification2, combinations, all_elements)
