def saludar(nombre_completo):
    """Devuelve un saludo personalizado. Si el nombre está vacío, devuelve un error."""
    if not nombre_completo or not nombre_completo.strip():
        return "Error: el nombre no puede estar vacío"
    return f"Hola {nombre_completo}"

print(saludar("GitHub"))
print(saludar(""))
