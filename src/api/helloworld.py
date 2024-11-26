from fastapi import APIRouter

router = APIRouter(tags=["Start page"])

@router.get("/")
def text_helloworld():
    return {'text': "Hello World"}