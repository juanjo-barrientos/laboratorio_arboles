# utils/logger_config.py
import logging
import os

def setup_logger():
    """Configura y retorna un logger para registrar operaciones."""
    # Crear el directorio de logs si no existe
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logger = logging.getLogger('tree_operations')
    logger.setLevel(logging.INFO)

    # Evitar agregar manejadores múltiples si el logger ya tiene
    if not logger.handlers:
        # Crear un manejador de archivos que registre incluso los mensajes de depuración
        fh = logging.FileHandler('logs/operations.log')
        fh.setLevel(logging.INFO)

        # Crear un formato y agregarlo a los manejadores
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # Agregar el manejador al logger
        logger.addHandler(fh)

    return logger

# Instancia global del logger
logger = setup_logger()