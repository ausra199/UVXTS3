from django.shortcuts import render
from django.core.mail import send_mail
from .models import Item

def video(request):
    obj = Item.objects.all()
    return render(request, 'about.html', {'obj':obj})

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def blog(request):
    return render(request, 'blog.html', {})

def blogsingle(request):
    return render(request, 'blogsingle.html', {})


def about(request):
    return render(request, 'about.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, # message
            message_email, # from email
            ['a.dovidaityte@gmail.com'], # to email
            fail_silently=False,
        )

        return render(request, 'contact.html', {"message_name":message_name})

    else:
        return render(request, 'contact.html', {})



'''
message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
'''