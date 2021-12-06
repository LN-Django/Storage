from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_higher_or_equals_one(value):
    if value < 1:
        raise ValidationError(
            _('%(value)s must not be lower than one'), params={'value': value})
