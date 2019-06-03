import re
import sys

open_brackets = ['(', '[', '{']
close_brackets = [')', ']', '}']


def brackets_match(open: tuple, close: chr):
    return open_brackets.index(open[0]) == close_brackets.index(close)


def to_stack(stack, bracket, index, skip=False):
    if len(stack) == 0:
        stack.append([(bracket, index, skip, sys.maxsize)])
        return

    if bracket == stack[-1][-1][0]:
        stack[-1].append((bracket, index, skip, sys.maxsize))
    else:
        stack.append([(bracket, index, skip, sys.maxsize)])


class Parser(object):
    def __init__(self, classification):
        self.classification = classification

        # coordinates
        self.stems = set()
        self.loops_type1 = {}
        self.loops_type2 = {}

    def preprocess_and_parse(self, sequence):
        return self.parse(self.preprocess(sequence))

    def preprocess(self, sequence):
        prev = ""
        while prev != sequence:
            prev = sequence
            sequence = self.skip_lonely_brackets(sequence)
        return sequence

    def skip_lonely_brackets(self, sequence) -> str:
        stack_of_stacks = []

        for i, ch in enumerate(sequence):
            if ch in open_brackets:
                to_stack(stack_of_stacks, ch, i, self.should_be_deleted_bracket(ch, sequence, i))
            elif ch in close_brackets:
                sequence = self.from_stack_preproc(sequence, stack_of_stacks, ch, i, self.should_be_deleted_bracket(ch, sequence, i))
        return sequence

    def should_be_deleted_bracket(self, char, sequence, index):
        return (True if index == 0 else sequence[index - 1] != char)\
               and (True if index == len(sequence) - 1 else sequence[index + 1] != char)

    def from_stack_preproc(self, sequence, stack, bracket, index, skip):
        if len(stack) == 0:
            return sequence
        i = 0
        while i < len(stack) and not brackets_match(stack[i][-1], bracket):
            i += 1
        if i < len(stack):
            deleted = stack[i].pop()
            if len(stack[i]) == 0:
                stack.pop(i)
            if deleted[2] or skip:
                sequence = sequence[:deleted[1]] + '.' + sequence[deleted[1] + 1:]
                sequence = sequence[:index] + '.' + sequence[index + 1:]
        return sequence

    def from_stack(self, sequence, stacks, bracket, index, offset) -> (bool, bool):  # returns (isWing, isECR, isBulging)
        if len(stacks) == 0:
            return sequence, True, False, False

        for i, stack in reversed(list(enumerate(stacks))):
            if brackets_match(stack[-1], bracket):
                deleted = stack.pop()
                self.stems.add((deleted[1] + offset, index + offset))
                sequence = sequence[:deleted[1]] + \
                           deleted[0] + self.do_parse(sequence[deleted[1] + 1 : index], offset + deleted[1] + 1) + bracket \
                           + sequence[index + 1:]
                is_bulging = (min(deleted[1], deleted[3]) == 0) ^ (index == len(sequence) - 1)
                if i == len(stacks) - 1:
                    if len(stack) == 0:
                        stacks.pop(i)
                    return sequence, False, deleted[3] != sys.maxsize, is_bulging
                else:
                    if len(stack) == 0:
                        stacks.pop(i)
                    for j in range(i + 1, len(stacks)):
                        for k, bracket_tuple in enumerate(stacks[j]):
                            bracket_tuple = list(bracket_tuple)
                            bracket_tuple[3] = deleted[1]
                            stacks[j][k] = tuple(bracket_tuple)
                    return sequence, False, False, is_bulging
        return sequence, False, False, False

    def parse(self, sequence: str):
        self.reset()
        sequence = self.do_parse(sequence, 0)
        return sequence\
            .replace('(', 's').replace(')', 's') \
            .replace('[', 's').replace(']', 's') \
            .replace('{', 's').replace('}', 's')

    def reset(self):
        self.stems.clear()
        self.loops_type1.clear()
        self.loops_type2.clear()

    def do_parse(self, sequence: str, offset: int):
        if '.' not in sequence:
            return sequence
        stack_of_stacks = []
        is_wing = is_face_ecr = is_bulging = False
        #face_count = 0

        for i, ch in enumerate(sequence):
            if ch in open_brackets:
                to_stack(stack_of_stacks, ch, i)
            elif ch in close_brackets:
                sequence, is_wing1, is_face_ecr1, is_bulging1 = self.from_stack(sequence, stack_of_stacks, ch, i, offset)
                is_wing = is_wing1 if is_wing1 else is_wing
                #is_face_ecr = is_face_ecr1 if is_face_ecr1 else is_face_ecr
                is_face_ecr = is_face_ecr1 if is_face_ecr1 and len(stack_of_stacks) == 0 else is_face_ecr
                is_bulging = is_bulging1 if is_bulging1 else is_bulging
                # if not is_wing and len(stack_of_stacks) == 0:
                #     face_count += 1

        if len(stack_of_stacks) != 0:
            #is_wing = True
            is_wing = stack_of_stacks[-1][-1][3] == sys.maxsize

        face_count = self.define_face_count(sequence)

        return self.fill_loop_types(sequence, face_count, is_bulging, offset)\
            if self.classification == 0\
            else self.fill_intersections(sequence, is_wing, is_face_ecr, offset)

    def define_face_count(self, seq):
        for i, pair in enumerate(zip(seq, seq[1:])):
            if pair[0] in close_brackets and pair[1] in open_brackets\
                    and self.left_balanced(seq[:i + 1]) or self.right_balanced(seq[i + 1:]):
                return len(re.findall(r'[\[{(][^.]*[\]})]', seq[:i + 1])) + self.define_face_count(seq[i + 1:])

        return len(re.findall(r'[\[{(][^.]*[\]})]', seq))

    def left_balanced(self, sequence):
        return len(re.findall(r'\(', sequence)) <= len(re.findall(r'\)', sequence))\
                and len(re.findall(r'\[', sequence)) <= len(re.findall(r'\]', sequence))\
                and len(re.findall(r'{', sequence)) <= len(re.findall(r'}', sequence))\

    def right_balanced(self, sequence):
        return len(re.findall(r'\(', sequence)) >= len(re.findall(r'\)', sequence))\
                and len(re.findall(r'\[', sequence)) >= len(re.findall(r'\]', sequence))\
                and len(re.findall(r'{', sequence)) >= len(re.findall(r'}', sequence))\

    def fill_loop_types(self, sequence, face_count, is_bulging, offset):
        assert face_count >= 0
        if face_count == 0:
            self.fill_loop_address(offset, sequence, self.loops_type1, "hairpin")
            return sequence.replace('.', 'h')
        elif face_count == 1:
            if is_bulging:
                self.fill_loop_address(offset, sequence, self.loops_type1, "bulging")
                return sequence.replace('.', 'b')
            self.fill_loop_address(offset, sequence, self.loops_type1, "internal_loop")
            return sequence.replace('.', 'i')
        else:
            self.fill_loop_address(offset, sequence, self.loops_type1, "mult")
            return sequence.replace('.', 'm')

    def fill_intersections(self, sequence, is_wing, is_face_ecr, offset):
        if is_wing:
            self.fill_loop_address(offset, sequence, self.loops_type2, "pseudo")
            return sequence.replace('.', 'p')
        elif is_face_ecr:
            self.fill_loop_address(offset, sequence, self.loops_type2, "isolate")
            return sequence.replace('.', 'i')
        else:
            self.fill_loop_address(offset, sequence, self.loops_type2, "classical")
            return sequence.replace('.', 'c')

    def fill_loop_address(self, offset, sequence, res: dict, key: str):
        loop_accum = []
        for i in tuple(re.finditer(r'\.+', sequence)):
            loop_accum.append(tuple([x + offset for x in list(i.span())]))
        if len(loop_accum) > 0:
            if key not in res:
                res[key] = []
            res[key].append(loop_accum)
