from django.shortcuts import render, get_object_or_404, redirect
from .forms import HashForm
from .models import Hash
import hashlib

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = HashForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=text_hash)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            
            return redirect('hash', hash=text_hash)

    form = HashForm()
    return render(request, 'hashing/index.html', {'form': form})

def hash_view(request, hash):   
    hash = get_object_or_404(Hash, hash=hash)
    return render(request, 'hashing/hash.html', {'hash': hash})

