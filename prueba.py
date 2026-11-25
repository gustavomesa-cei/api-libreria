import bcrypt

# 1. Hashear contraseña (REGISTRO)
contrasenia_plana = "mi_perro_bobby_123"
# bcrypt requiere bytes, por eso usamos .encode('utf-8')
salt = bcrypt.gensalt()
contrasenia_hasheada = bcrypt.hashpw(contrasenia_plana.encode('utf-8'), salt)

# Guardamos como texto en la BD usando .decode('utf-8')
hash_para_bd = contrasenia_hasheada.decode('utf-8')
print("Lo que guarda la Base de Datos:", hash_para_bd)

# 2. Verificar contraseña (LOGIN)
es_valida = bcrypt.checkpw(
    "mi_perro_bobby_123".encode('utf-8'), 
    hash_para_bd.encode('utf-8')
)
print("¿Es válida?:", es_valida)
