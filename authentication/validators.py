from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'The password must contain at least one letter',
                code='password_no_letter'
            )
    
    def get_help_text(self):
        return "Your password must contain at least one letter."
    

class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'The password must contain at least one number',
                code='password_no_number'
            )
    
    def get_help_text(self):
        return "Your password must contain at least one number."