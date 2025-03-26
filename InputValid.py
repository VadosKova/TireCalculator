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

