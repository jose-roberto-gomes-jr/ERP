import os
from datetime import datetime, timedelta, timezone
import jwt
from dotenv import load_dotenv

load_dotenv()

SECRETY_KEY_JWT = os.getenv("SECRETY_KEY_JWT")
ALGORITHM = "HS256"
EXPIRACAO_HORAS = 4

def criar_token(usuario_id: int) -> str:
    agora = datetime.now(timezone.utc)
    payload = {
        "sub": str(usuario_id),
        "iat": agora,
        "exp": agora + timedelta(hours=EXPIRACAO_HORAS)
    }

    token = jwt.encode(payload, SECRETY_KEY_JWT, algorithm=ALGORITHM)
    return token

def verificar_token (token: str) -> int:
    try:
        payload = jwt.decode(token, SECRETY_KEY_JWT, algorithms=[ALGORITHM])
        usuario_id = int(payload.get("sub"))
        return int(usuario_id) if usuario_id else None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None