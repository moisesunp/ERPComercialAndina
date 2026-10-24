# Inicia el Sistema de Personal (puerto 5001) y Mesa de Trámites (puerto 5000).
# Uso: python iniciar.py   (detener con Ctrl+C)
import subprocess, sys, time, os
aqui = os.path.dirname(os.path.abspath(__file__))
erp = subprocess.Popen([sys.executable, os.path.join(aqui, 'erp-personal', 'app.py')])
time.sleep(1)
app = subprocess.Popen([sys.executable, os.path.join(aqui, 'tramites', 'app.py')])
print('\nMesa de Trámites: http://localhost:5000\nSistema de Personal (API): http://localhost:5001/trabajadores\n')
try:
    app.wait()
except KeyboardInterrupt:
    pass
finally:
    erp.terminate(); app.terminate()
