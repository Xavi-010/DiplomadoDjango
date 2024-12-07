from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 5 != 0 :
        raise ValidationError(
            '%(value)s no es un multiplo de 5',
            params={'value':value},
        )
    
def validar_longitud_nombre(value):
    if len(value) < 3 or len(value) > 100:
        raise ValidationError(
            'El nombre %(value)s debe tener entre 3 y 100 caracteres',
            params={'value': value},
        )
    
def validation_categoria(value):
    if value == 'No permitido':
        raise ValidationError('No es una opcion permitida')
    
def validar_nombre(value):
    if value == 'Escoba':
        raise ValidationError(
            '%(value)s no es un texto permitido',
            params={'value':value}
        )