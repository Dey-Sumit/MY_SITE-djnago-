from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Carousel, Skill ,Message
from .forms import MessageForm
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail,EmailMessage


class Skill:
    def __init__(self,name,body,icon):
        self.name = name
        self.body = body
        self.icon = icon
def index(request):
    s1 = Skill("Java Script", "JavaScript is a lightweight, interpreted, or just.", "fa-js-square")
    s2 = Skill("React", "React(also known as React.js or ReactJS) is a JavaScript .", "fa-react")
    s3 = Skill("Python", "Python is an interpreted, high-level, general-purpose programming language.", "fa-python" )
    s4 = Skill("CSS3", "CSS3 is the latest evolution of the Cascading Style Sheets language and aims at extending CSS2.", "fa-css3-alt")
    skills = [s1, s2, s3, s4]

    ms1 = Skill("Node js", "Node.js is an open-source and cross-platform JavaScript runtime environment.", "fa-node")
    ms2 = Skill("Java ", "Java is a widely used programming language expressly designed for use ", "fa-java")
    ms3 = Skill("MySQL", "MySQL is the most popular Open Source Relational SQL Database Management System.", "fa-database")

    moreSkills = [ms1, ms2, ms3]

    if request.method == 'POST':
        print("msg received ")
        form = MessageForm(request.POST)

        if form.is_valid():
            cleaned_name = form.cleaned_data['name']
            cleaned_email = form.cleaned_data['email']
            cleaned_message = form.cleaned_data['message']

            data = Message(name=cleaned_name, email=cleaned_email, message=cleaned_message)
            data.save()

            if cleaned_email is not "":
                mail_body = "Thank You" + cleaned_name + ":)"
                email = EmailMessage(
                    mail_body,
                    'How was your experience about my portfolio ? Hope to see you again',
                    settings.EMAIL_HOST_USER,
                    [cleaned_email],
                    ['code.sumax@gmail.com'],
                    reply_to=['code.sumax@gmail.com'],
                    headers={'Message-ID': 100},
                )
                email.send(fail_silently=False)

            messages.success(request, 'Hey I got your messsage ; Thanks a lot :)')

            return HttpResponseRedirect('/')
        else:
            print("error")
            print(form.errors)

    carousel_items = Carousel.objects.all()
    return render(request, 'portfolio/v2/contact_SECTION.html', {"skills": skills, "more_skills": moreSkills,"carousel_items":carousel_items})
 #
 # {% if item.0 %}
 #            <div class="carousel-item active">
 #                {% else %}
 #                <div class="carousel-item ">
 #                    {% endif %}