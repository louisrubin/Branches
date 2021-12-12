
# BRANCHES

> Proyecto Web llevado a cabo con el Framework 'Django' en la Comisión 4 del Informatorio

**INTEGRANTES:**

- [louisrubin](https://github.com/louisrubin)
- [Marlenei](https://github.com/Marlenei)
- [MarcePerez](https://github.com/MarcePerez)
- [facuasan](https://github.com/facuasan)
- [juanir26](https://github.com/juanir26)

**Link al video:** (no disponible aún)

# INSTALACION
- Para correr el proyecto deben crear el archivo "local.py" dentro de la carpeta "settings", copiando la siguiente estructura de código y colocando su correspondiente base de datos local.
- Luego en "manage.py" en la linea 9 agregar ".local" seguido de "Branches.settings"
y listo :D
- Código para "local.py":

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
(En caso de querer usar otro motor, instalar las extensiones y conexiones correspondientes a esa bd.)
12/2021