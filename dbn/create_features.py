import pandas as pd

from common import get_element, search_element

feature_headers = ['same12', 'local12', 'longrange12', 'same23', 'local23', 'longrange23', 'same13', 'local13',
                   'longrange13', 'a1m5', 'c1m5', 'g1m5', 'u1m5', 's1m5', 'h1m5', 'b1m5', 'i1m5', 'j1m5', 'lc1m5',
                   'li1m5', 'lp1m5', 'fl1m5', 'fed1m5', 'a1m4', 'c1m4', 'g1m4', 'u1m4', 's1m4', 'h1m4', 'b1m4', 'i1m4',
 'j1m4', 'lc1m4', 'li1m4', 'lp1m4', 'fl1m4', 'fed1m4', 'a1m3', 'c1m3', 'g1m3', 'u1m3', 's1m3', 'h1m3', 'b1m3',
 'i1m3', 'j1m3', 'lc1m3', 'li1m3', 'lp1m3', 'fl1m3', 'fed1m3', 'a1m2', 'c1m2', 'g1m2', 'u1m2', 's1m2', 'h1m2', 'b1m2',
 'i1m2', 'j1m2', 'lc1m2', 'li1m2', 'lp1m2', 'fl1m2', 'fed1m2', 'a1m1', 'c1m1', 'g1m1', 'u1m1', 's1m1', 'h1m1', 'b1m1',
 'i1m1', 'j1m1', 'lc1m1', 'li1m1', 'lp1m1', 'fl1m1', 'fed1m1', 'a1', 'c1', 'g1', 'u1', 's1', 'h1', 'b1', 'i1', 'j1', 
 'lc1', 'li1', 'lp1', 'fl1', 'fed1', 'a1p1', 'c1p1', 'g1p1', 'u1p1', 's1p1', 'h1p1', 'b1p1', 'i1p1', 'j1p1', 'lc1p1', 
 'li1p1', 'lp1p1', 'fl1p1', 'fed1p1', 'a1p2', 'c1p2', 'g1p2', 'u1p2', 's1p2', 'h1p2', 'b1p2', 'i1p2', 'j1p2', 'lc1p2', 
 'li1p2', 'lp1p2', 'fl1p2', 'fed1p2', 'a1p3', 'c1p3', 'g1p3', 'u1p3', 's1p3', 'h1p3', 'b1p3', 'i1p3', 'j1p3', 'lc1p3', 
 'li1p3', 'lp1p3', 'fl1p3', 'fed1p3', 'a1p4', 'c1p4', 'g1p4', 'u1p4', 's1p4', 'h1p4', 'b1p4', 'i1p4', 'j1p4', 'lc1p4', 
 'li1p4', 'lp1p4', 'fl1p4', 'fed1p4', 'a1p5', 'c1p5', 'g1p5', 'u1p5', 's1p5', 'h1p5', 'b1p5', 'i1p5', 'j1p5', 'lc1p5', 
 'li1p5', 'lp1p5', 'fl1p5', 'fed1p5', 'a2m5', 'c2m5', 'g2m5', 'u2m5', 's2m5', 'h2m5', 'b2m5', 'i2m5', 'j2m5', 'lc2m5', 
 'li2m5', 'lp2m5', 'fl2m5', 'fed2m5', 'a2m4', 'c2m4', 'g2m4', 'u2m4', 's2m4', 'h2m4', 'b2m4', 'i2m4', 'j2m4', 'lc2m4', 
 'li2m4', 'lp2m4', 'fl2m4', 'fed2m4', 'a2m3', 'c2m3', 'g2m3','u2m3', 's2m3', 'h2m3', 'b2m3', 'i2m3', 'j2m3', 'lc2m3', 
 'li2m3', 'lp2m3', 'fl2m3', 'fed2m3', 'a2m2', 'c2m2', 'g2m2', 'u2m2', 's2m2', 'h2m2', 'b2m2', 'i2m2', 'j2m2', 'lc2m2', 
 'li2m2', 'lp2m2', 'fl2m2', 'fed2m2', 'a2m1', 'c2m1', 'g2m1', 'u2m1', 's2m1', 'h2m1', 'b2m1', 'i2m1', 'j2m1', 'lc2m1',
 'li2m1', 'lp2m1', 'fl2m1', 'fed2m1', 'a2', 'c2', 'g2', 'u2', 's2', 'h2', 'b2', 'i2', 'j2', 'lc2', 'li2', 'lp2', 'fl2',
 'fed2', 'a2p1', 'c2p1', 'g2p1', 'u2p1', 's2p1', 'h2p1', 'b2p1', 'i2p1', 'j2p1', 'lc2p1', 'li2p1', 'lp2p1', 'fl2p1',
 'fed2p1', 'a2p2', 'c2p2', 'g2p2', 'u2p2', 's2p2', 'h2p2', 'b2p2', 'i2p2', 'j2p2', 'lc2p2', 'li2p2', 'lp2p2', 'fl2p2',
 'fed2p2', 'a2p3', 'c2p3', 'g2p3', 'u2p3', 's2p3', 'h2p3', 'b2p3', 'i2p3', 'j2p3', 'lc2p3', 'li2p3', 'lp2p3', 'fl2p3', 
 'fed2p3', 'a2p4', 'c2p4', 'g2p4', 'u2p4', 's2p4', 'h2p4', 'b2p4', 'i2p4', 'j2p4', 'lc2p4', 'li2p4', 'lp2p4', 'fl2p4', 
 'fed2p4', 'a2p5', 'c2p5', 'g2p5', 'u2p5', 's2p5', 'h2p5', 'b2p5', 'i2p5', 'j2p5', 'lc2p5', 'li2p5', 'lp2p5', 'fl2p5', 
 'fed2p5', 'a3m5', 'c3m5', 'g3m5', 'u3m5', 's3m5', 'h3m5', 'b3m5', 'i3m5', 'j3m5', 'lc3m5', 'li3m5', 'lp3m5', 'fl3m5', 
 'fed3m5', 'a3m4', 'c3m4', 'g3m4', 'u3m4', 's3m4', 'h3m4', 'b3m4', 'i3m4', 'j3m4', 'lc3m4', 'li3m4', 'lp3m4', 'fl3m4', 
 'fed3m4', 'a3m3', 'c3m3', 'g3m3', 'u3m3', 's3m3', 'h3m3', 'b3m3', 'i3m3', 'j3m3', 'lc3m3', 'li3m3', 'lp3m3', 'fl3m3', 
 'fed3m3', 'a3m2', 'c3m2', 'g3m2', 'u3m2', 's3m2', 'h3m2', 'b3m2', 'i3m2', 'j3m2', 'lc3m2', 'li3m2','lp3m2', 'fl3m2', 
 'fed3m2', 'a3m1', 'c3m1', 'g3m1', 'u3m1', 's3m1', 'h3m1', 'b3m1', 'i3m1', 'j3m1', 'lc3m1', 'li3m1', 'lp3m1', 'fl3m1', 
 'fed3m1', 'a3', 'c3', 'g3', 'u3', 's3', 'h3', 'b3', 'i3', 'j3', 'lc3', 'li3', 'lp3', 'fl3', 'fed3', 'a3p1', 'c3p1', 
 'g3p1', 'u3p1', 's3p1', 'h3p1', 'b3p1', 'i3p1', 'j3p1', 'lc3p1', 'li3p1', 'lp3p1', 'fl3p1', 'fed3p1', 'a3p2', 'c3p2', 
 'g3p2', 'u3p2', 's3p2', 'h3p2', 'b3p2', 'i3p2', 'j3p2', 'lc3p2', 'li3p2', 'lp3p2', 'fl3p2', 'fed3p2', 'a3p3', 'c3p3', 
 'g3p3', 'u3p3', 's3p3', 'h3p3', 'b3p3', 'i3p3', 'j3p3', 'lc3p3', 'li3p3', 'lp3p3', 'fl3p3', 'fed3p3', 'a3p4', 'c3p4', 
 'g3p4', 'u3p4', 's3p4', 'h3p4', 'b3p4', 'i3p4', 'j3p4', 'lc3p4', 'li3p4', 'lp3p4', 'fl3p4', 'fed3p4', 'a3p5', 'c3p5',
 'g3p5', 'u3p5', 's3p5', 'h3p5', 'b3p5', 'i3p5', 'j3p5', 'lc3p5', 'li3p5', 'lp3p5', 'fl3p5', 'fed3p5']


