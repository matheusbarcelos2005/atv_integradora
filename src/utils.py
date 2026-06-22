def validar_mensagem(mensagem):
    if mensagem is None:
        raise ValueError("A mensagem não pode ser nula.")
    
    if not isinstance(mensagem, str):
        raise ValueError("A mensagem deve ser uma string de texto.")
    
    texto_limpo = mensagem.strip()
    if len(texto_limpo) < 1:
        raise ValueError("A mensagem não pode estar vazia.")
    
    if len(texto_limpo) > 4000:
        raise ValueError("A mensagem não pode exceder o limite de 4000 caracteres.")
        
    return texto_limpo
