import select
from django.shortcuts import render

# Create your views here.
def index(request):
    cover = None
    if request.method == 'POST':
        selectedImage = request.POST.get('selectedImage')
        backgroundColor = request.POST.get('backgroundColor')
        titleText = request.POST.get('titleText')
        fontSize = request.POST.get('fontSize')
        fontColor = request.POST.get('fontColor')
        
        cover = {
            'selected': f'images/{selectedImage}',
            'backgroundColor':backgroundColor,
            'titleText':titleText,
            'fontSize':fontSize,
            'fontColor':fontColor,
            }
        cover = {
            'cover':cover
            }
    return render(request,"magazine/index.html",cover) 