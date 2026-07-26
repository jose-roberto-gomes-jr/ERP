from auth import criar_token, verificar_token

token = criar_token(1)
print("Token criado:", token)

resultado = verificar_token(token)
print("Resultado da verificação:", resultado)