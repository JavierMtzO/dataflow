from Memories.virtual_memory import DATATYPE_SIZE, VirtualMemory
import ast

class Runtime_Memory:

    def __init__(self, resources:str, constant_dict:dict) -> None:
        # [g_i, g_f, g_c, g_b, l_i, l_f, l_c, l_b, c_i, c_f, c_c, c_b, t_i, t_f, t_c, t_b]   0 - 15
        # Convert String to list
        # print(resources)
        self.resources = ast.literal_eval(resources)
        self.constant_dict = constant_dict
        self.define_global_memory()
        
        # print(f'global_ints_memory: {len(self.global_ints_memory)}')
        # print(f'global_floats_memory: {len(self.global_floats_memory)}')
        # print(f'global_chars_memory: {len(self.global_chars_memory)}')
        # print(f'global_bools_memory: {len(self.global_bools_memory)}')

        # print(f'local_ints_memory: {len(self.local_ints_memory)}')
        # print(f'local_floats_memory: {len(self.local_floats_memory)}')
        # print(f'local_chars_memory: {len(self.local_chars_memory)}')
        # print(f'local_bools_memory: {len(self.local_bools_memory)}')

        # print(f'constant_ints_memory: {len(self.constant_ints_memory)}')
        # print(f'constant_floats_memory: {len(self.constant_floats_memory)}')
        # print(f'constant_chars_memory: {len(self.constant_chars_memory)}')
        # print(f'constant_bools_memory: {len(self.constant_bools_memory)}')

        # print(f'temporal_ints_memory: {len(self.temporal_ints_memory)}')
        # print(f'temporal_floats_memory: {len(self.temporal_floats_memory)}')
        # print(f'temporal_chars_memory: {len(self.temporal_chars_memory)}')
        # print(f'temporal_bools_memory: {len(self.temporal_bools_memory)}')
        
    def define_global_memory(self):
        self.global_ints_memory = self.generate_memory_segment(self.resources[0])
        self.global_floats_memory = self.generate_memory_segment(self.resources[1])
        self.global_chars_memory = self.generate_memory_segment(self.resources[2])
        self.global_bools_memory = self.generate_memory_segment(self.resources[3])

        self.local_ints_memory = self.generate_memory_segment(self.resources[4])
        self.local_floats_memory = self.generate_memory_segment(self.resources[5])
        self.local_chars_memory = self.generate_memory_segment(self.resources[6])
        self.local_bools_memory = self.generate_memory_segment(self.resources[7])

        self.constant_ints_memory = self.generate_memory_segment(self.resources[8])
        self.constant_floats_memory = self.generate_memory_segment(self.resources[9])
        self.constant_chars_memory = self.generate_memory_segment(self.resources[10])
        self.constant_bools_memory = self.generate_memory_segment(self.resources[11])

        self.temporal_ints_memory = self.generate_memory_segment(self.resources[12])
        self.temporal_floats_memory = self.generate_memory_segment(self.resources[13])
        self.temporal_chars_memory = self.generate_memory_segment(self.resources[14])
        self.temporal_bools_memory = self.generate_memory_segment(self.resources[15])
    
    def generate_memory_segment(self, size: int):
        return [None] * size
    
    def return_content(self, virtual_address: int) -> any:
        memory_categorizer = int(virtual_address / DATATYPE_SIZE)

        # INTS
        if memory_categorizer == 0:
            return self.global_ints_memory[virtual_address]
        if memory_categorizer == 1:
            return int(self.constant_dict[virtual_address])
        if memory_categorizer == 2:
            return self.local_ints_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        if memory_categorizer == 3:
            return self.temporal_ints_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        
        # FLOATS
        if memory_categorizer == 4:
            return self.global_floats_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        if memory_categorizer == 5:
            return float(self.constant_dict[virtual_address])
        if memory_categorizer == 6:
            return self.local_floats_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        if memory_categorizer == 7:
            return self.temporal_floats_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        
        # CHARS
        if memory_categorizer == 8:
            return self.global_floats_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        if memory_categorizer == 9:
            return str(self.constant_dict[virtual_address])
        if memory_categorizer == 10:
            return self.local_floats_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        if memory_categorizer == 11:
            return self.temporal_floats_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        
        # BOOLEANS
        if memory_categorizer == 12:
            return self.global_bools_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        if memory_categorizer == 13:
            return bool(self.constant_dict[virtual_address])
        if memory_categorizer == 14:
            return self.local_bools_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]
        if memory_categorizer == 15:
            return self.temporal_bools_memory[virtual_address - (DATATYPE_SIZE * memory_categorizer)]

    
    def assign_content_value(self, left_virtual_address: int, result:any):
        memory_categorizer = int(left_virtual_address / DATATYPE_SIZE)

        # INTS
        if memory_categorizer == 0:
            self.global_ints_memory[left_virtual_address] = result
        if memory_categorizer == 1:
            pass # You can't assign constant to constant
        if memory_categorizer == 2:
            self.local_ints_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        if memory_categorizer == 3:
            self.temporal_ints_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        
        # FLOATS
        if memory_categorizer == 4:
            self.global_floats_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        if memory_categorizer == 5:
            pass # You can't assign constant to constant
        if memory_categorizer == 6:
            self.local_floats_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        if memory_categorizer == 7:
            self.temporal_floats_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result

        # CHARS
        if memory_categorizer == 8:
            self.global_chars_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        if memory_categorizer == 9:
            pass # You can't assign constant to constant
        if memory_categorizer == 10:
            self.local_chars_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        if memory_categorizer == 11:
            self.temporal_chars_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        
        # BOOLEANS
        if memory_categorizer == 12:
            self.global_bools_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        if memory_categorizer == 13:
            pass # You can't assign constant to constant
        if memory_categorizer == 14:
            self.local_bools_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
        if memory_categorizer == 15:
            self.temporal_bools_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = result
    
    def assign_content(self, left_virtual_address: int, right_value: any):
        memory_categorizer = int(left_virtual_address / DATATYPE_SIZE)

        # INTS
        if memory_categorizer == 0:
            self.global_ints_memory[left_virtual_address] = right_value
        if memory_categorizer == 1:
            pass
        if memory_categorizer == 2:
            self.local_ints_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        if memory_categorizer == 3:
            self.temporal_ints_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        
        # FLOATS
        if memory_categorizer == 4:
            self.global_floats_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        if memory_categorizer == 5:
            pass
        if memory_categorizer == 6:
            self.local_floats_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        if memory_categorizer == 7:
            self.temporal_floats_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        
        # CHARS
        if memory_categorizer == 8:
            self.global_chars_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        if memory_categorizer == 9:
            pass
        if memory_categorizer == 10:
            self.local_chars_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        if memory_categorizer == 11:
            self.temporal_chars_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        
        # BOOLEANS
        if memory_categorizer == 12:
            self.global_bools_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        if memory_categorizer == 13:
            pass
        if memory_categorizer == 14:
            self.local_bools_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value
        if memory_categorizer == 15:
            self.temporal_bools_memory[left_virtual_address - (DATATYPE_SIZE * memory_categorizer)] = right_value

    


    
