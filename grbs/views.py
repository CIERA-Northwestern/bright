from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import GRB
from .forms import GRBForm, DownloadForm
from django.contrib.auth.decorators import user_passes_test
import zipfile
import io
# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    alphabetical_grbs_list = GRB.objects.order_by('grb_name')
    context = {'alphabetical_grbs_list': alphabetical_grbs_list}
    return render(request, 'grbs/index.html', context)

@user_passes_test(lambda u: u.is_superuser)
def detail(request, grb_id):
    grb = get_object_or_404(GRB, pk=grb_id)
    return render(request, 'grbs/detail.html', {'grb': grb})

def download(request, grb_ids):
    grb = get_object_or_404(GRB, pk=grb_id)
    return render(request, 'grbs/detail.html', {'grb': grb})

def function(request):
    if request.method == 'POST':
        form = GRBForm(request.POST)
        if form.is_valid():
            new_grb = form.save(commit=False)
            new_grb.save()
            return redirect(function_that_happens_at_url)

def function_that_happens_at_url(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = GRBForm(request.POST)
            if form.is_valid():
                new_grb = form.save(commit=False)
                new_grb.save()
                return redirect('/')
        else:
            form = GRBForm()
        return render(request, 'grbs/add_grb.html', {'form' : form})
    else:
        return redirect('/accounts/login')


def bulkdownload(request):
    if request.method == 'GET':
        form = DownloadForm(request.GET)
        if form.is_valid():
            grbs_ids_to_download = list(filter(None,form.cleaned_data['grbs'].split(',')))
            response = HttpResponse(content_type='application/zip')
            with zipfile.ZipFile(response, 'w') as zf:
                for grb_id in grbs_ids_to_download:
                    grb = get_object_or_404(GRB, pk=grb_id)
                    zf.write(grb.json_metadata.file.name, arcname=grb.json_metadata.name)
            ZIPFILE_NAME = 'grb_metadata.zip'
            response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
            return response
        return redirect("grbs:index")
    else:
        return redirect("grbs:index")
