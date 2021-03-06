from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal.models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from django.forms import modelformset_factory, inlineformset_factory
from django.core.files.storage import FileSystemStorage
from crispy_forms.helper import FormHelper

# Create your views here.


@login_required(login_url='administrator')
def accountSettings(request):
    user = request.user.useradmin
    form = UserAdminForm(instance=user)
    # print(form)

    if request.method == 'POST':
        form = UserAdminForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            messages.info(request, 'Data berhasil diubah')

    context = {'form': form}
    return render(request, 'adminportal/account_settings.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homeadmin')
        else:
            messages.info(request, 'Username atau Password tidak valid!')

    context = {}
    return render(request, 'adminportal/loginpage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('administrator')


@login_required(login_url='administrator')
def homeadmin(request):
    tot_pengumuman = Pengumuman.objects.all().count()
    tot_berita = Berita.objects.all().count()
    tot_aplikasi = LinkApp.objects.all().count()
    tot_probisSOP = Probis.objects.all().count()
    tot_stdDokumen = StandarDokumen.objects.all().count()
    tot_regulasi = Regulasi.objects.all().count()
    tot_banner = Banner.objects.all().count()

    context = {
        'tot_pengumuman': tot_pengumuman,
        'tot_berita': tot_berita,
        'tot_aplikasi': tot_aplikasi,
        'tot_probisSOP': tot_probisSOP,
        'tot_stdDokumen': tot_stdDokumen,
        'tot_regulasi': tot_regulasi,
        'tot_banner': tot_banner,
    }
    return render(request, 'adminportal/dashboard.html', context)


@login_required(login_url='administrator')
def pengumuman(request):
    context = {

    }
    return render(request, 'adminportal/pengumuman.html', context)


@login_required(login_url='administrator')
def admin_pengumuman(request):

    pengumuman = Pengumuman.objects.all().order_by('-id')
    form = PengumumanForm()

    if request.method == 'POST':
        form = PengumumanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_pengumuman')

    context = {
        'pengumuman': pengumuman,
        'form': form,
    }
    return render(request, 'adminportal/admin_pengumuman.html', context)


@login_required(login_url='administrator')
def lampirkan_file(request, pengumuman_id):
    pengumuman = Pengumuman.objects.get(id=pengumuman_id)
    LampiranPengumumanFormset = inlineformset_factory(
        Pengumuman, PengumumanFile, fields=('files',), can_delete=False, extra=3)

    if request.method == 'POST':
        formset = LampiranPengumumanFormset(
            request.POST, request.FILES, instance=pengumuman)
        if formset.is_valid():
            formset.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_pengumuman')

    formset = LampiranPengumumanFormset(instance=pengumuman)

    return render(request, 'adminportal/lampirkan_file.html', {'formset': formset})


@login_required(login_url='administrator')
def delete_pengumuman(request, pk):
    pengumuman = Pengumuman.objects.get(id=pk)
    pengumuman.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('admin_pengumuman')


@login_required(login_url='administrator')
def ubah_pengumuman(request, pk):
    judul1 = "Pengumuman"
    judul2 = "Ubah Pengumuman"

    pengumuman = Pengumuman.objects.get(id=pk)
    form = PengumumanForm(instance=pengumuman)

    if request.method == 'POST':
        form = PengumumanForm(request.POST, request.FILES, instance=pengumuman)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('admin_pengumuman')

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)


@login_required(login_url='administrator')
def admin_berita(request):
    berita = Berita.objects.all().order_by('-id')
    form = BeritaForm()

    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_berita')

    context = {
        'berita': berita,
        'form': form,
    }
    return render(request, 'adminportal/admin_berita.html', context)


@login_required(login_url='administrator')
def lampirkan_file_berita(request, berita_id):
    berita = Berita.objects.get(id=berita_id)
    LampiranBeritaFormset = inlineformset_factory(
        Berita, BeritaFile, fields=('files',), can_delete=False, extra=3)

    if request.method == 'POST':
        formset = LampiranBeritaFormset(
            request.POST, request.FILES, instance=berita)
        if formset.is_valid():
            formset.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_berita')

    formset = LampiranBeritaFormset(instance=berita)

    return render(request, 'adminportal/lampirkan_file_berita.html', {'formset': formset})


@login_required(login_url='administrator')
def delete_berita(request, pk):
    berita = Berita.objects.get(id=pk)
    berita.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('admin_berita')


@login_required(login_url='administrator')
def ubah_berita(request, pk):
    judul1 = "Berita"
    judul2 = "Ubah Berita"
    berita = Berita.objects.get(id=pk)
    form = BeritaForm(instance=berita)

    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES, instance=berita)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('admin_berita')

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)


@login_required(login_url='administrator')
def tautan_aplikasi(request):
    tautan_aplikasi = LinkApp.objects.all().order_by('-id')
    form = TautanForm()

    if request.method == 'POST':
        form = TautanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('tautan_aplikasi')

    context = {
        'form': form,
        'tautan': tautan_aplikasi,
    }

    return render(request, 'adminportal/tautan_aplikasi.html', context)


@login_required(login_url='administrator')
def delete_tautan(request, pk):
    tautan = LinkApp.objects.get(id=pk)
    tautan.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('delete_tautan')


