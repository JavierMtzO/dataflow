from Semantics.semantic_cube import types

DATATYPE_SIZE = 5000

INT_START = 0
FLOAT_START = INT_START + DATATYPE_SIZE * 4
CHAR_START = FLOAT_START + DATATYPE_SIZE * 4
BOOL_START = CHAR_START + DATATYPE_SIZE * 4

class VirtualMemory():

    # Int ranges
    global_int_range = [INT_START, INT_START + DATATYPE_SIZE - 1] # 0 4,999
    global_int_counter = global_int_range[0] # 0
    constant_int_range = [INT_START + DATATYPE_SIZE, INT_START + (DATATYPE_SIZE * 2) - 1] #5,000 9,999
    constant_int_counter = constant_int_range[0] # 5,000
    local_int_range = [INT_START + (DATATYPE_SIZE * 2), INT_START + (DATATYPE_SIZE * 3) - 1] #10,000 14,999
    local_int_init = local_int_range[0] # 10,000
    local_int_parameter = local_int_range[0] # 10,000
    local_int_counter = local_int_range[0] # 10,000
    temp_int_range = [INT_START + (DATATYPE_SIZE * 3), INT_START + (DATATYPE_SIZE * 4) - 1]#15,000 19,999
    temp_int_counter = temp_int_range[0] # 15,000
    temp_int_init = temp_int_range[0]

    # Float ranges
    global_float_range = [FLOAT_START, FLOAT_START + DATATYPE_SIZE - 1]
    global_float_counter = global_float_range[0]
    constant_float_range = [FLOAT_START + DATATYPE_SIZE, FLOAT_START + (DATATYPE_SIZE * 2) - 1]
    constant_float_counter = constant_float_range[0]
    local_float_range = [FLOAT_START + (DATATYPE_SIZE * 2), FLOAT_START + (DATATYPE_SIZE * 3) - 1]
    local_float_init = local_float_range[0]
    local_float_parameter = local_float_range[0]
    local_float_counter = local_float_range[0]
    temp_float_range = [FLOAT_START + (DATATYPE_SIZE * 3), FLOAT_START + (DATATYPE_SIZE * 4) - 1]
    temp_float_counter = temp_float_range[0]
    temp_float_init = temp_float_range[0] 

    # Char ranges
    global_char_range = [CHAR_START, CHAR_START + DATATYPE_SIZE - 1]
    global_char_counter = global_char_range[0] 
    constant_char_range = [CHAR_START + DATATYPE_SIZE, CHAR_START + (DATATYPE_SIZE * 2) - 1]
    constant_char_counter = constant_char_range[0] 
    local_char_range = [CHAR_START + (DATATYPE_SIZE * 2), CHAR_START + (DATATYPE_SIZE * 3) - 1]
    local_char_init = local_char_range[0]
    local_char_parameter = local_char_range[0]
    local_char_counter = local_char_range[0] 
    temp_char_range = [CHAR_START + (DATATYPE_SIZE * 3), CHAR_START + (DATATYPE_SIZE * 4) - 1]
    temp_char_counter = temp_char_range[0]
    temp_char_init = temp_char_range[0]

    # Bool ranges
    global_bool_range = [BOOL_START, BOOL_START + DATATYPE_SIZE - 1]
    global_bool_counter = global_bool_range[0] 
    constant_bool_range = [BOOL_START + DATATYPE_SIZE, BOOL_START + DATATYPE_SIZE + 1] # Boolean constants are only true or false
    constant_bool_counter = constant_bool_range[0] 
    local_bool_range = [BOOL_START + (DATATYPE_SIZE * 2), BOOL_START + (DATATYPE_SIZE * 3) - 1]
    local_bool_init = local_bool_range[0] 
    local_bool_parameter = local_bool_range[0]
    local_bool_counter = local_bool_range[0] 
    temp_bool_range = [ BOOL_START + (DATATYPE_SIZE * 3),  BOOL_START + (DATATYPE_SIZE * 4) - 1]
    temp_bool_counter = temp_bool_range[0]
    temp_bool_init = temp_bool_range[0]

    # Assign global variable addresses
    def assign_global_address_int(self):
        if self.global_int_counter > self.global_int_range[1]:
            raise Exception('Global integers exceeded')
        address = self.global_int_counter
        self.global_int_counter += 1
        return address
    
    def assign_global_address_float(self):
        if self.global_float_counter > self.global_float_range[1]:
            raise Exception('Global floats exceeded')
        address = self.global_float_counter
        self.global_float_counter += 1
        return address
    
    def assign_global_address_char(self):
        if self.global_char_counter > self.global_char_range[1]:
            raise Exception('Global chars exceeded')
        address = self.global_char_counter
        self.global_char_counter += 1
        return address
    
    def assign_global_address_bool(self):
        if self.global_bool_counter > self.global_bool_range[1]:
            raise Exception('Global booleans exceeded')
        address = self.global_bool_counter
        self.global_bool_counter += 1
        return address
    
    # Restart local memory
    def restart_local_memory(self):
        self.local_int_counter = self.local_int_init
        self.local_float_counter = self.local_float_init
        self.local_char_counter = self.local_char_init
        self.local_bool_counter = self.local_bool_init

        self.temp_int_counter = self.temp_int_init
        self.temp_float_counter = self.temp_float_init
        self.temp_char_counter = self.temp_char_init
        self.temp_bool_counter = self.temp_bool_init

    def restart_parameters(self):
        self.local_int_parameter = self.local_int_init
        self.local_float_parameter = self.local_float_init
        self.local_char_parameter = self.local_char_init
        self.local_bool_parameter = self.local_bool_init
    
    # Assign constant addresses
    def assign_constant_address_int(self):
        if self.constant_int_counter > self.constant_int_range[1]:
            raise Exception('Constant ints exceeded')
        address = self.constant_int_counter
        self.constant_int_counter += 1
        return address
    
    def assign_constant_address_float(self):
        if self.constant_float_counter > self.constant_float_range[1]:
            raise Exception('Constant floats exceeded')
        address = self.constant_float_counter
        self.constant_float_counter += 1
        return address
    
    def assign_constant_address_char(self):
        if self.constant_char_counter > self.constant_char_range[1]:
            raise Exception('Constant chars exceeded')
        address = self.constant_char_counter
        self.constant_char_counter += 1
        return address
    
    def assign_constant_address_bool(self):
        if self.constant_bool_counter > self.constant_bool_range[1]:
            raise Exception('Constant booleans exceeded')
        address = self.constant_bool_counter
        self.constant_bool_counter += 1
        return address
    
    # Assign temporal addresses
    def assign_temp_address_int(self):
        if self.temp_int_counter > self.temp_int_range[1]:
            raise Exception('Temporal ints exceeded')
        address = self.temp_int_counter
        self.temp_int_counter += 1
        return address
    
    def assign_temp_address_float(self):
        if self.temp_float_counter > self.temp_float_range[1]:
            raise Exception('Temporal floats exceeded')
        address = self.temp_float_counter
        self.temp_float_counter += 1
        return address
    
    def assign_temp_address_char(self):
        if self.temp_char_counter > self.temp_char_range[1]:
            raise Exception('Temporal chars exceeded')
        address = self.temp_char_counter
        self.temp_char_counter += 1
        return address
    
    def assign_temp_address_bool(self):
        if self.temp_bool_counter > self.temp_bool_range[1]:
            raise Exception('Temporal booleans exceeded')
        address = self.temp_bool_counter
        self.temp_bool_counter += 1
        return address
    
    # Assign local addresses
    def assign_local_address_int(self):
        if self.local_int_counter > self.local_int_range[1]:
            raise Exception('Local ints exceeded')
        address = self.local_int_counter
        self.local_int_counter += 1
        return address
    
    def assign_local_address_float(self):
        if self.local_float_counter > self.local_float_range[1]:
            raise Exception('Local floats exceeded')
        address = self.local_float_counter
        self.local_float_counter += 1
        return address
    
    def assign_local_address_char(self):
        if self.local_char_counter > self.local_char_range[1]:
            raise Exception('Local chars exceeded')
        address = self.local_char_counter
        self.local_char_counter += 1
        return address
    
    def assign_local_address_bool(self):
        if self.local_bool_counter > self.local_bool_range[1]:
            raise Exception('Local booleans exceeded')
        address = self.local_bool_counter
        self.local_bool_counter += 1
        return address
    
    # Assign parameters
    def assign_parameter_address_int(self):
        address = self.local_int_parameter
        self.local_int_parameter += 1
        return address
    
    def assign_parameter_address_float(self):
        address = self.local_float_parameter
        self.local_float_parameter += 1
        return address
    
    def assign_parameter_address_char(self):
        address = self.local_char_parameter
        self.local_char_parameter += 1
        return address
    
    def assign_parameter_address_bool(self):
        address = self.local_bool_parameter
        self.local_bool_parameter += 1
        return address
    
    
    def assign_virtual_address(self, type: str, is_const: bool = False, is_global: bool = False, is_temp: bool = False) -> int:
        if type == types['int']:
            if is_const:
                return self.assign_constant_address_int()
            elif is_temp:
                return self.assign_temp_address_int()
            elif is_global:
                return self.assign_global_address_int()
            else:
                return self.assign_local_address_int()
        elif type == types['float']:
            if is_const:
                return self.assign_constant_address_float()
            elif is_temp:
                return self.assign_temp_address_float()
            elif is_global:
                return self.assign_global_address_float()
            else:
                return self.assign_local_address_float()
        elif type == types['char']:
            if is_const:
                return self.assign_constant_address_char()
            elif is_temp:
                return self.assign_temp_address_char()
            elif is_global:
                return self.assign_global_address_char()
            else:
                return self.assign_local_address_char()
        elif type == types['bool']:
            if is_const:
                return self.assign_constant_address_bool()
            elif is_temp:
                return self.assign_temp_address_bool()
            elif is_global:
                return self.assign_global_address_bool()
            else:
                return self.assign_local_address_bool()
        else:
            raise Exception(f'Type: {type} was not recognized in virtual memory')  
    
    def assign_virtual_address_parameter(self, type: str) -> int:
        if type == types['int']:
            return self.assign_parameter_address_int()
        if type == types['float']:
            return self.assign_parameter_address_float()
        if type == types['char']:
            return self.assign_parameter_address_char()
        if type == types['bool']:
            return self.assign_parameter_address_bool()


