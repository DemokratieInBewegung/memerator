
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm

from .models import Meme
class MemeForm(ModelForm):
    class Meta:
        model = Meme
        exclude = ['id', 'created_at']


def show(request, code=None):
    if code:
        print(code)
        model = get_object_or_404(Meme, pk=code)
        return render(request, 'show.html', context=dict(model=model))

    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        model = form.save()
        return redirect('/{}#showShare'.format(model.id))

    return render(request, 'index.html', context=dict(form=MemeForm(), args=request.GET))


