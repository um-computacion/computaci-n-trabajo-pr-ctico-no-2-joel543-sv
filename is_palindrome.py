def is_palindrome(text):
    # Limpieza del texto: eliminar espacios, puntuación y convertir a minúsculas
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Comparar el texto limpio con su reverso
    return cleaned_text == cleaned_text[::-1]
