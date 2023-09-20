from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(id=UUID('1b2041eb-45fd-44ab-a584-193fbce901b3'),
         first_name="Dayanne", 
         last_name="Serafim", 
         email="dayanne@hotmail.com", 
         role=[Role.role_1]),

    User(id=UUID('ceca140a-0484-4bd6-baea-2d994920fe70'), 
         first_name="Felicia", 
         last_name="Warren", 
         email="felicia@hotmail.com", 
         role=[Role.role_2]),

    User(id=UUID('7dcaf656-54b7-41be-841e-8623c9a718e2'), 
         first_name="Blue", 
         last_name="Hayes", 
         email="blue@hotmail.com", 
         role=[Role.role_3]),
    
]

@app.get('/')
async def root():
    return {'message': 'Olá, WoMakers!'}

@app.get('/api/users')
async def get_users():
    return db;

@app.get('/api/users/{id}')
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return{'message': 'Usuário não encontrado.'}

@app.post('/api/users')
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    - ***id***: UUID
    - ***first_name***: string
    - ***last_name***: string
    - ***email***: string 
    - ***role***: Role

    """
    db.append(user)
    return {'id': user.id}

@app.delete('/api/users/{id}')
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'Usuário com o id {id} não encontrado!'
    )    

#crie uma função assíncrona de http put requests, criando e passando a rota se necessário
@app.put('/api/users/{id}')
async def update_user(id: UUID, first_name: str, last_name: str, email: str):
    for user in db:
        if user.id == id:
            user_to_update = user
            user_to_update.first_name = first_name
            user_to_update.last_name = last_name
            user_to_update.email = email
            return {'message': 'Usuário atualizado com sucesso', 'user': user_to_update}

    
    raise HTTPException(
        status_code=404,
        detail=f'Usuário com o id {id} não encontrado!'
    )
    