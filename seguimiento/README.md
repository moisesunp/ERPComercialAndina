# Proyecto Mesa de Trámites · Seguimiento y coordinación

Carpeta de trabajo de **Comercial Andina** (cliente) y **NovaSoft** (proveedor). Aquí se registran las solicitudes entre áreas, las decisiones y el expediente de cada grupo.

## 1. Situación

Comercial Andina (cadena comercial del norte, unos 1 500 trabajadores, Gerencia de TI de más de 80 personas) contrató a NovaSoft para desarrollar **Mesa de Trámites**, un sistema interno de seguimiento de trámites. Sus programadores están ocupados con otros sistemas, pero deben mantener la API del **Sistema de Personal**, que el sistema nuevo necesita.

NovaSoft entregó la **v0.1** en la carpeta `tramites/`; el Sistema de Personal está en `erp-personal/`. Ahora el cliente debe probarla, exigir lo que necesita y decidir si el proyecto puede continuar. Leer primero la carpeta `seguimiento/origen/`.

> Cada grupo representa un área con 3 roles. En una empresa real, cada área tendría más personas.

## 2. Áreas y roles

En grupos de 2, una persona asume dos roles. En grupos de 4, dos personas comparten un rol. Detalle en `seguimiento/origen/organigramas.md`.

| Grupo | Empresa | Área |
|---|---|---|
| 1 | Comercial Andina | Dirección de TI |
| 2 | Comercial Andina | Producto (área usuaria: Administración) |
| 3 | Comercial Andina | Arquitectura |
| 4 | Comercial Andina | Desarrollo interno (Sistema de Personal) |
| 5 | Comercial Andina | Ciberseguridad |
| 6 | Comercial Andina | Infraestructura y Cloud |
| 7 | Comercial Andina | QA y aceptación |
| 8 | Comercial Andina | Soporte / Service Desk |
| 9 | Comercial Andina | Datos |
| 10 | Comercial Andina | Proyecto y proveedores |
| 11 | NovaSoft | Jefatura de proyecto |
| 12 | NovaSoft | Frontend |
| 13 | NovaSoft | Backend |
| 14 | NovaSoft | QA y despliegue |

Gerencia General, Finanzas y RRHH las representa el docente. Solo se les escribe mediante un Issue con la etiqueta `gerencia`, usando la plantilla de escalamiento.

## 3. Reglas de interacción

- Toda solicitud entre áreas es un **Issue** con la plantilla *Solicitud entre áreas* y la etiqueta del área destinataria (`g01` … `g14`).
- **Acuse en 24 h** ("recibido, respondo el día X") y **respuesta completa en 48 h**. Si no hay respuesta, se escala con la plantilla de escalamiento.
- Los defectos del programa se registran como Issue con la etiqueta `defecto`, indicando el caso de prueba que falló.
- Las decisiones importantes se anotan en `seguimiento/decisiones.md`.
- El **enlace de coordinación** de cada grupo responde por los plazos.

## 4. Calendario

| Día | Fecha | Qué ocurre |
|---|---|---|
| 1 | Mié 28/10 (clase) | Lanzamiento: presentación y lectura del caso. Cada grupo asigna roles y crea su carpeta en `seguimiento/areas/`. |
| 2 | Jue 29/10 | Las áreas del cliente prueban la v0.1 y envían sus primeras solicitudes. |
| 3 | Vie 30/10 | El proveedor responde con su plan. El Grupo 4 confirma reglas de los datos de personal. |
| 4 | Sáb 31/10 – Dom 1/11 | El proveedor corrige y publica cambios por Pull Request. Seguridad, QA y Soporte revisan. |
| 5 | Lun 2/11 | Producto acepta u observa. Dirección de TI consolida el **Plan de arranque** y lo escala a Gerencia. |
| 6 | Mar 3/11, hasta las 23:59 | Cada grupo cierra su expediente y completa la evaluación entre áreas. |
| 7 | Mié 4/11 (clase) | Sustentación. |

> El fin de semana cuenta como un solo día para los plazos de 24 y 48 horas.

## 5. Mapa mínimo de solicitudes

Cada grupo envía **al menos estas 2 solicitudes** y responde todas las que reciba. Se pueden enviar más si el trabajo lo requiere.

| Grupo | Envía a… | Tema | Día |
|---|---|---|---|
| 1 | 11 | Condiciones para aprobar el plan de trabajo | 5 |
| 1 | Gerencia | Plan de arranque y decisión requerida | 5 |
| 2 | 11 | Historias de usuario priorizadas | 2 |
| 2 | 7 | Qué significa "listo" para los trabajadores | 3 |
| 3 | 13 | Cumplimiento de estándares e integración con Personal | 2 |
| 3 | 4 | Servicios que expone el Sistema de Personal | 2 |
| 4 | 9 | Reglas de roles y estados de los trabajadores | 3 |
| 4 | 7 | Casos de prueba sobre los datos de Personal | 3 |
| 5 | 6 | Controles de seguridad en los entornos | 2 |
| 5 | 12 | Hallazgo de seguridad en la v0.1 | 4 |
| 6 | 14 | Entornos y forma de despliegue | 2 |
| 6 | 5 | Accesos para los entornos | 3 |
| 7 | 14 | Criterios de aceptación | 2 |
| 7 | 12 | Observaciones de las pruebas | 4 |
| 8 | 2 | Quiénes usarán el módulo y cómo capacitarlos | 2 |
| 8 | 12 | Mensajes que verá el usuario si algo falla | 4 |
| 9 | 4 | Calidad de los datos de trabajadores | 2 |
| 9 | 8 | Qué hacer si un trámite queda sin responsable válido | 4 |
| 10 | 11 | Hitos del contrato | 2 |
| 10 | 1 | Estado del proyecto y riesgos | 5 |
| 11 | 1 | Plan de trabajo y equipo | 3 |
| 11 | 10 | Dudas sobre cronograma y contrato | 3 |
| 12 | 2 | Validar cambios en la pantalla | 3 |
| 12 | 13 | Formato de errores y servicios | 3 |
| 13 | 4 | Datos de Personal que necesita | 2 |
| 13 | 3 | Propuesta de corrección para validar | 3 |
| 14 | 7 | Versión lista para pruebas | 4 |
| 14 | 6 | Entorno de pruebas | 3 |

## 6. Entregable de cada grupo

Carpeta `seguimiento/areas/GXX-nombre-del-area/` con un archivo `expediente.md` (máximo 4 páginas) basado en `seguimiento/plantillas/expediente.md`. Cada sección indica quién la elaboró.

1. **Diagnóstico:** estructura de la empresa y posicionamiento de TI, con evidencia del caso.
2. **Ficha del área:** propósito, responsabilidades, qué decide, qué coordina y qué escala.
3. **Objetivo del área:** cadena entrega técnica → capacidad → cambio → resultado → valor, y la evidencia que mostraría avance.
4. **Personas:** perfil de los 3 roles y una brecha de capacidad con su alternativa.
5. **Aporte al proyecto:** enlaces a sus Issues, pruebas, Pull Requests o decisiones.

Entregas especiales: Grupo 1 entrega el Plan de arranque consolidado; Grupo 11 el plan de trabajo del proveedor.

## 7. Evaluación

| Criterio | Peso |
|---|---|
| Diagnóstico | 15 % |
| Ficha y decisiones del área | 20 % |
| Objetivo y cadena de valor | 15 % |
| Personas y brecha | 10 % |
| Calidad de interacciones (Issues, pruebas, Pull Requests) | 20 % |
| Evaluación entre áreas (con evidencia) | 10 % |
| Sustentación y pregunta individual | 10 % |
