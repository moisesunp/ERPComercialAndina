-- Sistema de Personal de Comercial Andina (datos de muestra)
CREATE TABLE areas (id INTEGER PRIMARY KEY, nombre TEXT);
CREATE TABLE trabajadores (
  codigo TEXT PRIMARY KEY, nombre TEXT, area_id INTEGER, cargo TEXT,
  jefe_codigo TEXT, rol TEXT, estado TEXT
);
INSERT INTO areas VALUES
 (1,'Recursos Humanos'),(2,'Contabilidad'),(3,'Logística'),(4,'Mesa de Ayuda TI'),
 (5,'Comercial'),(6,'Operaciones de tiendas'),(7,'Gerencia de Administración');
INSERT INTO trabajadores VALUES
 ('T001','Rosa Quispe Ramos',7,'Gerente de Administración',NULL,'jefe','ACTIVO'),
 ('T002','Luis Castillo Neyra',1,'Jefe de RRHH','T001','jefe','ACTIVO'),
 ('T003','Carmen Saldarriaga Flores',1,'Analista de RRHH','T002','gestor','ACTIVO'),
 ('T004','Jorge Ipanaqué Ruiz',1,'Asistente de RRHH','T002','gestor','ACTIVO'),
 ('T005','Ana Lucía Chira Vílchez',2,'Contadora','T001','jefe','ACTIVO'),
 ('T006','Pedro Zapata Morales',2,'Asistente contable','T005','gestor','ACTIVO'),
 ('T007','Milagros Yarlequé Paz',3,'Jefa de Logística','T001','jefe','ACTIVO'),
 ('T008','Kevin Sernaqué Lozada',3,'Comprador','T007','gestor','ACTIVO'),
 ('T009','Diego Alburqueque Silva',4,'Coordinador de Mesa de Ayuda','T001','jefe','ACTIVO'),
 ('T010','Fiorella Panta Cruz',4,'Analista de soporte','T009','gestor','ACTIVO'),
 ('T011','Raúl Mendoza Távara',1,'Analista de RRHH','T002','gestor','CESADO'),
 ('T012','Sofía Ramírez Olaya',5,'Jefa Comercial','T001','jefe','ACTIVO'),
 ('T013','Martín Correa Juárez',5,'Ejecutivo comercial','T012','colaborador','ACTIVO'),
 ('T014','Gabriela Nima Seminario',6,'Jefa de tienda Sullana','T099','jefe','ACTIVO'),
 ('T015','Andrés Vite Calle',6,'Vendedor','T014','colaborador','ACTIVO'),
 ('T016','Karina Ojeda Prieto',6,'Vendedora','T014','colaborador','ACTIVO'),
 ('T017','Héctor Rumiche Durand',6,'Vendedor','T014','colaborador','ACTIVO'),
 ('T018','Ana Lucia Chira Vilchez',2,'Contadora','T001','jefe','ACTIVO'),
 ('T019','Paola Inga Mogollón',3,'Asistente de almacén','T007','gestor','ACTIVO'),
 ('T020','César Farfán Zeta',4,'Analista de soporte','T009','gestor','ACTIVO');
