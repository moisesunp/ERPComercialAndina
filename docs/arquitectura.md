# Arquitectura vigente de Comercial Andina

Responsable: Grupo 3 · Arquitectura

| Componente | Situación |
|---|---|
| Sistema de Personal | Sistema interno. Fuente oficial de trabajadores, áreas, cargos y jefes. Expone API REST de solo lectura (simulada en `erp-personal/`). |
| Identidad corporativa | Cada trabajador tiene una cuenta con contraseña. En el curso se simula con el código de trabajador. |
| Sistemas de terceros | Pueden tener su propia base de datos para sus datos de negocio, pero **no copian** datos de personal como fuente oficial: los consultan a la API. |

## Principios obligatorios
1. Los datos de trabajadores solo se leen del Sistema de Personal.
2. Ningún sistema de terceros escribe en el Sistema de Personal.
3. Las integraciones siguen `docs/estandares-api.md`.
4. Todo cambio en producción tiene plan de reversión.
