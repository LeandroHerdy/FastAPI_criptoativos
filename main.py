from fastapi import FastAPI, APIRouter

from views import user_router, assets_router

app = FastAPI(title='API Criptoativos - FastAPI sqlalchemy')
router = APIRouter()

# @app.router.get('/')
@router.get('/')
def first():
    return 'hello world!'

app.include_router(prefix='/first', router=router)
app.include_router(user_router)
app.include_router(assets_router)
