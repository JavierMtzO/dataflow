from Semantics.semantic_cube import types

DATATYPE_SIZE = 5000

INT_START = 0
FLOAT_START = INT_START + DATATYPE_SIZE * 4
CHAR_START = FLOAT_START + DATATYPE_SIZE * 4
BOOL_START = CHAR_START + DATATYPE_SIZE * 4

class VirtualMemory():
    """
    Class: VirtualMemory

    This class manages the allocation of virtual memory addresses for different data types in a simulated environment.

    Attributes:
    - global_int_range: A list representing the range of addresses for global integers.
    - global_int_counter: An integer representing the current counter for global integers.
    - constant_int_range: A list representing the range of addresses for constant integers.
    - constant_int_counter: An integer representing the current counter for constant integers.
    - local_int_range: A list representing the range of addresses for local integers.
    - local_int_init: An integer representing the initial counter for local integers.
    - local_int_parameter: An integer representing the counter for local integer parameters.
    - local_int_counter: An integer representing the current counter for local integers.
    - temp_int_range: A list representing the range of addresses for temporary integers.
    - temp_int_counter: An integer representing the current counter for temporary integers.
    - temp_int_init: An integer representing the initial counter for temporary integers.
    - global_float_range: A list representing the range of addresses for global floats.
    - global_float_counter: An integer representing the current counter for global floats.
    - constant_float_range: A list representing the range of addresses for constant floats.
    - constant_float_counter: An integer representing the current counter for constant floats.
    - local_float_range: A list representing the range of addresses for local floats.
    - local_float_init: An integer representing the initial counter for local floats.
    - local_float_parameter: An integer representing the counter for local float parameters.
    - local_float_counter: An integer representing the current counter for local floats.
    - temp_float_range: A list representing the range of addresses for temporary floats.
    - temp_float_counter: An integer representing the current counter for temporary floats.
    - temp_float_init: An integer representing the initial counter for temporary floats.
    - global_char_range: A list representing the range of addresses for global characters.
    - global_char_counter: An integer representing the current counter for global characters.
    - constant_char_range: A list representing the range of addresses for constant characters.
    - constant_char_counter: An integer representing the current counter for constant characters.
    - local_char_range: A list representing the range of addresses for local characters.
    - local_char_init: An integer representing the initial counter for local characters.
    - local_char_parameter: An integer representing the counter for local character parameters.
    - local_char_counter: An integer representing the current counter for local characters.
    - temp_char_range: A list representing the range of addresses for temporary characters.
    - temp_char_counter: An integer representing the current counter for temporary characters.
    - temp_char_init: An integer representing the initial counter for temporary characters.
    - global_bool_range: A list representing the range of addresses for global booleans.
    - global_bool_counter: An integer representing the current counter for global booleans.
    - constant_bool_range: A list representing the range of addresses for constant booleans.
    - constant_bool_counter: An integer representing the current counter for constant booleans.
    - local_bool_range: A list representing the range of addresses for local booleans.
    - local_bool_init: An integer representing the initial counter for local booleans.
    - local_bool_parameter: An integer representing the counter for local boolean parameters.
    - local_bool_counter: An integer representing the current counter for local booleans.
    - temp_bool_range: A list representing the range of addresses for temporary booleans.
    - temp_bool_counter: An integer representing the current counter for temporary booleans.
    - temp_bool_init: An integer representing the initial counter for temporary booleans.

    Methods:
    - assign_global_address_int: Assigns a global address for integers.
    - assign_global_address_float: Assigns a global address for floats.
    - assign_global_address_char: Assigns a global address for characters.
    - assign_global_address_bool: Assigns a global address for booleans.
    - restart_local_memory: Restarts the counters for local memory addresses.
    - restart_parameters: Restarts the counters for parameter addresses.
    - assign_constant_address_int: Assigns a constant address for integers.
    - assign_constant_address_float: Assigns a constant address for floats.
    - assign_constant_address_char: Assigns a constant address for characters.
    - assign_constant_address_bool: Assigns a constant address for booleans.
    - assign_temp_address_int: Assigns a temporary address for integers.
    - assign_temp_address_float: Assigns a temporary address for floats.
    - assign_temp_address_char: Assigns a temporary address for characters.
    - assign_temp_address_bool: Assigns a temporary address for booleans.
    - assign_local_address_int: Assigns a local address for integers.
    - assign_local_address_float: Assigns a local address for floats.
    - assign_local_address_char: Assigns a local address for characters.
    - assign_local_address_bool: Assigns a local address for booleans.
    - assign_parameter_address_int: Assigns a parameter address for integers.
    - assign_parameter_address_float: Assigns a parameter address for floats.
    - assign_parameter_address_char: Assigns a parameter address for characters.
    - assign_parameter_address_bool: Assigns a parameter address for booleans.
    - assign_virtual_address: Assigns a virtual address based on the data type, constancy, and scope.
    - assign_virtual_address_parameter: Assigns a virtual address for a parameter based on the data type.

    """

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
    global_float_range = [FLOAT_START, FLOAT_START + DATATYPE_SIZE - 1] #20,000 24,999
    global_float_counter = global_float_range[0]
    constant_float_range = [FLOAT_START + DATATYPE_SIZE, FLOAT_START + (DATATYPE_SIZE * 2) - 1] #25,000 29,999
    constant_float_counter = constant_float_range[0]
    local_float_range = [FLOAT_START + (DATATYPE_SIZE * 2), FLOAT_START + (DATATYPE_SIZE * 3) - 1] #30,000 34,999
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
    def assign_global_address_int(self, size):
        if self.global_int_counter > self.global_int_range[1]:
            raise Exception('Global integers exceeded')
        address = self.global_int_counter
        self.global_int_counter += 1 * size
        return address
    
    def assign_global_address_float(self, size):
        if self.global_float_counter > self.global_float_range[1]:
            raise Exception('Global floats exceeded')
        address = self.global_float_counter
        self.global_float_counter += 1 * size
        return address
    
    def assign_global_address_char(self, size):
        if self.global_char_counter > self.global_char_range[1]:
            raise Exception('Global chars exceeded')
        address = self.global_char_counter
        self.global_char_counter += 1 * size
        return address
    
    def assign_global_address_bool(self, size):
        if self.global_bool_counter > self.global_bool_range[1]:
            raise Exception('Global booleans exceeded')
        address = self.global_bool_counter
        self.global_bool_counter += 1 * size
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
    def assign_local_address_int(self, size):
        if self.local_int_counter > self.local_int_range[1]:
            raise Exception('Local ints exceeded')
        address = self.local_int_counter
        self.local_int_counter += 1 * size
        return address
    
    def assign_local_address_float(self, size):
        if self.local_float_counter > self.local_float_range[1]:
            raise Exception('Local floats exceeded')
        address = self.local_float_counter
        self.local_float_counter += 1 * size
        return address
    
    def assign_local_address_char(self, size):
        if self.local_char_counter > self.local_char_range[1]:
            raise Exception('Local chars exceeded')
        address = self.local_char_counter
        self.local_char_counter += 1 * size
        return address
    
    def assign_local_address_bool(self, size):
        if self.local_bool_counter > self.local_bool_range[1]:
            raise Exception('Local booleans exceeded')
        address = self.local_bool_counter
        self.local_bool_counter += 1 * size
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
    
    
    def assign_virtual_address(self, type: str, is_const: bool = False, is_global: bool = False, is_temp: bool = False, size:int = 1) -> int:
        if type == types['int']:
            if is_const:
                return self.assign_constant_address_int()
            elif is_temp:
                return self.assign_temp_address_int()
            elif is_global:
                return self.assign_global_address_int(size)
            else:
                return self.assign_local_address_int(size)
        elif type == types['float']:
            if is_const:
                return self.assign_constant_address_float()
            elif is_temp:
                return self.assign_temp_address_float()
            elif is_global:
                return self.assign_global_address_float(size)
            else:
                return self.assign_local_address_float(size)
        elif type == types['char']:
            if is_const:
                return self.assign_constant_address_char()
            elif is_temp:
                return self.assign_temp_address_char()
            elif is_global:
                return self.assign_global_address_char(size)
            else:
                return self.assign_local_address_char(size)
        elif type == types['bool']:
            if is_const:
                return self.assign_constant_address_bool()
            elif is_temp:
                return self.assign_temp_address_bool()
            elif is_global:
                return self.assign_global_address_bool(size)
            else:
                return self.assign_local_address_bool(size)
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


