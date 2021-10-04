SECRET_KEY = 'django-insecure-^pu9tenrzouluy(e%%hi7c!p9r5+_x-t9$_nqv1t_2j0s&@&63'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Jakefromstatefarm1!@!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}