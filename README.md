# BRANCHES

> Proyecto Web llevado a cabo con el Framework 'Django' en la Comisión 4 del Informatorio

**INTEGRANTES:**

- [louisrubin](https://github.com/louisrubin)
- [Marlenei](https://github.com/Marlenei)
- [MarcePerez](https://github.com/MarcePerez)
- [facuasan] No participó
- [juanir26] No participó

**Link al video:** https://youtu.be/fc_F4T8sPXE

# INSTALACION

- Crear archivo "local.py" dentro de la carpeta "settings" (Branches/Branches/settings)
- Pegar la estructura de código dada a continuación en "local.py" y colocar su base de datos local (MySQL)
- Hacer Migrate por consola: ***python manage.py migrate***

### Código para "local.py":

```
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": ""
    }
}
```

---> ¡ESTE PROYECTO ESTÁ CONFIGURADO CON MYSQL! 
(En caso de querer usar otro motor, instalar las extensiones y conexiones correspondientes a esa bd; Cambiando 'ENGINE')
12/2021
