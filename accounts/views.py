from django.shortcuts import render, redirect
from clubs.models import Student

# Create your views here.
def registerPage(request):
    from accounts.forms import SignupForm
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            Student.objects.create(
                user=user,
                first_name=username,
            )
            return redirect('login')

    context = {'form': form, }
    return render(request, 'registration/register.html', context)