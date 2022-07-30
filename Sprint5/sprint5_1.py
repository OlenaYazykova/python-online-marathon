import re


def valid_email(email_address):
    pattern=r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    try:
        if not re.fullmatch(pattern, email_address):
            raise ValueError('Email is not valid')
        return 'Email is valid'
    except ValueError as e:
        return e


print(valid_email('trafik@ukr.tel.com'))
print(valid_email('trafik@ukr_tel.com'))
print(valid_email('tra@fik@ukr.com'))
print(valid_email('ownsite@our.c0m'))
print(valid_email("example@source.ua"))
