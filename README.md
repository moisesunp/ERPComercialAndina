# Mesa de Trámites · Comercial Andina

**Comercial Andina** es una cadena comercial del norte del Perú con unos 1 500 trabajadores y una Gerencia de TI de más de 80 personas. Contrató a **NovaSoft** para desarrollar **Mesa de Trámites**: un sistema interno para registrar y dar seguimiento a los trámites de los trabajadores (vacaciones, constancias, reembolsos, compras menores y accesos a sistemas).

- **Estado:** NovaSoft entregó la **v0.1**, pendiente de pruebas y aceptación.
- **Coordinación del proyecto (caso, áreas, reglas, calendario y evaluación):** [`seguimiento/README.md`](seguimiento/README.md)

## Requerimiento

1. El trabajador inicia sesión con su cuenta corporativa.
2. Registra un trámite; el sistema lo asigna a un gestor del área que lo atiende.
3. El solicitante y el responsable ven el estado y la fecha límite.
4. El responsable cambia el estado: en proceso, atendido o rechazado. Queda historial.
5. La Gerencia de Administración ve qué trabajadores destacan en la atención de trámites.

**Para qué:** hoy los trámites se piden por correo o WhatsApp, nadie sabe en qué estado están y no hay forma de saber qué áreas se demoran.

## Dos sistemas

| Carpeta | Sistema | Dueño | Base de datos |
|---|---|---|---|
| `erp-personal/` | **Sistema de Personal** de Comercial Andina (ya existe). Expone una API de solo lectura con áreas y trabajadores. | Grupo 4 · Desarrollo interno | SQLite `personal.db` (se crea con `datos.sql`) |
| `tramites/` | **Mesa de Trámites** v0.1 de NovaSoft. Su backend (`app.py`) consulta la API de Personal; su pantalla está en `static/index.html`. | Grupo 13 · Backend y Grupo 12 · Frontend | SQLite `tramites.db` |

## Cómo ejecutarlo

**Opción A · En el navegador, sin instalar nada:** botón **Code → Codespaces → Create codespace on main**. En la terminal:

```
pip install -r requirements.txt
python iniciar.py
```
Abrir el puerto 5000 cuando el Codespace lo ofrezca.

**Opción B · En tu computadora** (Python 3.10 o superior): los mismos dos comandos y abrir `http://localhost:5000`.

Códigos de prueba: `T015` (vendedor), `T013` (ejecutivo comercial), `T003` (gestora de RRHH), `T010` (soporte TI), `T001` (Gerente de Administración). Para reiniciar los datos, borrar `personal.db` y `tramites.db`.

## Reglas de trabajo

- Nadie modifica `main` directamente: todo cambio entra por **Pull Request** revisado por al menos un área del cliente.
- El proveedor **no puede modificar** `erp-personal/`. Si necesita algo nuevo de esa API, lo pide al Grupo 4 mediante un Issue.
- Cada defecto se registra como **Issue** con la etiqueta `defecto`.
