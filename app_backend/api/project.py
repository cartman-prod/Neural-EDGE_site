from fastapi import APIRouter

router = APIRouter(tags=["Projects"])

@router.get('/projects')
async def get_projects():
    return { "projects": 'Page_Projects' }