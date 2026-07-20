# 📋 Práctica Tareas — Módulo Odoo

Módulo personalizado para Odoo 19: gestor simple de tareas, desarrollado como proyecto de práctica para aprender la arquitectura de desarrollo de Odoo (modelos, vistas, seguridad y despliegue).

> Desplegado y probado en un servidor propio (VPS) corriendo Odoo 19 como servicio systemd.

---

## ¿Qué hace?

Agrega una nueva app dentro de Odoo para gestionar tareas simples, con:

- Título, descripción y fecha límite
- Estado de completado (checkbox)
- Vista de lista y vista de formulario
- Menú propio dentro de Odoo ("Práctica Tareas")

---

## Stack técnico

| Componente | Tecnología |
|---|---|
| Framework | Odoo 19 |
| Lenguaje | Python 3 |
| ORM | Odoo ORM (`models.Model`) |
| Vistas | XML (Odoo view architecture) |
| Base de datos | PostgreSQL (motor interno de Odoo) |
| Despliegue | VPS Ubuntu + systemd |

---

## Estructura del módulo

```
practica_tareas/
├── __init__.py
├── __manifest__.py          ← Metadatos del módulo (nombre, versión, dependencias)
├── models/
│   ├── __init__.py
│   └── tarea.py              ← Modelo de datos (practica.tarea)
├── views/
│   └── tarea_views.xml       ← Vistas de lista, formulario, acción y menú
└── security/
    └── ir.model.access.csv   ← Permisos de acceso al modelo
```

---

## Modelo de datos

```python
class Tarea(models.Model):
    _name = 'practica.tarea'
    _description = 'Tarea de práctica'

    name = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha_limite = fields.Date(string='Fecha límite')
    hecho = fields.Boolean(string='Completada', default=False)
```

---

## Qué aprendí construyendo esto

- Estructura estándar de un módulo instalable de Odoo (`__manifest__.py`, dependencias, flags `installable`/`application`)
- Definición de modelos con el ORM propio de Odoo (`fields.Char`, `fields.Text`, `fields.Date`, `fields.Boolean`)
- Construcción de vistas en XML: `list`, `form`, `ir.actions.act_window` y `menuitem`
- Configuración de seguridad y permisos vía `ir.model.access.csv`
- Despliegue de Odoo en un VPS Ubuntu, gestionado como servicio con `systemd`
- Activación e instalación de módulos personalizados desde el modo desarrollador de Odoo

---

## Instalación

1. Clonar este repositorio dentro de la carpeta `custom-addons` de tu instancia de Odoo 19:
```bash
git clone <repo-url> /opt/odoo19/custom-addons/practica_tareas
```

2. Reiniciar el servicio de Odoo:
```bash
systemctl restart odoo19
```

3. Activar el modo desarrollador y actualizar la lista de apps desde la interfaz de Odoo.

4. Buscar "Práctica Tareas" en Apps y activar el módulo.

---

## Estado del proyecto

- ✅ Módulo instalable y funcional
- ✅ Probado en instancia real de Odoo 19 (VPS)
- ✅ CRUD completo operativo (crear, ver, editar tareas)
- 🚧 Proyecto de práctica — próximos pasos: agregar relaciones (many2one con usuarios), vista kanban, y validaciones personalizadas

---

## Autor

**Nashisilver (SilverWolf)**
Proyecto de práctica para aprender desarrollo de módulos Odoo.