@login_required(login_url='administrator')
def ubah_tautan(request, pk):
    judul1 = "Tautan"
    judul2 = "Ubah Tautan"
    tautan = LinkApp.objects.get(id=pk)
    form = TautanForm(instance=tautan)

    if request.method == 'POST':
        form = TautanForm(request.POST, request.FILES, instance=tautan)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('tautan_aplikasi')

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)


@login_required(login_url='administrator')
def admin_probis_sop(request):
    admin_probis_sop = Probis.objects.all().order_by('-id')
    form = ProbisSopForm()

    if request.method == 'POST':
        form = ProbisSopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_probis_sop')

    context = {
        'form': form,
        'admin_probis_sop': admin_probis_sop,
    }

    return render(request, 'adminportal/admin_probis_sop.html', context)


@login_required(login_url='administrator')
def delete_probis_sop(request, pk):
    admin_probis_sop = Probis.objects.get(id=pk)
    admin_probis_sop.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('admin_probis_sop')


@login_required(login_url='administrator')
def ubah_admin_probis_sop(request, pk):
    judul1 = "Proses Bisnis & SOP"
    judul2 = "Ubah Proses Bisnis"
    probis = Probis.objects.get(id=pk)
    form = ProbisSopForm(instance=probis)

    if request.method == 'POST':
        form = ProbisSopForm(request.POST, request.FILES,
                             instance=probis)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('admin_probis_sop')

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)


@login_required(login_url='administrator')
def ubah_admin_sop(request, pk):
    judul1 = "Proses Bisnis & SOP"
    judul2 = "Ubah SOP"
    probis = Probis.objects.get(id=pk)

    LampiranSOPFormset = inlineformset_factory(
        Probis, SOP, fields=('title', 'description', 'file', ), can_delete=False, extra=1)

    if request.method == 'POST':
        form = LampiranSOPFormset(
            request.POST, request.FILES, instance=probis)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_probis_sop')

    form = LampiranSOPFormset(instance=probis)

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)


@login_required(login_url='administrator')
def admin_standar_dokumen(request):
    standar_dokumen = StandarDokumen.objects.all().order_by('-id')

    form = StandarDokumenForm()

    if request.method == 'POST':
        form = StandarDokumenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_standar_dokumen')

    context = {'standar_dokumen': standar_dokumen, 'form': form}
    return render(request, 'adminportal/admin_standar_dokumen.html', context)


@login_required(login_url='administrator')
def ubah_admin_dokumen(request, pk):
    judul1 = "Standar Dokumen"
    judul2 = "Standar Dokumen"
    dokumen = StandarDokumen.objects.get(id=pk)
    form = StandarDokumenForm(instance=dokumen)

    if request.method == 'POST':
        form = StandarDokumenForm(request.POST, request.FILES,
                                  instance=dokumen)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('admin_standar_dokumen')

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)


@login_required(login_url='administrator')
def ubah_admin_stddokumen(request, pk):
    judul1 = "Standar Dokumen"
    judul2 = "Ubah Standar Dokumen"

    dokumen = StandarDokumen.objects.get(id=pk)

    LampiranStdDokumenFormset = inlineformset_factory(
        StandarDokumen, SDF, fields=('title', 'file', ), can_delete=False, extra=1)

    if request.method == 'POST':
        form = LampiranStdDokumenFormset(
            request.POST, request.FILES, instance=dokumen)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_standar_dokumen')

    form = LampiranStdDokumenFormset(instance=dokumen)

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)


@login_required(login_url='administrator')
def delete_admin_dokumen(request, pk):
    dokumen = StandarDokumen.objects.get(id=pk)
    dokumen.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('admin_standar_dokumen')

@login_required(login_url='administrator')
def admin_regulasi(request):
    regulasi = Regulasi.objects.all().order_by('-id')
    form = RegulasiForm()

    if request.method == 'POST':
        form = RegulasiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_regulasi')

    context = {'regulasi': regulasi, 'form': form}
    return render(request, 'adminportal/admin_regulasi.html', context)

@login_required(login_url='administrator')
def ubah_admin_regulasi(request, pk):
    judul1 = "Regulasi"
    judul2 = "Ubah Regulasi"

    regulasi = Regulasi.objects.get(id=pk)
    form = RegulasiForm(instance=regulasi)

    if request.method == 'POST':
        form = RegulasiForm(request.POST, request.FILES,instance=regulasi)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('admin_regulasi')

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)

@login_required(login_url='administrator')
def hapus_admin_regulasi(request, pk):
    regulasi = Regulasi.objects.get(id=pk)
    regulasi.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('admin_regulasi')

@login_required(login_url='administrator')
def admin_banner(request):
    banner = Banner.objects.all().order_by('-id')
    form = BannerForm()

    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('admin_banner')

    context = {'banner': banner, 'form': form}
    return render(request, 'adminportal/admin_banner.html', context)

@login_required(login_url='administrator')
def ubah_admin_banner(request, pk):
    judul1 = "Banner"
    judul2 = "Ubah Banner"

    banner = Banner.objects.get(id=pk)
    form = BannerForm(instance=banner)

    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES,instance=banner)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('admin_banner')

    context = {'form': form, 'judul1': judul1, 'judul2': judul2}
    return render(request, 'adminportal/admin_ubah.html', context)

@login_required(login_url='administrator')
def hapus_admin_banner(request, pk):
    banner = Banner.objects.get(id=pk)
    banner.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('admin_banner')