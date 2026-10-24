# Estándares de API

Responsable: Grupo 3 · Arquitectura

## API del Sistema de Personal (puerto 5001)
| Servicio | Devuelve |
|---|---|
| `GET /areas` | Lista de áreas |
| `GET /trabajadores` | Lista de trabajadores: código, nombre, área, cargo, jefe, rol (`colaborador`, `gestor`, `jefe`) y estado (`ACTIVO`, `CESADO`) |
| `GET /trabajadores/<codigo>` | Un trabajador, o error 404 |

## Reglas para todas las APIs
- Respuestas en JSON.
- Todo error devuelve `{ "codigo": "...", "mensaje_usuario": "..." }`. El `mensaje_usuario` se muestra tal cual al trabajador: lenguaje claro, sin detalles internos.
- Cambios que rompan un servicio existente requieren nueva versión y aviso a las áreas afectadas.
