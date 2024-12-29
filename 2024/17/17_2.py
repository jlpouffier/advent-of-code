# That's a fail. Not working yet...
import time
import itertools

class Computer:
    def __init__(self, A, B, C,  program):
        self.A = A
        self.B = B
        self.C = C
        self.initial_A = A
        self.initial_B = B
        self.initial_C = C
        self.program = program
        self.instruction_pointer = 0
        self.output = []
        self.halt = False
    
    def __repr__(self):
        strA = f"Register A: {self.A}"
        strB = f"Register B: {self.B}"
        strC = f"Register C: {self.C}"
        strIP = f"Instruction pointer: {self.instruction_pointer}"
        strOutput = f"Output: {','.join(str(char) for char in self.output)}"
        return '\n'.join(str for str in [strA, strB, strC, strIP, strOutput])
        
    def get_opcode(self):
        if 0 <= self.instruction_pointer < len(self.program):
            return self.program[self.instruction_pointer]
        else: 
            return -1
        
    def get_literal_operand(self):
        return self.program[self.instruction_pointer + 1]
    
    def get_combo_operand(self):
        literal_operand = self.get_literal_operand()
        if 0 <= literal_operand <= 3:
            return literal_operand
        elif literal_operand == 4:
            return self.A
        elif literal_operand == 5:
            return self.B
        elif literal_operand == 6:
            return self.C
        else:
            raise ValueError("Reserved and should not appear in valid programs")
    
    def run_program(self):
        while not self.halt:
            self.run_instruction()

    # def debug(self):
    #     A_coefficients = [0 for i in range(len(self.program))]
    #     for i in range(len(self.program)):
    #         print(f'Trying to match this program part: {self.program[-i-1:]}')
    #         for j in range(8):
    #             A_coefficients[len(self.program) - 1 - i] = j
    #             print(A_coefficients)
    #             tested_A = sum(coef * (8 ** exp) for exp, coef in enumerate(reversed(A_coefficients)))
    #             print(tested_A)
    #             self.reset()
    #             self.A = tested_A
    #             self.run_program()
    #             print(self.output)
    #             if self.program[-i-1:] == self.output[-i-1:]:
    #                 print("MATCH!")
    #                 break

    def test_debug_index(self, A_coefficients, index):
        print(A_coefficients)
        tested_A = sum(coef * (8 ** exp) for exp, coef in enumerate(reversed(A_coefficients)))
        self.reset()
        self.A = tested_A
        self.run_program()
        return self.program[-index-1] == self.output[-index-1]
    
    def debug_backtrack(self, A_coefficients, index = 0):
        
        if index == len(A_coefficients):
            return True
        
        for j in range(8):
            A_coefficients[index] = j

            if self.test_debug_index(A_coefficients, index):
                if self.debug_backtrack(A_coefficients, index+1):
                    return True
        
        A_coefficients[index] = 0
        return False

    def debug(self, index = 0):
        A_coefficients = [0] * 16
        if self.debug_backtrack(A_coefficients):
            tested_A = sum(coef * (8 ** exp) for exp, coef in enumerate(reversed(A_coefficients)))
            print("Found a solution:", tested_A)
        else:
            print("No solution was found.")
            

    def reset(self):
        self.A = self.initial_A
        self.B = self.initial_B
        self.C = self.initial_C
        self.output = []
        self.instruction_pointer = 0
        self.halt = False
    
    def run_instruction(self):
        opcode = self.get_opcode()
        # adv instruction
        if opcode == 0:
            combo_operand = self.get_combo_operand()
            numerator = self.A
            denominator = 2 ** combo_operand
            self.A = numerator // denominator
            self.instruction_pointer += 2

        # bxl instruction
        elif opcode == 1:
            literal_operand = self.get_literal_operand()
            self.B = self.B ^ literal_operand
            self.instruction_pointer += 2

        # bst instruction
        elif opcode == 2:
            combo_operand = self.get_combo_operand()
            self.B = combo_operand % 8
            self.instruction_pointer += 2

        # jnz instruction
        elif opcode == 3:
            if self.A != 0:
                self.instruction_pointer = self.get_literal_operand()
            else:
                self.instruction_pointer += 2

        # bxc instruction
        elif opcode == 4:
            self.B = self.B ^ self.C
            self.instruction_pointer += 2

        # out instruction
        elif opcode == 5:
            combo_operand = self.get_combo_operand()
            self.output.append(combo_operand % 8)
            self.instruction_pointer += 2

        # bdv
        elif opcode == 6:
            combo_operand = self.get_combo_operand()
            numerator = self.A
            denominator = 2 ** combo_operand
            self.B = numerator // denominator
            self.instruction_pointer += 2

        # cdv
        elif opcode == 7:
            combo_operand = self.get_combo_operand()
            numerator = self.A
            denominator = 2 ** combo_operand
            self.C = numerator // denominator
            self.instruction_pointer += 2

        # halt
        elif opcode == -1:
            self.halt = True

        else:
            raise ValueError("Unknown Opcode")
            
part1_start_time = time.time()

A = 0
B = 0
C = 0
program = [2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0]

computer = Computer(A,B,C,program)
computer.debug()

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")

