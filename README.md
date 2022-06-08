# django_ilus_skeleton

## Skeleton django project with some security inputs

- A custom user is implemented
  - Login
  - Logout
  - Change password
- MFA factor is implemented
- Quality password is implemented (also control if is it pwned)
- 12 factor with the settings (.env)

### To do for Yubikey function on "python manage.py shell"
> from otp_yubikey.models import ValidationService
> 
> ValidationService.objects.create(
> 
> ... ... ... ... name='default', use_ssl=True, param_sl='', param_timeout=''
> 
> )
> 
><ValidationService: default>

## Work to do for the next steps

- production side finalise
- session (geoip to introduce)
- meta
- cookiecutter production
