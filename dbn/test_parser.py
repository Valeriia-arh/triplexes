from unittest import TestCase

from parse_sequence import Parser


class TestParser(TestCase):
    def test_preprocess(self):
        parser = Parser(0)
        self.assertEqual("...((.......))..", parser.preprocess("...(((...)..)).."))
        self.assertEqual("...((............))..", parser.preprocess("...((...((...)..))).."))
        self.assertEqual("...................", parser.preprocess("...(...((...)..)).."))
        self.assertEqual("............", parser.preprocess("((...)(...))"))
        self.assertEqual("...((.....))..((...((....((.......)).......[[...))....]]...((...))..((...))...)).....",
                         parser.preprocess("...((.....))..((...((....((..[[...))..].]..[[...))....]]...((...))..((...))...))....."))

    def test_parse_1(self):
        parser = Parser(0)

        self.assertEqual(
            "hhhhhhhhhhhh",
            parser.parse("............")
        )
        self.assertEqual(set(), parser.stems)
        self.assertEqual({'hairpin': [[(0, 12)]]}, parser.loops_type1)

        self.assertEqual(
            "iiisshhhhhhhssii",
            parser.parse("...((.......))..")
        )
        self.assertEqual({(3, 13), (4, 12)}, parser.stems)
        self.assertEqual({'hairpin': [[(5, 12)]], 'internal_loop': [[(0, 3), (14, 16)]]}, parser.loops_type1)

        self.assertEqual(
            "ssshhhsssshhhsss",
            parser.parse("(((...))((...)))")
        )
        self.assertEqual({(9, 13), (8, 14), (2, 6), (0, 15), (1, 7)}, parser.stems)
        self.assertEqual({'hairpin': [[(3, 6)], [(10, 13)]]}, parser.loops_type1)

        self.assertEqual(
            "ssmmsshsshhsssshhhssmmss",
            parser.parse("((..((.[[..))((...))..))")
        )

        self.assertEqual(
            "iiissiisshhhssiissiii",
            parser.parse("...((..((...))..))...")
        )
        self.assertEqual({(7, 13), (3, 17), (4, 16), (8, 12)}, parser.stems)
        self.assertEqual(
            {'hairpin': [[(9, 12)]],'internal_loop': [[(5, 7), (14, 16)], [(0, 3), (18, 21)]]},
            parser.loops_type1
        )

        self.assertEqual(
            "iiisssshhhssbbssiii",
            parser.parse("...((((...))..))...")
        )
        self.assertEqual({(3, 15), (6, 10), (4, 14), (5, 11)}, parser.stems)
        self.assertEqual(
            {'bulging': [[(12, 14)]], 'hairpin': [[(7, 10)]], 'internal_loop': [[(0, 3), (16, 19)]]},
            parser.loops_type1
        )

        self.assertEqual(
            "iiisshhsshhhsshhssii",
            parser.parse("...((..[[...))..]]..")
        )
        self.assertEqual({(8, 16), (4, 12), (7, 17), (3, 13)}, parser.stems)
        self.assertEqual(
            {'hairpin': [[(5, 7), (9, 12)], [(14, 16)]], 'internal_loop': [[(0, 3), (18, 20)]]},
            parser.loops_type1
        )

        self.assertEqual(
            "iissiisssshhsshhsshhsshhssiissbbssiissiiii",
            parser.parse("..((..((((..[[..[[..))..]]..]]..))..))....")
        )
        self.assertEqual(
            {(2, 37), (3, 36), (6, 33), (7, 32), (8, 21), (9, 20), (12, 29), (13, 28), (16, 25), (17, 24)},
            parser.stems
        )


        self.assertEqual(
            "iissiissiisshhsshhsshhsshhssiissiissiissiiii",
            parser.parse("..((..((..((..[[..[[..))..]]..]]..))..))....")
        )
        self.assertEqual(
            {(2, 39), (14, 31), (19, 26), (15, 30), (18, 27), (11, 22), (6, 35), (3, 38), (10, 23), (7, 34)},
            parser.stems
        )

        self.assertEqual(
            "iiissiisshhhsshhhssiiisshhhhhhssiii",
            parser.parse("...((..[[...{{...]]...))......}}...")
        )
        self.assertEqual({(3, 23), (13, 30), (7, 18), (12, 31), (4, 22), (8, 17)}, parser.stems)

        self.assertEqual(
            "mmmsshhhhhssmmssmmmssiiiisshhsshhhsshhssiissiiisshhhhssmmmsshhhssmmsshhhssmmmssmmmmm",
            parser.parse("...((.....))..((...((....((..[[...))..]]..[[...))....]]...((...))..((...))...)).....")
        )
        self.assertEqual(
            {(4, 10), (42, 54), (29, 39), (15, 77), (68, 72), (19, 48), (58, 64), (14, 78),
             (3, 11), (26, 34), (67, 73), (43, 53), (59, 63), (20, 47), (25, 35), (30, 38)},
            parser.stems)

    def test_parse_2(self):
        parser = Parser(1)
        self.assertEqual(
            "cccccccccccc",
            parser.parse("............")
        )
        self.assertEqual(
            "cccsscccccccsscc",
            parser.parse("...((.......))..")
        )
        self.assertEqual(
            "cccssccsscccssccssccc",
            parser.parse("...((..((...))..))...")
        )
        self.assertEqual(
            "cccsssscccssccssccc",
            parser.parse("...((((...))..))...")
        )
        self.assertEqual(
            "iiissppsspppssppssii",
            parser.parse("...((..[[...))..]]..")
        )

        self.assertEqual(
            "ccssccssiissppssppssppssppssccssiissccsscccc",
            parser.parse("..((..((..((..[[..[[..))..]]..]]..))..))....")
        )

        self.assertEqual(
            "iissccssppssppssccsspppppssii",
            parser.parse("..((..[[..{{..]]..)).....}}..")
        )
        self.assertEqual(
            "ccssccssssppssppssppssppssccssiissccsscccc",
            parser.parse("..((..((((..[[..[[..))..]]..]]..))..))....")
        )

    def test_real_examples(self):
        parser0 = Parser(0)
        parser1 = Parser(1)

        # 1
        sequence = "(((((...[[[......)))))........]]]"
        self.assertEqual("ssssshhhssshhhhhhssssshhhhhhhhsss", parser0.preprocess_and_parse(sequence))
        self.assertEqual("ssssspppsssppppppsssssppppppppsss", parser1.preprocess_and_parse(sequence))

        # 2
        sequence = "((((((........[[[[[[[[[)))))).........]]]]]]]]]"
        self.assertEqual("sssssshhhhhhhhssssssssssssssshhhhhhhhhsssssssss", parser0.preprocess_and_parse(sequence))
        self.assertEqual("ssssssppppppppssssssssssssssspppppppppsssssssss", parser1.preprocess_and_parse(sequence))

        # 3
        sequence = "(((((((..((((........)))).(((((.......)))))....(((((.......))))))))))))...."
        self.assertEqual("sssssssmmsssshhhhhhhhssssmssssshhhhhhhsssssmmmmssssshhhhhhhssssssssssssbbbb", parser0.preprocess_and_parse(sequence))
        self.assertEqual("sssssssccssssccccccccsssscssssscccccccsssssccccssssscccccccsssssssssssscccc", parser1.preprocess_and_parse(sequence))

        # 4
        sequence = "((((((((.((((.(((.....))))))......)..)))).....(((...((((......))))...)))..))))."
        self.assertEqual("ssssssssiisssbssshhhhhssssssiiiiiiiiissssmmmmmsssiiisssshhhhhhssssiiisssmmssssb", parser0.preprocess_and_parse(sequence))
        self.assertEqual("ssssssssccssscssscccccsssssscccccccccsssscccccssscccssssccccccsssscccsssccssssc", parser1.preprocess_and_parse(sequence))

        # 5
        sequence = "............(((((((((((...[[[[[[[)))))))))))((((((((.........))).)))))...]].]]]]]."
        self.assertEqual("iiiiiiiiiiiissssssssssshhhsssssssssssssssssssssssssshhhhhhhhhsssbsssssiiissbsssssi", parser0.preprocess_and_parse(sequence))
        self.assertEqual("iiiiiiiiiiiissssssssssspppsssssssssssssssssssssssssscccccccccssscssssspppsscsssssi", parser1.preprocess_and_parse(sequence))

        # 6
        sequence = "((((((......((...((((((....))))))...))...(((.((((((((..(((.......))))))))..))))))...)).))))......"
        self.assertEqual("ssssssmmmmmmssiiisssssshhhhssssssiiissmmmsssbssssssssbbssshhhhhhhssssssssbbssssssmmmssbssssbbbbbb", parser0.preprocess_and_parse(sequence))
        self.assertEqual("ssssssccccccsscccssssssccccsssssscccsscccssscssssssssccssscccccccssssssssccsssssscccsscsssscccccc", parser1.preprocess_and_parse(sequence))

        # 7
        sequence = "((((((((....[[[[[...[[[.((((]]]......]]]]](((..(((((...(((((.....))))).)))..)).)))....))))((((((.....))))))...))))))))"
        self.assertEqual("ssssssssmmmmsssssiiissshsssssssiiiiiissssssssiisssssiiissssshhhhhsssssisssbbssisssiiiisssssssssshhhhhssssssmmmssssssss",
                        parser0.preprocess_and_parse(sequence))
        self.assertEqual("ssssssssiiiissssscccssspsssssssccccccssssssssccssssscccssssscccccssssscsssccsscsssppppsssssssssscccccssssssiiissssssss",
                         parser1.preprocess_and_parse(sequence))

        # 8
        sequence = "((((((..(((..(((..((((((((......(((((((((((....((((....))))....))))....))(((((((((.......)))))))))....))))).((((....))))....)))))))).)))...)))..))....))))"
        self.assertEqual("ssssssiisssiisssiissssssssmmmmmmsssssssssssiiiisssshhhhssssiiiissssbbbbssssssssssshhhhhhhsssssssssmmmmsssssmsssshhhhssssmmmmssssssssisssiiisssiissbbbbssss",
                         parser0.preprocess_and_parse(sequence))
        self.assertEqual("ssssssccsssccsssccssssssssccccccsssssssssssccccssssccccssssccccssssccccssssssssssscccccccsssssssssccccssssscssssccccssssccccsssssssscssscccsssccssccccssss",
                         parser1.preprocess_and_parse(sequence))

        # 9
        sequence = ".((((((..(.(((((......(((((((((.(((((((((((.((((((((((.....))))).))))).........)))))))))))......)))))))))..))))))..))))))(((((((((.(((((....)))))..)))))))))"
        self.assertEqual("mssssssiiiisssssiiiiiisssssssssisssssssssssisssssssssshhhhhsssssbsssssiiiiiiiiisssssssssssiiiiiisssssssssiisssssiiisssssssssssssssissssshhhhsssssiisssssssss",
                         parser0.preprocess_and_parse(sequence))
        self.assertEqual("cssssssccccsssssccccccssssssssscssssssssssscsssssssssscccccssssscssssscccccccccsssssssssssccccccsssssssssccssssscccssssssssssssssscsssssccccsssssccsssssssss",
                         parser1.preprocess_and_parse(sequence))

        # 14
        sequence = "(((((((((..............)))))))))...((((((((((......)))))))))).(((((((((((.((.......)).))))))).))))..(((((.((...((((((....(((.......(((.(((((((((.(((((((((....)))))))))..(((.....)))...))))....).)))))))......)))...)).))))((...((((...((((((((.....))))))))..))))...))..[.[[[[[..)).))))).(((((((.....)))))))........]]]]]]((...(((((....)))))(((((((....((((......))))....))))))).((((((((.((((((....)))))).)))))))).........))........"
        self.assertEqual(
            "ssssssssshhhhhhhhhhhhhhsssssssssmmmsssssssssshhhhhhssssssssssmsssssssssssisshhhhhhhssisssssssbssssmmsssssissmmmssssssiiiisssiiiiiiisssbssssissssmssssssssshhhhsssssssssmmssshhhhhsssmmmssssiiiiiisssssssiiiiiisssiiissbssssssiiissssiiisssssssshhhhhssssssssiissssiiissmmmmsssssmmssisssssissssssshhhhhsssssssiiiiiiiisssssmssmmmssssshhhhssssssssssssiiiisssshhhhhhssssiiiisssssssmssssssssisssssshhhhssssssissssssssmmmmmmmmmssmmmmmmmm",
            parser0.preprocess_and_parse(sequence))
        self.assertEqual(
            "sssssssssccccccccccccccsssssssssiiissssssssssccccccssssssssssissssssssssscsscccccccsscssssssscssssiissssscsspppssssssccccssscccccccssscsssscsssscsssssssssccccsssssssssccssscccccssscccssssccccccsssssssccccccssscccsscsssssscccsssscccsssssssscccccssssssssccsssscccssppppsssssppsscssssspssssssscccccsssssssppppppppsssssisscccsssssccccssssssssssssccccssssccccccssssccccssssssscsssssssscssssssccccsssssscsssssssscccccccccssiiiiiiii",
            parser1.preprocess_and_parse(sequence))

        # 17
        sequence = "....(((((..[[[[[[.)))))..........(((((.......)))))....]]]]]]......"
        self.assertEqual("iiiissssshhsssssshsssssiiiiiiiiiissssshhhhhhhsssssiiiissssssiiiiii", parser0.preprocess_and_parse(sequence))
        self.assertEqual("iiiisssssppsssssspsssssppppppppppssssscccccccsssssppppssssssiiiiii", parser1.preprocess_and_parse(sequence))

        # 18
        sequence = "(((((((((...((((((.........))))))........((((((.......))))))..)))))))))"
        self.assertEqual("sssssssssmmmsssssshhhhhhhhhssssssmmmmmmmmsssssshhhhhhhssssssmmsssssssss",
                         parser0.preprocess_and_parse(sequence))
        self.assertEqual("ssssssssscccsssssscccccccccssssssccccccccsssssscccccccssssssccsssssssss",
                         parser1.preprocess_and_parse(sequence))

        # 19
        sequence = "(((((((..((((........)))).(((((.......))))).....(((((.......))))))))))))...."
        self.assertEqual("sssssssmmsssshhhhhhhhssssmssssshhhhhhhsssssmmmmmssssshhhhhhhssssssssssssbbbb",
                         parser0.preprocess_and_parse(sequence))
        self.assertEqual("sssssssccssssccccccccsssscssssscccccccssssscccccssssscccccccsssssssssssscccc", parser1.preprocess_and_parse(sequence))

        # 20
        sequence = "((((((((((.....((((((((.......((((.............))))........)))))).)).((.((..(.((((((((...)))))))).)..)).))...))))))))))."
        self.assertEqual("ssssssssssmmmmmssssssssiiiiiiisssshhhhhhhhhhhhhssssiiiiiiiissssssbssmssissiiiisssssssshhhssssssssiiiississmmmssssssssssb",
                         parser0.preprocess_and_parse(sequence))
        self.assertEqual("sssssssssscccccsssssssscccccccsssscccccccccccccssssccccccccsssssscsscsscssccccsssssssscccssssssssccccsscsscccssssssssssc", parser1.preprocess_and_parse(sequence))
