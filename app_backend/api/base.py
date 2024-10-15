from fastapi import APIRouter

router = APIRouter(tags=["Home"])

@router.get('/')
async def index():
    return {'message': 'home_page'}