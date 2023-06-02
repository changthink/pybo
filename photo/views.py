from django.shortcuts import render
from .models import Photo, Brand, Unit, Viewimage
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect

# 로그인 여부에 대해서, 함수형 뷰에는 decolator, 클래스형 뷰에는 mixins 을 사용함
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

def brand_list(request):
    brands = Brand.objects.all()
    context = { 'brands' : brands }
    return render(request, 'photo/brand_list.html', context)

def img_list(request, brand_id):
    brands = Brand.objects.get(id=brand_id)
    units = brands.unit_set.all()
    context = {'brands': brands, 'units': units }
    return render(request, 'photo/img_list.html', context)


def viewimg_list(request):
    vimg = Viewimage.objects.all()
    context = {'images': vimg }
    return render(request, 'photo/viewimg_list.html', context)

