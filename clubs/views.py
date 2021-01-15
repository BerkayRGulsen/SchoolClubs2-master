from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'clubs/home.html')


def all_clubs(request):
    return render(request, 'clubs/allClubs.html')

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def socialclubs(request, pk):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()
    club = Club.objects.get(id=pk)

    user = request.user.student
    try:
        myclubs = ClubStudent.objects.get(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    context = {'allclubs': allclubs, 'myclubs': myclubs, 'club': club, 'events':events}
    return render(request, 'clubs/SocialClubs.html', context)

@login_required(login_url='login')
def socialclubs_def(request):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()

    user = request.user.student
    try:
        myclubs = ClubStudent.objects.get(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None

    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    context = {'allclubs': allclubs, 'myclubs': myclubs, 'events':events}
    return render(request, 'clubs/SocialClubs_def.html', context)

def announcement(request, pk):
    from clubs.models import Club,ClubStudent,Event
    allclubs = Club.objects.all()
    user = request.user.student

    try:
        myclubs = ClubStudent.objects.get(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    club = Club.objects.get(id=pk)

    announcements = club.announcement_set.all()

    context = {'announcements':announcements,'allclubs': allclubs, 'myclubs': myclubs, 'club':club, 'events':events}
    return render(request, 'clubs/announcements.html', context)


def post(request, pk):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()
    user = request.user.student
    try:
        myclubs = ClubStudent.objects.get(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None

    try:
        club = Club.objects.get(id=pk)
    except Club.DoesNotExist:
        club = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    posts = club.posts_set.all()

    context = {'posts': posts, 'allclubs': allclubs, 'myclubs': myclubs,'club':club, 'events':events}
    return render(request, 'clubs/posts.html', context)



def chat(request, pk):
    context = {}
    return render(request, 'clubs/chat.html')

def survey(request, pk):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()
    user = request.user.student

    club = Club.objects.get(id=pk)
    try:
        myclubs = ClubStudent.objects.get(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    surveys = club.survey_set.all()

    context = {'surveys': surveys, 'allclubs': allclubs, 'myclubs': myclubs, 'club': club, 'events':events}
    return render(request, 'clubs/surveys.html', context)



def discussion(request, pk):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()
    user = request.user.student

    club = Club.objects.get(id=pk)
    try:
        myclubs = ClubStudent.objects.get(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    discussions = club.discussion_set.all()
    context = {'discussions': discussions, 'allclubs': allclubs, 'myclubs': myclubs, 'club': club, 'events': events}
    return render(request, 'clubs/discussions.html')


def messages(request):
    return render(request, 'clubs/message.html')


def ccalendar(request):
    return render(request, 'clubs/ccalendar.html')


def clupDetail(request):
    return render(request, 'clubs/detailPage.html')

def eventPage(request):
    return render(request, 'clubs/eventPage.html')

def eventPageJoined(request):
    return render(request, 'clubs/eventPageJoined.html')

def userPage(request):
    return render(request, 'clubs/userpage.html')

def addEvent(request):

    if request.method=="POST":
        student = request.user.student
        name = request.POST.get('name')
        content = request.POST.get('content')
        location = request.POST.get('location')
        date = request.POST.get('date')
        from clubs.models import Event
        Event.objects.create(
            content=content,
            location=location,
            until_date=date,
            publisher=student,
            event_name=name
        )

    return render(request, 'forms/addEvent.html')

def addPost(request):
    return render(request, 'forms/addPost.html')



def addSurvey(request, pk):
    from clubs.models import Club,Survey
    from clubs.forms import addSurveyForm

    user = request.user.student
    club = Club.objects.get(id=pk)


    form = addSurveyForm()
    if request.method == "POST":
        form = addSurveyForm(request.POST)
        if form.is_valid():

            end_date = form.cleaned_data.get("end_date")
            question = form.cleaned_data.get("question")
            element1 = form.cleaned_data.get("element1")
            element2 = form.cleaned_data.get("element2")

            Survey.objects.create(
                end_date = end_date,
                question = question,
                publisher = user,
                element1 = element1,
                element2 = element2,
                counter1 = 0,
                counter2 = 0,
                club = club,
            )

            return redirect('survey', pk=club.id)

    context = {'form': form}
    return render(request, 'forms/addSurvey.html', context)




def addDiscussion(request):
    return render(request, 'forms/addDiscussion.html')

def join(request):
    return render(request, 'forms/join.html')

def report(request):
    return render(request, 'forms/report.html')


