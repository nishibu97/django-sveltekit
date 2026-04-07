from ninja import Router

router = Router()

@router.get("/")
def index(request):
    return {"message": "Hello from polls"}