def features(rna, elements, loop_types, combinations, all_elements):
    feature_table = pd.DataFrame(columns=feature_headers)

    for i in range(10):
        same12, same23, same13, local12, local23, local13, longrange12, longrange23, longrange13 = \
            search_element(all_elements, combinations[i])

        a1m5 = 1 if (combinations[i][0] - 5 >= 0 and rna[combinations[i][0] - 5] == 'A') else 0
        c1m5 = 1 if (combinations[i][0] - 5 >= 0 and rna[combinations[i][0] - 5] == 'C') else 0
        g1m5 = 1 if (combinations[i][0] - 5 >= 0 and rna[combinations[i][0] - 5] == 'G') else 0
        u1m5 = 1 if (combinations[i][0] - 5 >= 0 and rna[combinations[i][0] - 5] == 'U') else 0

        a2m5 = 1 if (combinations[i][1] - 5 >= 0 and rna[combinations[i][1] - 5] == 'A') else 0
        c2m5 = 1 if (combinations[i][1] - 5 >= 0 and rna[combinations[i][1] - 5] == 'C') else 0
        g2m5 = 1 if (combinations[i][1] - 5 >= 0 and rna[combinations[i][1] - 5] == 'G') else 0
        u2m5 = 1 if (combinations[i][1] - 5 >= 0 and rna[combinations[i][1] - 5] == 'U') else 0

        a3m5 = 1 if (combinations[i][2] - 5 >= 0 and rna[combinations[i][2] - 5] == 'A') else 0
        c3m5 = 1 if (combinations[i][2] - 5 >= 0 and rna[combinations[i][2] - 5] == 'C') else 0
        g3m5 = 1 if (combinations[i][2] - 5 >= 0 and rna[combinations[i][2] - 5] == 'G') else 0
        u3m5 = 1 if (combinations[i][2] - 5 >= 0 and rna[combinations[i][2] - 5] == 'U') else 0

        a1m4 = 1 if (combinations[i][0] - 4 >= 0 and rna[combinations[i][0] - 4] == 'A') else 0
        c1m4 = 1 if (combinations[i][0] - 4 >= 0 and rna[combinations[i][0] - 4] == 'C') else 0
        g1m4 = 1 if (combinations[i][0] - 4 >= 0 and rna[combinations[i][0] - 4] == 'G') else 0
        u1m4 = 1 if (combinations[i][0] - 4 >= 0 and rna[combinations[i][0] - 4] == 'U') else 0

        a2m4 = 1 if (combinations[i][1] - 4 >= 0 and rna[combinations[i][1] - 4] == 'A') else 0
        c2m4 = 1 if (combinations[i][1] - 4 >= 0 and rna[combinations[i][1] - 4] == 'C') else 0
        g2m4 = 1 if (combinations[i][1] - 4 >= 0 and rna[combinations[i][1] - 4] == 'G') else 0
        u2m4 = 1 if (combinations[i][1] - 4 >= 0 and rna[combinations[i][1] - 4] == 'U') else 0

        a3m4 = 1 if (combinations[i][2] - 4 >= 0 and rna[combinations[i][2] - 4] == 'A') else 0
        c3m4 = 1 if (combinations[i][2] - 4 >= 0 and rna[combinations[i][2] - 4] == 'C') else 0
        g3m4 = 1 if (combinations[i][2] - 4 >= 0 and rna[combinations[i][2] - 4] == 'G') else 0
        u3m4 = 1 if (combinations[i][2] - 4 >= 0 and rna[combinations[i][2] - 4] == 'U') else 0

        a1m3 = 1 if (combinations[i][0] - 3 >= 0 and rna[combinations[i][0] - 3] == 'A') else 0
        c1m3 = 1 if (combinations[i][0] - 3 >= 0 and rna[combinations[i][0] - 3] == 'C') else 0
        g1m3 = 1 if (combinations[i][0] - 3 >= 0 and rna[combinations[i][0] - 3] == 'G') else 0
        u1m3 = 1 if (combinations[i][0] - 3 >= 0 and rna[combinations[i][0] - 3] == 'U') else 0

        a2m3 = 1 if (combinations[i][1] - 3 >= 0 and rna[combinations[i][1] - 3] == 'A') else 0
        c2m3 = 1 if (combinations[i][1] - 3 >= 0 and rna[combinations[i][1] - 3] == 'C') else 0
        g2m3 = 1 if (combinations[i][1] - 3 >= 0 and rna[combinations[i][1] - 3] == 'G') else 0
        u2m3 = 1 if (combinations[i][1] - 3 >= 0 and rna[combinations[i][1] - 3] == 'U') else 0

        a3m3 = 1 if (combinations[i][2] - 3 >= 0 and rna[combinations[i][2] - 3] == 'A') else 0
        c3m3 = 1 if (combinations[i][2] - 3 >= 0 and rna[combinations[i][2] - 3] == 'C') else 0
        g3m3 = 1 if (combinations[i][2] - 3 >= 0 and rna[combinations[i][2] - 3] == 'G') else 0
        u3m3 = 1 if (combinations[i][2] - 3 >= 0 and rna[combinations[i][2] - 3] == 'U') else 0

        a1m2 = 1 if (combinations[i][0] - 2 >= 0 and rna[combinations[i][0] - 2] == 'A') else 0
        c1m2 = 1 if (combinations[i][0] - 2 >= 0 and rna[combinations[i][0] - 2] == 'C') else 0
        g1m2 = 1 if (combinations[i][0] - 2 >= 0 and rna[combinations[i][0] - 2] == 'G') else 0
        u1m2 = 1 if (combinations[i][0] - 2 >= 0 and rna[combinations[i][0] - 2] == 'U') else 0

        a2m2 = 1 if (combinations[i][1] - 2 >= 0 and rna[combinations[i][1] - 2] == 'A') else 0
        c2m2 = 1 if (combinations[i][1] - 2 >= 0 and rna[combinations[i][1] - 2] == 'C') else 0
        g2m2 = 1 if (combinations[i][1] - 2 >= 0 and rna[combinations[i][1] - 2] == 'G') else 0
        u2m2 = 1 if (combinations[i][1] - 2 >= 0 and rna[combinations[i][1] - 2] == 'U') else 0

        a3m2 = 1 if (combinations[i][2] - 2 >= 0 and rna[combinations[i][2] - 2] == 'A') else 0
        c3m2 = 1 if (combinations[i][2] - 2 >= 0 and rna[combinations[i][2] - 2] == 'C') else 0
        g3m2 = 1 if (combinations[i][2] - 2 >= 0 and rna[combinations[i][2] - 2] == 'G') else 0
        u3m2 = 1 if (combinations[i][2] - 2 >= 0 and rna[combinations[i][2] - 2] == 'U') else 0

        a1m1 = 1 if (combinations[i][0] - 1 >= 0 and rna[combinations[i][0] - 1] == 'A') else 0
        c1m1 = 1 if (combinations[i][0] - 1 >= 0 and rna[combinations[i][0] - 1] == 'C') else 0
        g1m1 = 1 if (combinations[i][0] - 1 >= 0 and rna[combinations[i][0] - 1] == 'G') else 0
        u1m1 = 1 if (combinations[i][0] - 1 >= 0 and rna[combinations[i][0] - 1] == 'U') else 0

        a2m1 = 1 if (combinations[i][1] - 1 >= 0 and rna[combinations[i][1] - 1] == 'A') else 0
        c2m1 = 1 if (combinations[i][1] - 1 >= 0 and rna[combinations[i][1] - 1] == 'C') else 0
        g2m1 = 1 if (combinations[i][1] - 1 >= 0 and rna[combinations[i][1] - 1] == 'G') else 0
        u2m1 = 1 if (combinations[i][1] - 1 >= 0 and rna[combinations[i][1] - 1] == 'U') else 0

        a3m1 = 1 if (combinations[i][2] - 1 >= 0 and rna[combinations[i][2] - 1] == 'A') else 0
        c3m1 = 1 if (combinations[i][2] - 1 >= 0 and rna[combinations[i][2] - 1] == 'C') else 0
        g3m1 = 1 if (combinations[i][2] - 1 >= 0 and rna[combinations[i][2] - 1] == 'G') else 0
        u3m1 = 1 if (combinations[i][2] - 1 >= 0 and rna[combinations[i][2] - 1] == 'U') else 0

        a1p1 = 1 if (combinations[i][0] + 1 <= len(rna) - 1 and rna[combinations[i][0] + 1] == 'A') else 0
        c1p1 = 1 if (combinations[i][0] + 1 <= len(rna) - 1 and rna[combinations[i][0] + 1] == 'C') else 0
        g1p1 = 1 if (combinations[i][0] + 1 <= len(rna) - 1 and rna[combinations[i][0] + 1] == 'G') else 0
        u1p1 = 1 if (combinations[i][0] + 1 <= len(rna) - 1 and rna[combinations[i][0] + 1] == 'U') else 0

        a2p1 = 1 if (combinations[i][1] + 1 <= len(rna) - 1 and rna[combinations[i][1] + 1] == 'A') else 0
        c2p1 = 1 if (combinations[i][1] + 1 <= len(rna) - 1 and rna[combinations[i][1] + 1] == 'C') else 0
        g2p1 = 1 if (combinations[i][1] + 1 <= len(rna) - 1 and rna[combinations[i][1] + 1] == 'G') else 0
        u2p1 = 1 if (combinations[i][1] + 1 <= len(rna) - 1 and rna[combinations[i][1] + 1] == 'U') else 0

        a3p1 = 1 if (combinations[i][2] + 1 <= len(rna) - 1 and rna[combinations[i][2] + 1] == 'A') else 0
        c3p1 = 1 if (combinations[i][2] + 1 <= len(rna) - 1 and rna[combinations[i][2] + 1] == 'C') else 0
        g3p1 = 1 if (combinations[i][2] + 1 <= len(rna) - 1 and rna[combinations[i][2] + 1] == 'G') else 0
        u3p1 = 1 if (combinations[i][2] + 1 <= len(rna) - 1 and rna[combinations[i][2] + 1] == 'U') else 0

        a1p2 = 1 if (combinations[i][0] + 2 <= len(rna) - 1 and rna[combinations[i][0] + 2] == 'A') else 0
        c1p2 = 1 if (combinations[i][0] + 2 <= len(rna) - 1 and rna[combinations[i][0] + 2] == 'C') else 0
        g1p2 = 1 if (combinations[i][0] + 2 <= len(rna) - 1 and rna[combinations[i][0] + 2] == 'G') else 0
        u1p2 = 1 if (combinations[i][0] + 2 <= len(rna) - 1 and rna[combinations[i][0] + 2] == 'U') else 0

        a2p2 = 1 if (combinations[i][1] + 2 <= len(rna) - 1 and rna[combinations[i][1] + 2] == 'A') else 0
        c2p2 = 1 if (combinations[i][1] + 2 <= len(rna) - 1 and rna[combinations[i][1] + 2] == 'C') else 0
        g2p2 = 1 if (combinations[i][1] + 2 <= len(rna) - 1 and rna[combinations[i][1] + 2] == 'G') else 0
        u2p2 = 1 if (combinations[i][1] + 2 <= len(rna) - 1 and rna[combinations[i][1] + 2] == 'U') else 0

        a3p2 = 1 if (combinations[i][2] + 2 <= len(rna) - 1 and rna[combinations[i][2] + 2] == 'A') else 0
        c3p2 = 1 if (combinations[i][2] + 2 <= len(rna) - 1 and rna[combinations[i][2] + 2] == 'C') else 0
        g3p2 = 1 if (combinations[i][2] + 2 <= len(rna) - 1 and rna[combinations[i][2] + 2] == 'G') else 0
        u3p2 = 1 if (combinations[i][2] + 2 <= len(rna) - 1 and rna[combinations[i][2] + 2] == 'U') else 0

        a1p3 = 1 if (combinations[i][0] + 3 <= len(rna) - 1 and rna[combinations[i][0] + 3] == 'A') else 0
        c1p3 = 1 if (combinations[i][0] + 3 <= len(rna) - 1 and rna[combinations[i][0] + 3] == 'C') else 0
        g1p3 = 1 if (combinations[i][0] + 3 <= len(rna) - 1 and rna[combinations[i][0] + 3] == 'G') else 0
        u1p3 = 1 if (combinations[i][0] + 3 <= len(rna) - 1 and rna[combinations[i][0] + 3] == 'U') else 0

        a2p3 = 1 if (combinations[i][1] + 3 <= len(rna) - 1 and rna[combinations[i][1] + 3] == 'A') else 0
        c2p3 = 1 if (combinations[i][1] + 3 <= len(rna) - 1 and rna[combinations[i][1] + 3] == 'C') else 0
        g2p3 = 1 if (combinations[i][1] + 3 <= len(rna) - 1 and rna[combinations[i][1] + 3] == 'G') else 0
        u2p3 = 1 if (combinations[i][1] + 3 <= len(rna) - 1 and rna[combinations[i][1] + 3] == 'U') else 0

        a3p3 = 1 if (combinations[i][2] + 3 <= len(rna) - 1 and rna[combinations[i][2] + 3] == 'A') else 0
        c3p3 = 1 if (combinations[i][2] + 3 <= len(rna) - 1 and rna[combinations[i][2] + 3] == 'C') else 0
        g3p3 = 1 if (combinations[i][2] + 3 <= len(rna) - 1 and rna[combinations[i][2] + 3] == 'G') else 0
        u3p3 = 1 if (combinations[i][2] + 3 <= len(rna) - 1 and rna[combinations[i][2] + 3] == 'U') else 0

        a1p4 = 1 if (combinations[i][0] + 4 <= len(rna) - 1 and rna[combinations[i][0] + 4] == 'A') else 0
        c1p4 = 1 if (combinations[i][0] + 4 <= len(rna) - 1 and rna[combinations[i][0] + 4] == 'C') else 0
        g1p4 = 1 if (combinations[i][0] + 4 <= len(rna) - 1 and rna[combinations[i][0] + 4] == 'G') else 0
        u1p4 = 1 if (combinations[i][0] + 4 <= len(rna) - 1 and rna[combinations[i][0] + 4] == 'U') else 0

        a2p4 = 1 if (combinations[i][1] + 4 <= len(rna) - 1 and rna[combinations[i][1] + 4] == 'A') else 0
        c2p4 = 1 if (combinations[i][1] + 4 <= len(rna) - 1 and rna[combinations[i][1] + 4] == 'C') else 0
        g2p4 = 1 if (combinations[i][1] + 4 <= len(rna) - 1 and rna[combinations[i][1] + 4] == 'G') else 0
        u2p4 = 1 if (combinations[i][1] + 4 <= len(rna) - 1 and rna[combinations[i][1] + 4] == 'U') else 0

        a3p4 = 1 if (combinations[i][2] + 4 <= len(rna) - 1 and rna[combinations[i][2] + 4] == 'A') else 0
        c3p4 = 1 if (combinations[i][2] + 4 <= len(rna) - 1 and rna[combinations[i][2] + 4] == 'C') else 0
        g3p4 = 1 if (combinations[i][2] + 4 <= len(rna) - 1 and rna[combinations[i][2] + 4] == 'G') else 0
        u3p4 = 1 if (combinations[i][2] + 4 <= len(rna) - 1 and rna[combinations[i][2] + 4] == 'U') else 0

        a1p5 = 1 if (combinations[i][0] + 5 <= len(rna) - 1 and rna[combinations[i][0] + 5] == 'A') else 0
        c1p5 = 1 if (combinations[i][0] + 5 <= len(rna) - 1 and rna[combinations[i][0] + 5] == 'C') else 0
        g1p5 = 1 if (combinations[i][0] + 5 <= len(rna) - 1 and rna[combinations[i][0] + 5] == 'G') else 0
        u1p5 = 1 if (combinations[i][0] + 5 <= len(rna) - 1 and rna[combinations[i][0] + 5] == 'U') else 0

        a2p5 = 1 if (combinations[i][1] + 5 <= len(rna) - 1 and rna[combinations[i][1] + 5] == 'A') else 0
        c2p5 = 1 if (combinations[i][1] + 5 <= len(rna) - 1 and rna[combinations[i][1] + 5] == 'C') else 0
        g2p5 = 1 if (combinations[i][1] + 5 <= len(rna) - 1 and rna[combinations[i][1] + 5] == 'G') else 0
        u2p5 = 1 if (combinations[i][1] + 5 <= len(rna) - 1 and rna[combinations[i][1] + 5] == 'U') else 0

        a3p5 = 1 if (combinations[i][2] + 5 <= len(rna) - 1 and rna[combinations[i][2] + 5] == 'A') else 0
        c3p5 = 1 if (combinations[i][2] + 5 <= len(rna) - 1 and rna[combinations[i][2] + 5] == 'C') else 0
        g3p5 = 1 if (combinations[i][2] + 5 <= len(rna) - 1 and rna[combinations[i][2] + 5] == 'G') else 0
        u3p5 = 1 if (combinations[i][2] + 5 <= len(rna) - 1 and rna[combinations[i][2] + 5] == 'U') else 0

        a1 = 1 if rna[combinations[i][0]] == 'A' else 0
        c1 = 1 if rna[combinations[i][0]] == 'C' else 0
        g1 = 1 if rna[combinations[i][0]] == 'G' else 0
        u1 = 1 if rna[combinations[i][0]] == 'U' else 0

        a2 = 1 if rna[combinations[i][1]] == 'A' else 0
        c2 = 1 if rna[combinations[i][1]] == 'C' else 0
        g2 = 1 if rna[combinations[i][1]] == 'G' else 0
        u2 = 1 if rna[combinations[i][1]] == 'U' else 0

        a3 = 1 if rna[combinations[i][2]] == 'A' else 0
        c3 = 1 if rna[combinations[i][2]] == 'C' else 0
        g3 = 1 if rna[combinations[i][2]] == 'G' else 0
        u3 = 1 if rna[combinations[i][2]] == 'U' else 0

        s1 = 1 if elements[combinations[i][0]] == 's' else 0
        s2 = 1 if elements[combinations[i][1]] == 's' else 0
        s3 = 1 if elements[combinations[i][2]] == 's' else 0

        h1 = 1 if elements[combinations[i][0]] == 'h' else 0
        h2 = 1 if elements[combinations[i][1]] == 'h' else 0
        h3 = 1 if elements[combinations[i][2]] == 'h' else 0

        i1 = 1 if elements[combinations[i][0]] == 'i' else 0
        i2 = 1 if elements[combinations[i][1]] == 'i' else 0
        i3 = 1 if elements[combinations[i][2]] == 'i' else 0

        j1 = 1 if elements[combinations[i][0]] == 'j' else 0
        j2 = 1 if elements[combinations[i][1]] == 'j' else 0
        j3 = 1 if elements[combinations[i][2]] == 'j' else 0

        b1 = 1 if elements[combinations[i][0]] == 'b' else 0
        b2 = 1 if elements[combinations[i][1]] == 'b' else 0
        b3 = 1 if elements[combinations[i][2]] == 'b' else 0

        lc1 = 1 if loop_types[combinations[i][0]] == 'c' else 0
        lc2 = 1 if loop_types[combinations[i][1]] == 'c' else 0
        lc3 = 1 if loop_types[combinations[i][2]] == 'c' else 0

        li1 = 1 if loop_types[combinations[i][0]] == 'i' else 0
        li2 = 1 if loop_types[combinations[i][1]] == 'i' else 0
        li3 = 1 if loop_types[combinations[i][2]] == 'i' else 0

        lp1 = 1 if loop_types[combinations[i][0]] == 'p' else 0
        lp2 = 1 if loop_types[combinations[i][1]] == 'p' else 0
        lp3 = 1 if loop_types[combinations[i][2]] == 'p' else 0

        s1m5 = 1 if (combinations[i][0] - 5 >= 0 and elements[combinations[i][0] - 5] == 's') else 0
        s2m5 = 1 if (combinations[i][1] - 5 >= 0 and elements[combinations[i][1] - 5] == 's') else 0
        s3m5 = 1 if (combinations[i][2] - 5 >= 0 and elements[combinations[i][2] - 5] == 's') else 0

        s1m4 = 1 if (combinations[i][0] - 4 >= 0 and elements[combinations[i][0] - 4] == 's') else 0
        s2m4 = 1 if (combinations[i][1] - 4 >= 0 and elements[combinations[i][1] - 4] == 's') else 0
        s3m4 = 1 if (combinations[i][2] - 4 >= 0 and elements[combinations[i][2] - 4] == 's') else 0

        s1m3 = 1 if (combinations[i][0] - 3 >= 0 and elements[combinations[i][0] - 3] == 's') else 0
        s2m3 = 1 if (combinations[i][1] - 3 >= 0 and elements[combinations[i][1] - 3] == 's') else 0
        s3m3 = 1 if (combinations[i][2] - 3 >= 0 and elements[combinations[i][2] - 3] == 's') else 0

        s1m2 = 1 if (combinations[i][0] - 2 >= 0 and elements[combinations[i][0] - 2] == 's') else 0
        s2m2 = 1 if (combinations[i][1] - 2 >= 0 and elements[combinations[i][1] - 2] == 's') else 0
        s3m2 = 1 if (combinations[i][2] - 2 >= 0 and elements[combinations[i][2] - 2] == 's') else 0

        s1m1 = 1 if (combinations[i][0] - 1 >= 0 and elements[combinations[i][0] - 1] == 's') else 0
        s2m1 = 1 if (combinations[i][1] - 1 >= 0 and elements[combinations[i][1] - 1] == 's') else 0
        s3m1 = 1 if (combinations[i][2] - 1 >= 0 and elements[combinations[i][2] - 1] == 's') else 0

        s1p1 = 1 if (combinations[i][0] + 1 <= len(elements) - 1 and elements[combinations[i][0] + 1] == 's') else 0
        s2p1 = 1 if (combinations[i][1] + 1 <= len(elements) - 1 and elements[combinations[i][1] + 1] == 's') else 0
        s3p1 = 1 if (combinations[i][2] + 1 <= len(elements) - 1 and elements[combinations[i][2] + 1] == 's') else 0

        s1p2 = 1 if (combinations[i][0] + 2 <= len(elements) - 1 and elements[combinations[i][0] + 2] == 's') else 0
        s2p2 = 1 if (combinations[i][1] + 2 <= len(elements) - 1 and elements[combinations[i][1] + 2] == 's') else 0
        s3p2 = 1 if (combinations[i][2] + 2 <= len(elements) - 1 and elements[combinations[i][2] + 2] == 's') else 0

        s1p3 = 1 if (combinations[i][0] + 3 <= len(elements) - 1 and elements[combinations[i][0] + 3] == 's') else 0
        s2p3 = 1 if (combinations[i][1] + 3 <= len(elements) - 1 and elements[combinations[i][1] + 3] == 's') else 0
        s3p3 = 1 if (combinations[i][2] + 3 <= len(elements) - 1 and elements[combinations[i][2] + 3] == 's') else 0

        s1p4 = 1 if (combinations[i][0] + 4 <= len(elements) - 1 and elements[combinations[i][0] + 4] == 's') else 0
        s2p4 = 1 if (combinations[i][1] + 4 <= len(elements) - 1 and elements[combinations[i][1] + 4] == 's') else 0
        s3p4 = 1 if (combinations[i][2] + 4 <= len(elements) - 1 and elements[combinations[i][2] + 4] == 's') else 0

        s1p5 = 1 if (combinations[i][0] + 5 <= len(elements) - 1 and elements[combinations[i][0] + 5] == 's') else 0
        s2p5 = 1 if (combinations[i][1] + 5 <= len(elements) - 1 and elements[combinations[i][1] + 5] == 's') else 0
        s3p5 = 1 if (combinations[i][2] + 5 <= len(elements) - 1 and elements[combinations[i][2] + 5] == 's') else 0

        h1m1 = 1 if (combinations[i][0] - 1 >= 0 and elements[combinations[i][0] - 1] == 'h') else 0
        h2m1 = 1 if (combinations[i][1] - 1 >= 0 and elements[combinations[i][1] - 1] == 'h') else 0
        h3m1 = 1 if (combinations[i][2] - 1 >= 0 and elements[combinations[i][2] - 1] == 'h') else 0

        h1m2 = 1 if (combinations[i][0] - 2 >= 0 and elements[combinations[i][0] - 2] == 'h') else 0
        h2m2 = 1 if (combinations[i][1] - 2 >= 0 and elements[combinations[i][1] - 2] == 'h') else 0
        h3m2 = 1 if (combinations[i][2] - 2 >= 0 and elements[combinations[i][2] - 2] == 'h') else 0

        h1m3 = 1 if (combinations[i][0] - 3 >= 0 and elements[combinations[i][0] - 3] == 'h') else 0
        h2m3 = 1 if (combinations[i][1] - 3 >= 0 and elements[combinations[i][1] - 3] == 'h') else 0
        h3m3 = 1 if (combinations[i][2] - 3 >= 0 and elements[combinations[i][2] - 3] == 'h') else 0

        h1m4 = 1 if (combinations[i][0] - 4 >= 0 and elements[combinations[i][0] - 4] == 'h') else 0
        h2m4 = 1 if (combinations[i][1] - 4 >= 0 and elements[combinations[i][1] - 4] == 'h') else 0
        h3m4 = 1 if (combinations[i][2] - 4 >= 0 and elements[combinations[i][2] - 4] == 'h') else 0

        h1m5 = 1 if (combinations[i][0] - 5 >= 0 and elements[combinations[i][0] - 5] == 'h') else 0
        h2m5 = 1 if (combinations[i][1] - 5 >= 0 and elements[combinations[i][1] - 5] == 'h') else 0
        h3m5 = 1 if (combinations[i][2] - 5 >= 0 and elements[combinations[i][2] - 5] == 'h') else 0

        h1p1 = 1 if (combinations[i][0] + 1 <= len(elements) - 1 and elements[combinations[i][0] + 1] == 'h') else 0
        h2p1 = 1 if (combinations[i][1] + 1 <= len(elements) - 1 and elements[combinations[i][1] + 1] == 'h') else 0
        h3p1 = 1 if (combinations[i][2] + 1 <= len(elements) - 1 and elements[combinations[i][2] + 1] == 'h') else 0

        h1p2 = 1 if (combinations[i][0] + 2 <= len(elements) - 1 and elements[combinations[i][0] + 2] == 'h') else 0
        h2p2 = 1 if (combinations[i][1] + 2 <= len(elements) - 1 and elements[combinations[i][1] + 2] == 'h') else 0
        h3p2 = 1 if (combinations[i][2] + 2 <= len(elements) - 1 and elements[combinations[i][2] + 2] == 'h') else 0

        h1p3 = 1 if (combinations[i][0] + 3 <= len(elements) - 1 and elements[combinations[i][0] + 3] == 'h') else 0
        h2p3 = 1 if (combinations[i][1] + 3 <= len(elements) - 1 and elements[combinations[i][1] + 3] == 'h') else 0
        h3p3 = 1 if (combinations[i][2] + 3 <= len(elements) - 1 and elements[combinations[i][2] + 3] == 'h') else 0

        h1p4 = 1 if (combinations[i][0] + 4 <= len(elements) - 1 and elements[combinations[i][0] + 4] == 'h') else 0
        h2p4 = 1 if (combinations[i][1] + 4 <= len(elements) - 1 and elements[combinations[i][1] + 4] == 'h') else 0
        h3p4 = 1 if (combinations[i][2] + 4 <= len(elements) - 1 and elements[combinations[i][2] + 4] == 'h') else 0

        h1p5 = 1 if (combinations[i][0] + 5 <= len(elements) - 1 and elements[combinations[i][0] + 5] == 'h') else 0
        h2p5 = 1 if (combinations[i][1] + 5 <= len(elements) - 1 and elements[combinations[i][1] + 5] == 'h') else 0
        h3p5 = 1 if (combinations[i][2] + 5 <= len(elements) - 1 and elements[combinations[i][2] + 5] == 'h') else 0

        i1m1 = 1 if (combinations[i][0] - 1 >= 0 and elements[combinations[i][0] - 1] == 'i') else 0
        i2m1 = 1 if (combinations[i][1] - 1 >= 0 and elements[combinations[i][1] - 1] == 'i') else 0
        i3m1 = 1 if (combinations[i][2] - 1 >= 0 and elements[combinations[i][2] - 1] == 'i') else 0

        i1m2 = 1 if (combinations[i][0] - 2 >= 0 and elements[combinations[i][0] - 2] == 'i') else 0
        i2m2 = 1 if (combinations[i][1] - 2 >= 0 and elements[combinations[i][1] - 2] == 'i') else 0
        i3m2 = 1 if (combinations[i][2] - 2 >= 0 and elements[combinations[i][2] - 2] == 'i') else 0

        i1m3 = 1 if (combinations[i][0] - 3 >= 0 and elements[combinations[i][0] - 3] == 'i') else 0
        i2m3 = 1 if (combinations[i][1] - 3 >= 0 and elements[combinations[i][1] - 3] == 'i') else 0
        i3m3 = 1 if (combinations[i][2] - 3 >= 0 and elements[combinations[i][2] - 3] == 'i') else 0

        i1m4 = 1 if (combinations[i][0] - 4 >= 0 and elements[combinations[i][0] - 4] == 'i') else 0
        i2m4 = 1 if (combinations[i][1] - 4 >= 0 and elements[combinations[i][1] - 4] == 'i') else 0
        i3m4 = 1 if (combinations[i][2] - 4 >= 0 and elements[combinations[i][2] - 4] == 'i') else 0

        i1m5 = 1 if (combinations[i][0] - 5 >= 0 and elements[combinations[i][0] - 5] == 'i') else 0
        i2m5 = 1 if (combinations[i][1] - 5 >= 0 and elements[combinations[i][1] - 5] == 'i') else 0
        i3m5 = 1 if (combinations[i][2] - 5 >= 0 and elements[combinations[i][2] - 5] == 'i') else 0

        i1p1 = 1 if (combinations[i][0] + 1 <= len(elements) - 1 and elements[combinations[i][0] + 1] == 'i') else 0
        i2p1 = 1 if (combinations[i][1] + 1 <= len(elements) - 1 and elements[combinations[i][1] + 1] == 'i') else 0
        i3p1 = 1 if (combinations[i][2] + 1 <= len(elements) - 1 and elements[combinations[i][2] + 1] == 'i') else 0

        i1p2 = 1 if (combinations[i][0] + 2 <= len(elements) - 1 and elements[combinations[i][0] + 2] == 'i') else 0
        i2p2 = 1 if (combinations[i][1] + 2 <= len(elements) - 1 and elements[combinations[i][1] + 2] == 'i') else 0
        i3p2 = 1 if (combinations[i][2] + 2 <= len(elements) - 1 and elements[combinations[i][2] + 2] == 'i') else 0

        i1p3 = 1 if (combinations[i][0] + 3 <= len(elements) - 1 and elements[combinations[i][0] + 3] == 'i') else 0
        i2p3 = 1 if (combinations[i][1] + 3 <= len(elements) - 1 and elements[combinations[i][1] + 3] == 'i') else 0
        i3p3 = 1 if (combinations[i][2] + 3 <= len(elements) - 1 and elements[combinations[i][2] + 3] == 'i') else 0

        i1p4 = 1 if (combinations[i][0] + 4 <= len(elements) - 1 and elements[combinations[i][0] + 4] == 'i') else 0
        i2p4 = 1 if (combinations[i][1] + 4 <= len(elements) - 1 and elements[combinations[i][1] + 4] == 'i') else 0
        i3p4 = 1 if (combinations[i][2] + 4 <= len(elements) - 1 and elements[combinations[i][2] + 4] == 'i') else 0

        i1p5 = 1 if (combinations[i][0] + 5 <= len(elements) - 1 and elements[combinations[i][0] + 5] == 'i') else 0
        i2p5 = 1 if (combinations[i][1] + 5 <= len(elements) - 1 and elements[combinations[i][1] + 5] == 'i') else 0
        i3p5 = 1 if (combinations[i][2] + 5 <= len(elements) - 1 and elements[combinations[i][2] + 5] == 'i') else 0

        j1m1 = 1 if (combinations[i][0] - 1 >= 0 and elements[combinations[i][0] - 1] == 'm') else 0
        j2m1 = 1 if (combinations[i][1] - 1 >= 0 and elements[combinations[i][1] - 1] == 'm') else 0
        j3m1 = 1 if (combinations[i][2] - 1 >= 0 and elements[combinations[i][2] - 1] == 'm') else 0

        j1m2 = 1 if (combinations[i][0] - 2 >= 0 and elements[combinations[i][0] - 2] == 'm') else 0
        j2m2 = 1 if (combinations[i][1] - 2 >= 0 and elements[combinations[i][1] - 2] == 'm') else 0
        j3m2 = 1 if (combinations[i][2] - 2 >= 0 and elements[combinations[i][2] - 2] == 'm') else 0

        j1m3 = 1 if (combinations[i][0] - 3 >= 0 and elements[combinations[i][0] - 3] == 'm') else 0
        j2m3 = 1 if (combinations[i][1] - 3 >= 0 and elements[combinations[i][1] - 3] == 'm') else 0
        j3m3 = 1 if (combinations[i][2] - 3 >= 0 and elements[combinations[i][2] - 3] == 'm') else 0

        j1m4 = 1 if (combinations[i][0] - 4 >= 0 and elements[combinations[i][0] - 4] == 'm') else 0
        j2m4 = 1 if (combinations[i][1] - 4 >= 0 and elements[combinations[i][1] - 4] == 'm') else 0
        j3m4 = 1 if (combinations[i][2] - 4 >= 0 and elements[combinations[i][2] - 4] == 'm') else 0

        j1m5 = 1 if (combinations[i][0] - 5 >= 0 and elements[combinations[i][0] - 5] == 'm') else 0
        j2m5 = 1 if (combinations[i][1] - 5 >= 0 and elements[combinations[i][1] - 5] == 'm') else 0
        j3m5 = 1 if (combinations[i][2] - 5 >= 0 and elements[combinations[i][2] - 5] == 'm') else 0

        j1p1 = 1 if (combinations[i][0] + 1 <= len(elements) - 1 and elements[combinations[i][0] + 1] == 'm') else 0
        j2p1 = 1 if (combinations[i][1] + 1 <= len(elements) - 1 and elements[combinations[i][1] + 1] == 'm') else 0
        j3p1 = 1 if (combinations[i][2] + 1 <= len(elements) - 1 and elements[combinations[i][2] + 1] == 'm') else 0

        j1p2 = 1 if (combinations[i][0] + 2 <= len(elements) - 1 and elements[combinations[i][0] + 2] == 'm') else 0
        j2p2 = 1 if (combinations[i][1] + 2 <= len(elements) - 1 and elements[combinations[i][1] + 2] == 'm') else 0
        j3p2 = 1 if (combinations[i][2] + 2 <= len(elements) - 1 and elements[combinations[i][2] + 2] == 'm') else 0
        j1p3 = 1 if (combinations[i][0] + 3 <= len(elements) - 1 and elements[combinations[i][0] + 3] == 'm') else 0
        j2p3 = 1 if (combinations[i][1] + 3 <= len(elements) - 1 and elements[combinations[i][1] + 3] == 'm') else 0
        j3p3 = 1 if (combinations[i][2] + 3 <= len(elements) - 1 and elements[combinations[i][2] + 3] == 'm') else 0

        j1p4 = 1 if (combinations[i][0] + 4 <= len(elements) - 1 and elements[combinations[i][0] + 4] == 'm') else 0
        j2p4 = 1 if (combinations[i][1] + 4 <= len(elements) - 1 and elements[combinations[i][1] + 4] == 'm') else 0
        j3p4 = 1 if (combinations[i][2] + 4 <= len(elements) - 1 and elements[combinations[i][2] + 4] == 'm') else 0

        j1p5 = 1 if (combinations[i][0] + 5 <= len(elements) - 1 and elements[combinations[i][0] + 5] == 'm') else 0
        j2p5 = 1 if (combinations[i][1] + 5 <= len(elements) - 1 and elements[combinations[i][1] + 5] == 'm') else 0
        j3p5 = 1 if (combinations[i][2] + 5 <= len(elements) - 1 and elements[combinations[i][2] + 5] == 'm') else 0

        b1m1 = 1 if (combinations[i][0] - 1 >= 0 and elements[combinations[i][0] - 1] == 'b') else 0
        b2m1 = 1 if (combinations[i][1] - 1 >= 0 and elements[combinations[i][1] - 1] == 'b') else 0
        b3m1 = 1 if (combinations[i][2] - 1 >= 0 and elements[combinations[i][2] - 1] == 'b') else 0

        b1m2 = 1 if (combinations[i][0] - 2 >= 0 and elements[combinations[i][0] - 2] == 'b') else 0
        b2m2 = 1 if (combinations[i][1] - 2 >= 0 and elements[combinations[i][1] - 2] == 'b') else 0
        b3m2 = 1 if (combinations[i][2] - 2 >= 0 and elements[combinations[i][2] - 2] == 'b') else 0

        b1m3 = 1 if (combinations[i][0] - 3 >= 0 and elements[combinations[i][0] - 3] == 'b') else 0
        b2m3 = 1 if (combinations[i][1] - 3 >= 0 and elements[combinations[i][1] - 3] == 'b') else 0
        b3m3 = 1 if (combinations[i][2] - 3 >= 0 and elements[combinations[i][2] - 3] == 'b') else 0

        b1m4 = 1 if (combinations[i][0] - 4 >= 0 and elements[combinations[i][0] - 4] == 'b') else 0
        b2m4 = 1 if (combinations[i][1] - 4 >= 0 and elements[combinations[i][1] - 4] == 'b') else 0
        b3m4 = 1 if (combinations[i][2] - 4 >= 0 and elements[combinations[i][2] - 4] == 'b') else 0

        b1m5 = 1 if (combinations[i][0] - 5 >= 0 and elements[combinations[i][0] - 5] == 'b') else 0
        b2m5 = 1 if (combinations[i][1] - 5 >= 0 and elements[combinations[i][1] - 5] == 'b') else 0
        b3m5 = 1 if (combinations[i][2] - 5 >= 0 and elements[combinations[i][2] - 5] == 'b') else 0

        b1p1 = 1 if (combinations[i][0] + 1 <= len(elements) - 1 and elements[combinations[i][0] + 1] == 'b') else 0
        b2p1 = 1 if (combinations[i][1] + 1 <= len(elements) - 1 and elements[combinations[i][1] + 1] == 'b') else 0
        b3p1 = 1 if (combinations[i][2] + 1 <= len(elements) - 1 and elements[combinations[i][2] + 1] == 'b') else 0

        b1p2 = 1 if (combinations[i][0] + 2 <= len(elements) - 1 and elements[combinations[i][0] + 2] == 'b') else 0
        b2p2 = 1 if (combinations[i][1] + 2 <= len(elements) - 1 and elements[combinations[i][1] + 2] == 'b') else 0
        b3p2 = 1 if (combinations[i][2] + 2 <= len(elements) - 1 and elements[combinations[i][2] + 2] == 'b') else 0
        b1p3 = 1 if (combinations[i][0] + 3 <= len(elements) - 1 and elements[combinations[i][0] + 3] == 'b') else 0
        b2p3 = 1 if (combinations[i][1] + 3 <= len(elements) - 1 and elements[combinations[i][1] + 3] == 'b') else 0
        b3p3 = 1 if (combinations[i][2] + 3 <= len(elements) - 1 and elements[combinations[i][2] + 3] == 'b') else 0

        b1p4 = 1 if (combinations[i][0] + 4 <= len(elements) - 1 and elements[combinations[i][0] + 4] == 'b') else 0
        b2p4 = 1 if (combinations[i][1] + 4 <= len(elements) - 1 and elements[combinations[i][1] + 4] == 'b') else 0
        b3p4 = 1 if (combinations[i][2] + 4 <= len(elements) - 1 and elements[combinations[i][2] + 4] == 'b') else 0

        b1p5 = 1 if (combinations[i][0] + 5 <= len(elements) - 1 and elements[combinations[i][0] + 5] == 'b') else 0
        b2p5 = 1 if (combinations[i][1] + 5 <= len(elements) - 1 and elements[combinations[i][1] + 5] == 'b') else 0
        b3p5 = 1 if (combinations[i][2] + 5 <= len(elements) - 1 and elements[combinations[i][2] + 5] == 'b') else 0

        lc1m1 = 1 if (combinations[i][0] - 1 >= 0 and loop_types[combinations[i][0] - 1] == 'c') else 0
        lc2m1 = 1 if (combinations[i][1] - 1 >= 0 and loop_types[combinations[i][1] - 1] == 'c') else 0
        lc3m1 = 1 if (combinations[i][2] - 1 >= 0 and loop_types[combinations[i][2] - 1] == 'c') else 0

        lc1m2 = 1 if (combinations[i][0] - 2 >= 0 and loop_types[combinations[i][0] - 2] == 'c') else 0
        lc2m2 = 1 if (combinations[i][1] - 2 >= 0 and loop_types[combinations[i][1] - 2] == 'c') else 0
        lc3m2 = 1 if (combinations[i][2] - 2 >= 0 and loop_types[combinations[i][2] - 2] == 'c') else 0

        lc1m3 = 1 if (combinations[i][0] - 3 >= 0 and loop_types[combinations[i][0] - 3] == 'c') else 0
        lc2m3 = 1 if (combinations[i][1] - 3 >= 0 and loop_types[combinations[i][1] - 3] == 'c') else 0
        lc3m3 = 1 if (combinations[i][2] - 3 >= 0 and loop_types[combinations[i][2] - 3] == 'c') else 0

        lc1m4 = 1 if (combinations[i][0] - 4 >= 0 and loop_types[combinations[i][0] - 4] == 'c') else 0
        lc2m4 = 1 if (combinations[i][1] - 4 >= 0 and loop_types[combinations[i][1] - 4] == 'c') else 0
        lc3m4 = 1 if (combinations[i][2] - 4 >= 0 and loop_types[combinations[i][2] - 4] == 'c') else 0

        lc1m5 = 1 if (combinations[i][0] - 5 >= 0 and loop_types[combinations[i][0] - 5] == 'c') else 0
        lc2m5 = 1 if (combinations[i][1] - 5 >= 0 and loop_types[combinations[i][1] - 5] == 'c') else 0
        lc3m5 = 1 if (combinations[i][2] - 5 >= 0 and loop_types[combinations[i][2] - 5] == 'c') else 0

        lc1p1 = 1 if (combinations[i][0] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 1] == 'c') else 0
        lc2p1 = 1 if (combinations[i][1] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 1] == 'c') else 0
        lc3p1 = 1 if (combinations[i][2] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 1] == 'c') else 0

        lc1p2 = 1 if (combinations[i][0] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 2] == 'c') else 0
        lc2p2 = 1 if (combinations[i][1] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 2] == 'c') else 0
        lc3p2 = 1 if (combinations[i][2] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 2] == 'c') else 0
        lc1p3 = 1 if (combinations[i][0] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 3] == 'c') else 0
        lc2p3 = 1 if (combinations[i][1] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 3] == 'c') else 0
        lc3p3 = 1 if (combinations[i][2] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 3] == 'c') else 0

        lc1p4 = 1 if (combinations[i][0] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 4] == 'c') else 0
        lc2p4 = 1 if (combinations[i][1] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 4] == 'c') else 0
        lc3p4 = 1 if (combinations[i][2] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 4] == 'c') else 0

        lc1p5 = 1 if (combinations[i][0] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 5] == 'c') else 0
        lc2p5 = 1 if (combinations[i][1] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 5] == 'c') else 0
        lc3p5 = 1 if (combinations[i][2] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 5] == 'c') else 0

        lp1m1 = 1 if (combinations[i][0] - 1 >= 0 and loop_types[combinations[i][0] - 1] == 'p') else 0
        lp2m1 = 1 if (combinations[i][1] - 1 >= 0 and loop_types[combinations[i][1] - 1] == 'p') else 0
        lp3m1 = 1 if (combinations[i][2] - 1 >= 0 and loop_types[combinations[i][2] - 1] == 'p') else 0

        lp1m2 = 1 if (combinations[i][0] - 2 >= 0 and loop_types[combinations[i][0] - 2] == 'p') else 0
        lp2m2 = 1 if (combinations[i][1] - 2 >= 0 and loop_types[combinations[i][1] - 2] == 'p') else 0
        lp3m2 = 1 if (combinations[i][2] - 2 >= 0 and loop_types[combinations[i][2] - 2] == 'p') else 0

        lp1m3 = 1 if (combinations[i][0] - 3 >= 0 and loop_types[combinations[i][0] - 3] == 'p') else 0
        lp2m3 = 1 if (combinations[i][1] - 3 >= 0 and loop_types[combinations[i][1] - 3] == 'p') else 0
        lp3m3 = 1 if (combinations[i][2] - 3 >= 0 and loop_types[combinations[i][2] - 3] == 'p') else 0

        lp1m4 = 1 if (combinations[i][0] - 4 >= 0 and loop_types[combinations[i][0] - 4] == 'p') else 0
        lp2m4 = 1 if (combinations[i][1] - 4 >= 0 and loop_types[combinations[i][1] - 4] == 'p') else 0
        lp3m4 = 1 if (combinations[i][2] - 4 >= 0 and loop_types[combinations[i][2] - 4] == 'p') else 0

        lp1m5 = 1 if (combinations[i][0] - 5 >= 0 and loop_types[combinations[i][0] - 5] == 'p') else 0
        lp2m5 = 1 if (combinations[i][1] - 5 >= 0 and loop_types[combinations[i][1] - 5] == 'p') else 0
        lp3m5 = 1 if (combinations[i][2] - 5 >= 0 and loop_types[combinations[i][2] - 5] == 'p') else 0

        lp1p1 = 1 if (combinations[i][0] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 1] == 'p') else 0
        lp2p1 = 1 if (combinations[i][1] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 1] == 'p') else 0
        lp3p1 = 1 if (combinations[i][2] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 1] == 'p') else 0

        lp1p2 = 1 if (combinations[i][0] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 2] == 'p') else 0
        lp2p2 = 1 if (combinations[i][1] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 2] == 'p') else 0
        lp3p2 = 1 if (combinations[i][2] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 2] == 'p') else 0
        lp1p3 = 1 if (combinations[i][0] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 3] == 'p') else 0
        lp2p3 = 1 if (combinations[i][1] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 3] == 'p') else 0
        lp3p3 = 1 if (combinations[i][2] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 3] == 'p') else 0

        lp1p4 = 1 if (combinations[i][0] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 4] == 'p') else 0
        lp2p4 = 1 if (combinations[i][1] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 4] == 'p') else 0
        lp3p4 = 1 if (combinations[i][2] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 4] == 'p') else 0

        lp1p5 = 1 if (combinations[i][0] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 5] == 'p') else 0
        lp2p5 = 1 if (combinations[i][1] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 5] == 'p') else 0
        lp3p5 = 1 if (combinations[i][2] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 5] == 'p') else 0

        li1m1 = 1 if (combinations[i][0] - 1 >= 0 and loop_types[combinations[i][0] - 1] == 'i') else 0
        li2m1 = 1 if (combinations[i][1] - 1 >= 0 and loop_types[combinations[i][1] - 1] == 'i') else 0
        li3m1 = 1 if (combinations[i][2] - 1 >= 0 and loop_types[combinations[i][2] - 1] == 'i') else 0

        li1m2 = 1 if (combinations[i][0] - 2 >= 0 and loop_types[combinations[i][0] - 2] == 'i') else 0
        li2m2 = 1 if (combinations[i][1] - 2 >= 0 and loop_types[combinations[i][1] - 2] == 'i') else 0
        li3m2 = 1 if (combinations[i][2] - 2 >= 0 and loop_types[combinations[i][2] - 2] == 'i') else 0

        li1m3 = 1 if (combinations[i][0] - 3 >= 0 and loop_types[combinations[i][0] - 3] == 'i') else 0
        li2m3 = 1 if (combinations[i][1] - 3 >= 0 and loop_types[combinations[i][1] - 3] == 'i') else 0
        li3m3 = 1 if (combinations[i][2] - 3 >= 0 and loop_types[combinations[i][2] - 3] == 'i') else 0

        li1m4 = 1 if (combinations[i][0] - 4 >= 0 and loop_types[combinations[i][0] - 4] == 'i') else 0
        li2m4 = 1 if (combinations[i][1] - 4 >= 0 and loop_types[combinations[i][1] - 4] == 'i') else 0
        li3m4 = 1 if (combinations[i][2] - 4 >= 0 and loop_types[combinations[i][2] - 4] == 'i') else 0

        li1m5 = 1 if (combinations[i][0] - 5 >= 0 and loop_types[combinations[i][0] - 5] == 'i') else 0
        li2m5 = 1 if (combinations[i][1] - 5 >= 0 and loop_types[combinations[i][1] - 5] == 'i') else 0
        li3m5 = 1 if (combinations[i][2] - 5 >= 0 and loop_types[combinations[i][2] - 5] == 'i') else 0

        li1p1 = 1 if (combinations[i][0] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 1] == 'i') else 0
        li2p1 = 1 if (combinations[i][1] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 1] == 'i') else 0
        li3p1 = 1 if (combinations[i][2] + 1 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 1] == 'i') else 0

        li1p2 = 1 if (combinations[i][0] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 2] == 'i') else 0
        li2p2 = 1 if (combinations[i][1] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 2] == 'i') else 0
        li3p2 = 1 if (combinations[i][2] + 2 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 2] == 'i') else 0
        li1p3 = 1 if (combinations[i][0] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 3] == 'i') else 0
        li2p3 = 1 if (combinations[i][1] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 3] == 'i') else 0
        li3p3 = 1 if (combinations[i][2] + 3 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 3] == 'i') else 0

        li1p4 = 1 if (combinations[i][0] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 4] == 'i') else 0
        li2p4 = 1 if (combinations[i][1] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 4] == 'i') else 0
        li3p4 = 1 if (combinations[i][2] + 4 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 4] == 'i') else 0

        li1p5 = 1 if (combinations[i][0] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][0] + 5] == 'i') else 0
        li2p5 = 1 if (combinations[i][1] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][1] + 5] == 'i') else 0
        li3p5 = 1 if (combinations[i][2] + 5 <= len(loop_types) - 1 and loop_types[combinations[i][2] + 5] == 'i') else 0

        part = get_element(all_elements, combinations[i][0])
        fl1 = part[1] - part[0]
        fed1 = part[1] - combinations[i][0]

        part = get_element(all_elements, combinations[i][1])
        fl2 = part[1] - part[0]
        fed2 = part[1] - combinations[i][1]

        part = get_element(all_elements, combinations[i][2])
        fl3 = part[1] - part[0]
        fed3 = part[1] - combinations[i][2]

        part = get_element(all_elements, combinations[i][0] - 1)
        fl1m1 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] - 1)
        fl2m1 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] - 1)
        fl3m1 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] - 2)
        fl1m2 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] - 2)
        fl2m2 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] - 2)
        fl3m2 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] - 3)
        fl1m3 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] - 3)
        fl2m3 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] - 3)
        fl3m3 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] - 4)
        fl1m4 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] - 4)
        fl2m4 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] - 4)
        fl3m4 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] - 5)
        fl1m5 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] - 5)
        fl2m5 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] - 5)
        fl3m5 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] + 1)
        fl1p1 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] + 1)
        fl2p1 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] + 1)
        fl3p1 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] + 2)
        fl1p2 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] + 2)
        fl2p2 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] + 2)
        fl3p2 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] + 3)
        fl1p3 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] + 3)
        fl2p3 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] + 3)
        fl3p3 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] + 4)
        fl1p4 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] + 4)
        fl2p4 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] + 4)
        fl3p4 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] + 5)
        fl1p5 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][1] + 5)
        fl2p5 = part[1] - part[0] if part else 0
        part = get_element(all_elements, combinations[i][2] + 5)
        fl3p5 = part[1] - part[0] if part else 0

        part = get_element(all_elements, combinations[i][0] - 1)
        fed1m1 = part[1] - combinations[i][0] + 1 if part else 0
        part = get_element(all_elements, combinations[i][1] - 1)
        fed2m1 = part[1] - combinations[i][1] + 1 if part else 0
        part = get_element(all_elements, combinations[i][2] - 1)
        fed3m1 = part[1] - combinations[i][2] + 1 if part else 0

        part = get_element(all_elements, combinations[i][0] - 2)
        fed1m2 = part[1] - combinations[i][0] + 2 if part else 0
        part = get_element(all_elements, combinations[i][1] - 2)
        fed2m2 = part[1] - combinations[i][1] + 2 if part else 0
        part = get_element(all_elements, combinations[i][2] - 2)
        fed3m2 = part[1] - combinations[i][2] + 2 if part else 0

        part = get_element(all_elements, combinations[i][0] - 3)
        fed1m3 = part[1] - combinations[i][0] + 3 if part else 0
        part = get_element(all_elements, combinations[i][1] - 3)
        fed2m3 = part[1] - combinations[i][1] + 3 if part else 0
        part = get_element(all_elements, combinations[i][2] - 3)
        fed3m3 = part[1] - combinations[i][2] + 3 if part else 0

        part = get_element(all_elements, combinations[i][0] - 4)
        fed1m4 = part[1] - combinations[i][0] + 4 if part else 0
        part = get_element(all_elements, combinations[i][1] - 4)
        fed2m4 = part[1] - combinations[i][1] + 4 if part else 0
        part = get_element(all_elements, combinations[i][2] - 4)
        fed3m4 = part[1] - combinations[i][2] + 4 if part else 0

        part = get_element(all_elements, combinations[i][0] - 5)
        fed1m5 = part[1] - combinations[i][0] + 5 if part else 0
        part = get_element(all_elements, combinations[i][1] - 5)
        fed2m5 = part[1] - combinations[i][1] + 5 if part else 0
        part = get_element(all_elements, combinations[i][2] - 5)
        fed3m5 = part[1] - combinations[i][2] + 5 if part else 0

        part = get_element(all_elements, combinations[i][0] + 1)
        fed1p1 = part[1] - combinations[i][0] - 1 if part else 0
        part = get_element(all_elements, combinations[i][1] + 1)
        fed2p1 = part[1] - combinations[i][1] - 1 if part else 0
        part = get_element(all_elements, combinations[i][2] + 1)
        fed3p1 = part[1] - combinations[i][2] - 1 if part else 0

        part = get_element(all_elements, combinations[i][0] + 2)
        fed1p2 = part[1] - combinations[i][0] - 2 if part else 0
        part = get_element(all_elements, combinations[i][1] + 2)
        fed2p2 = part[1] - combinations[i][1] - 2 if part else 0
        part = get_element(all_elements, combinations[i][2] + 2)
        fed3p2 = part[1] - combinations[i][2] - 2 if part else 0

        part = get_element(all_elements, combinations[i][0] + 3)
        fed1p3 = part[1] - combinations[i][0] - 3 if part else 0
        part = get_element(all_elements, combinations[i][1] + 3)
        fed2p3 = part[1] - combinations[i][1] - 3 if part else 0
        part = get_element(all_elements, combinations[i][2] + 3)
        fed3p3 = part[1] - combinations[i][2] - 3 if part else 0

        part = get_element(all_elements, combinations[i][0] + 4)
        fed1p4 = part[1] - combinations[i][0] - 4 if part else 0
        part = get_element(all_elements, combinations[i][1] + 4)
        fed2p4 = part[1] - combinations[i][1] - 4 if part else 0
        part = get_element(all_elements, combinations[i][2] + 4)
        fed3p4 = part[1] - combinations[i][2] - 4 if part else 0

        part = get_element(all_elements, combinations[i][0] + 5)
        fed1p5 = part[1] - combinations[i][0] - 5 if part else 0
        part = get_element(all_elements, combinations[i][1] + 5)
        fed2p5 = part[1] - combinations[i][1] - 5 if part else 0
        part = get_element(all_elements, combinations[i][2] + 5)
        fed3p5 = part[1] - combinations[i][2] - 5 if part else 0

        feature_table.loc[i] = [same12, local12, longrange12, same23, local23, longrange23, same13, local13,
                                longrange13, a1m5, c1m5, g1m5, u1m5, s1m5, h1m5, b1m5, i1m5, j1m5, lc1m5,
                                li1m5, lp1m5, fl1m5, fed1m5, a1m4, c1m4, g1m4, u1m4, s1m4, h1m4, b1m4, i1m4,
                                j1m4, lc1m4, li1m4, lp1m4, fl1m4, fed1m4, a1m3, c1m3, g1m3, u1m3, s1m3, h1m3, b1m3,
                                i1m3, j1m3, lc1m3, li1m3, lp1m3, fl1m3, fed1m3, a1m2, c1m2, g1m2, u1m2, s1m2, h1m2, b1m2,
                                i1m2, j1m2, lc1m2, li1m2, lp1m2, fl1m2, fed1m2, a1m1, c1m1, g1m1, u1m1, s1m1, h1m1, b1m1,
                                i1m1, j1m1, lc1m1, li1m1, lp1m1, fl1m1, fed1m1, a1, c1, g1, u1, s1, h1, b1, i1, j1,
                                lc1, li1, lp1, fl1, fed1, a1p1, c1p1, g1p1, u1p1, s1p1, h1p1, b1p1, i1p1, j1p1, lc1p1,
                                li1p1, lp1p1, fl1p1, fed1p1, a1p2, c1p2, g1p2, u1p2, s1p2, h1p2, b1p2, i1p2, j1p2, lc1p2,
                                li1p2, lp1p2, fl1p2, fed1p2, a1p3, c1p3, g1p3, u1p3, s1p3, h1p3, b1p3, i1p3, j1p3, lc1p3,
                                li1p3, lp1p3, fl1p3, fed1p3, a1p4, c1p4, g1p4, u1p4, s1p4, h1p4, b1p4, i1p4, j1p4, lc1p4,
                                li1p4, lp1p4, fl1p4, fed1p4, a1p5, c1p5, g1p5, u1p5, s1p5, h1p5, b1p5, i1p5, j1p5, lc1p5,
                                li1p5, lp1p5, fl1p5, fed1p5, a2m5, c2m5, g2m5, u2m5, s2m5, h2m5, b2m5, i2m5, j2m5, lc2m5,
                                li2m5, lp2m5, fl2m5, fed2m5, a2m4, c2m4, g2m4, u2m4, s2m4, h2m4, b2m4, i2m4, j2m4, lc2m4,
                                li2m4, lp2m4, fl2m4, fed2m4, a2m3, c2m3, g2m3,u2m3, s2m3, h2m3, b2m3, i2m3, j2m3, lc2m3,
                                li2m3, lp2m3, fl2m3, fed2m3, a2m2, c2m2, g2m2, u2m2, s2m2, h2m2, b2m2, i2m2, j2m2, lc2m2,
                                li2m2, lp2m2, fl2m2, fed2m2, a2m1, c2m1, g2m1, u2m1, s2m1, h2m1, b2m1, i2m1, j2m1, lc2m1,
                                li2m1, lp2m1, fl2m1, fed2m1, a2, c2, g2, u2, s2, h2, b2, i2, j2, lc2, li2, lp2, fl2,
                                fed2, a2p1, c2p1, g2p1, u2p1, s2p1, h2p1, b2p1, i2p1, j2p1, lc2p1, li2p1, lp2p1, fl2p1,
                                fed2p1, a2p2, c2p2, g2p2, u2p2, s2p2, h2p2, b2p2, i2p2, j2p2, lc2p2, li2p2, lp2p2, fl2p2,
                                fed2p2, a2p3, c2p3, g2p3, u2p3, s2p3, h2p3, b2p3, i2p3, j2p3, lc2p3, li2p3, lp2p3, fl2p3,
                                fed2p3, a2p4, c2p4, g2p4, u2p4, s2p4, h2p4, b2p4, i2p4, j2p4, lc2p4, li2p4, lp2p4, fl2p4,
                                fed2p4, a2p5, c2p5, g2p5, u2p5, s2p5, h2p5, b2p5, i2p5, j2p5, lc2p5, li2p5, lp2p5, fl2p5,
                                fed2p5, a3m5, c3m5, g3m5, u3m5, s3m5, h3m5, b3m5, i3m5, j3m5, lc3m5, li3m5, lp3m5, fl3m5,
                                fed3m5, a3m4, c3m4, g3m4, u3m4, s3m4, h3m4, b3m4, i3m4, j3m4, lc3m4, li3m4, lp3m4, fl3m4,
                                fed3m4, a3m3, c3m3, g3m3, u3m3, s3m3, h3m3, b3m3, i3m3, j3m3, lc3m3, li3m3, lp3m3, fl3m3,
                                fed3m3, a3m2, c3m2, g3m2, u3m2, s3m2, h3m2, b3m2, i3m2, j3m2, lc3m2, li3m2,lp3m2, fl3m2,
                                fed3m2, a3m1, c3m1, g3m1, u3m1, s3m1, h3m1, b3m1, i3m1, j3m1, lc3m1, li3m1, lp3m1, fl3m1,
                                fed3m1, a3, c3, g3, u3, s3, h3, b3, i3, j3, lc3, li3, lp3, fl3, fed3, a3p1, c3p1,
                                g3p1, u3p1, s3p1, h3p1, b3p1, i3p1, j3p1, lc3p1, li3p1, lp3p1, fl3p1, fed3p1, a3p2, c3p2,
                                g3p2, u3p2, s3p2, h3p2, b3p2, i3p2, j3p2, lc3p2, li3p2, lp3p2, fl3p2, fed3p2, a3p3, c3p3,
                                g3p3, u3p3, s3p3, h3p3, b3p3, i3p3, j3p3, lc3p3, li3p3, lp3p3, fl3p3, fed3p3, a3p4, c3p4,
                                g3p4, u3p4, s3p4, h3p4, b3p4, i3p4, j3p4, lc3p4, li3p4, lp3p4, fl3p4, fed3p4, a3p5, c3p5,
                                g3p5, u3p5, s3p5, h3p5, b3p5, i3p5, j3p5, lc3p5, li3p5, lp3p5, fl3p5, fed3p5]
    print("DATA", feature_table)
    feature_table.to_csv('rna_features.csv', sep='\t')