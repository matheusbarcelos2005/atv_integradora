import json
from urllib import request

def enviar_mensagem_api(mensagem: str, api_key: str, api_url: str) -> str:
    payload = json.dumps({"message": mensagem}).encode("utf-8")
    
    req = request.Request(
        api_url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    
    with request.urlopen(req, timeout=30) as response:
        dados = json.loads(response.read().decode("utf-8"))
        
    return dados.get("content") or dados.get("response") or ""
