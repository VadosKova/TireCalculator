class InputValid:
    def validate_input(self, value, value_type):
        try:
            if value_type == 'int':
                int(value)
            elif value_type == 'float':
                float(value)
            return True
        except ValueError:
            return False

    def get_valid_input(self, prompt, value_type):
        while True:
            value = input(prompt)
            if self.validate_input(value, value_type):
                if value_type == 'int':
                    return int(value)
                elif value_type == 'float':
                    return float(value)
            else:
                print("Error")