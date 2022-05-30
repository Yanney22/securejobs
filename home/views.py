# Create your views here.
import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render

from home.models import our, package, team, carosel_image, maincarodis, job, enquiry, online_order, \
    customer_own_job_request, service, terms_condition
from securejobs import settings


def own_job_request(request):
    try:
        our1 = our.objects.all()
        packages = package.objects.all().order_by('price')

        carosel_image1 = carosel_image.objects.all().order_by('date_added')
        maincarodis1 = maincarodis.objects.all().order_by('date_added')
        mes = 'Please fill the form below'
        return render(request, "own_job_request.html", {'our': our1,
                                                        'packages': packages,
                                                        'carosel': carosel_image1,
                                                        'main': maincarodis1,
                                                        'message': mes

                                                        })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'The requested page failed to load'
        mes2 = 'Please refresh the page or click on back. If problem still persist, please contact us through any of ' \
               'our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Page Failed to load"
        backg = ' rgba(94,86,97,0.8)'
        return render(request, "error_page.html", {'our': our1,
                                                   'mes1': mes1,
                                                   'mes2': mes2,
                                                   'mes3': mes3,
                                                   'mes4': mes4,
                                                   'backg': backg
                                                   }
                      )


def terms(request):
    try:
        our1 = our.objects.all()
        packages = package.objects.all().order_by('price')
        terms_condition1 = terms_condition.objects.all()
        carosel_image1 = carosel_image.objects.all().order_by('date_added')
        maincarodis1 = maincarodis.objects.all().order_by('date_added')

        return render(request, "terms_and_conditions.html", {'our': our1,
                                                             'packages': packages,
                                                             'carosel': carosel_image1,
                                                             'main': maincarodis1,
                                                             'terms_condition': terms_condition1

                                                             })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'The requested page failed to load'
        mes2 = 'Please refresh the page or click on back. If problem still persist, please contact us through any of ' \
               'our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Page Failed to load"
        backg = ' rgba(94,86,97,0.8)'
        return render(request, "error_page.html", {'our': our1,
                                                   'mes1': mes1,
                                                   'mes2': mes2,
                                                   'mes3': mes3,
                                                   'mes4': mes4,
                                                   'backg': backg
                                                   }
                      )


def submit_own_job(request):
    try:
        our1 = our.objects.all()
        packages = package.objects.all().order_by('price')
        carosel_image1 = carosel_image.objects.all().order_by('date_added')
        maincarodis1 = maincarodis.objects.all().order_by('date_added')

        if request.method == "POST":
            fullname = request.POST['fullname']
            emailaddress = request.POST['emailaddress']
            phonenumber = request.POST['phonenumber']
            pack_choosen = request.POST['pack']
            cv = request.POST['cvupload']
            jobexpect = request.POST['jobexpect']
            salaryexpect = request.POST['salaryexpect']
            actual_salary = 'Not set'
            location_of_company = 'Not Set'
            activationcode = f'{fullname[1:1]}{actual_salary[1:1]}{phonenumber[0:3]}{jobexpect[0:1]}'
            date_added = datetime.datetime.now()
            starting_date = '1111-11-11'

            database = customer_own_job_request()
            database.fullname = fullname
            database.email = emailaddress
            database.phonenumber = phonenumber

            database.pack_choosen = pack_choosen
            database.cv = cv
            database.jobexpect = jobexpect
            database.salaryexpect = salaryexpect
            database.actual_salary = actual_salary
            database.location_of_company = location_of_company
            database.activation_code = activationcode
            database.date_added = date_added
            database.starting_date = starting_date

            database.save()
            messages.warning(request,
                             f"New Make Your Own Job Request from A Customer named {fullname} with phone number {phonenumber} and  email {emailaddress}")
            # Email

            subject = "Welcome to Secure Express"

            message = f'Dear {fullname},Your Make Your Own Job Request has been received successfully.' \
                      f'An agent of ours will call you soon.' \
                      f'Thank you for using Secure Express'
            from_email = settings.EMAIL_HOST_USER
            to_list = [emailaddress]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            mes_success1 = f'Dear {fullname},Your Make Your Own Job Request has been received successfully.'
            mes_success2 = f'An agent of ours will call you soon with you activation code .'
            return render(request, "own_job_request.html", {'our': our1,
                                                            'packages': packages,
                                                            'carosel': carosel_image1,
                                                            'main': maincarodis1,
                                                            'message1': mes_success1,
                                                            'message2': mes_success2,

                                                            })
        else:
            our1 = our.objects.all()
            carosel_image1 = carosel_image.objects.all().order_by('date_added')
            packages = package.objects.all().order_by('price')
            maincarodis1 = maincarodis.objects.all().order_by('date_added')
            return render(request, "own_job_request.html", {'our': our1,
                                                            'packages': packages,
                                                            'carosel': carosel_image1,
                                                            'main': maincarodis1

                                                            }
                          )
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive your request submitted'
        mes2 = 'Please refresh the page or try submitting it again. If problem still persist, please contact us through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Make Your Own Job Request Failed"
        backg = "rgba(94,86,97,0.8)"

        return render(request, "error_page.html", {'our': our1,
                                                   'mes1': mes1,
                                                   'mes2': mes2,
                                                   'mes3': mes3,
                                                   'mes4': mes4,
                                                   'backg': backg
                                                   }
                      )


def enquiry1(request):
    try:
        our1 = our.objects.all()
        packages = package.objects.all().order_by('price')
        team1 = team.objects.all()
        carosel_image1 = carosel_image.objects.all().order_by('date_added')
        maincarodis1 = maincarodis.objects.all().order_by('date_added')

        if request.method == "POST":
            fullname = request.POST['fullname']

            phonenumber = request.POST['phonenumber']
            emailaddress = request.POST['emailaddress']
            option = request.POST['option']
            message = request.POST['message']
            date_added = datetime.datetime.now()

            database = enquiry()
            database.fullname = fullname
            database.phonenumber = phonenumber
            database.emailaddress = emailaddress
            database.option = option
            database.message = message
            database.date_added = date_added

            database.save()
            messages.info(request,
                          f"New Enquire Received from A Customer with phone number {phonenumber} and  email {emailaddress}")
            # Email

            subject = "Welcome to Secure Express"

            message = f'Dear {fullname},your enquiry has been received successfully.' \
                      f'An agent of ours will call you soon for your answer/answers.' \
                      f'Thank you for using Secure Express'
            from_email = settings.EMAIL_HOST_USER
            to_list = [emailaddress]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        return render(request, "thanks.html", {'our': our1,
                                               'packages': packages,
                                               'team': team1,
                                               'carosel': carosel_image1,
                                               'main': maincarodis1
                                               })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive your request submitted'
        mes2 = 'Please refresh the page or try submitting it again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Enquiry Failed "
        backg = "rgba(94,86,97,0.8)"

        return render(request, "error_page.html", {'our': our1,
                                                   'mes1': mes1,
                                                   'mes2': mes2,
                                                   'mes3': mes3,
                                                   'mes4': mes4,
                                                   'backg': backg
                                                   }
                      )


def myiactivation(request):
    try:
        our1 = our.objects.all()
        return render(request, "activation.html", {'our': our1
                                                   })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Enter Activation Code Page, Failed To Load '
        mes2 = 'Please refresh the page or try submitting it again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "IT'S NOT YOU"
        mes4 = "IT'S ME"
        backg = "rgba(94,86,97,0.8)"
        return render(request, "error_page.html", {'our': our1,
                                                   'mes1': mes1,
                                                   'mes2': mes2,
                                                   'mes3': mes3,
                                                   'mes4': mes4,
                                                   'backg': backg
                                                   }
                      )


def finalacti(request):
    try:
        code = request.GET['code']
        suc_mes = ''

        job1 = online_order.objects.filter(Q(activation_code__exact=code))

        if job1:

            our1 = our.objects.all()
            suc_mes = 0
            return render(request, "gurantor_sucessfull.html", {'our': our1,
                                                                'jobs': job1,
                                                                'message1': suc_mes
                                                                })

        else:
            job2 = customer_own_job_request.objects.filter(Q(activation_code__exact=code))

            if job2:
                our1 = our.objects.all()
                suc_mes = 0
                ##suc_mes = f".You got {job2.objects.company_that_the_customer_will_be_placed_in}," \
                ##        f" located at {job2.objects.location_of_company} "
                return render(request, "gurantor_sucessfull.html", {'our': our1,
                                                                    'jobs': job2,
                                                                    'message1': suc_mes
                                                                    })
            else:
                our1 = our.objects.all()
                return render(request, "grantorform.html", {'our': our1
                                                            })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive your request submitted'
        mes2 = 'Please refresh the page or try submitting it again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "IT'S NOT YOU"
        mes4 = "IT'S ME"
        backg = "rgba(94,86,97,0.8)"
        return render(request, "error_page.html", {'our': our1,
                                                   'mes1': mes1,
                                                   'mes2': mes2,
                                                   'mes3': mes3,
                                                   'mes4': mes4,
                                                   'backg': backg
                                                   }
                      )


def onlineorder1(request):
    try:
        our1 = our.objects.all()

        today = datetime.datetime.now()

        if request.method == "POST":
            hisid = request.POST['cname']
            thename = request.POST['jobiname']
            itscat = request.POST['category']
            fulname = request.POST['fullname']
            mail = request.POST['emailaddress']
            phonenumber = request.POST['phonenumber']
            pack = request.POST['pack']
            cv = request.FILES['cvupload']
            jobexpect = request.POST['jobexpect']
            salaryexpect = request.POST['salaryexpect']
            date_added = datetime.datetime.now()
            activationcode = f'{hisid[1:4]}{thename[0:1]}{phonenumber[0:3]}{fulname[0:1]}{salaryexpect[0:2]}'

            whatsiti = online_order()
            whatsiti.job_ID = hisid
            whatsiti.company_name = thename
            whatsiti.company_category = itscat
            whatsiti.fullname = fulname
            whatsiti.phonenumber = phonenumber
            whatsiti.email = mail
            whatsiti.pack_choosen =pack
            whatsiti.cv = cv
            whatsiti.jobexpect = jobexpect
            whatsiti.salaryexpect = salaryexpect
            whatsiti.date_added = date_added
            whatsiti.activation_code = activationcode
            whatsiti.save()
            job1 = job.objects.filter(company_name__company_name__icontains=thename,
                                      company_category__company_category__icontains=itscat)
            messages.success(request,
                             f"New Job Application Received from A Customer Named {fulname} With Phone Number {phonenumber} and "
                             f" email {mail}. Thank you")

            # Email

            subject = "Welcome to Secure Express"
            message = f'Dear {fulname},your job application has been received successfully.' \
                      f'An agent of ours will call you soon to finalise the process.' \
                      f'Thank you for using Secure Express Ghana'
            from_email = settings.EMAIL_HOST_USER
            to_list = [mail]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            return render(request, "successcart.html", {'our': our1,
                                                        'jobs': job1,
                                                        'today': today
                                                        })
        else:
            today = datetime.datetime.now()
            our1 = our.objects.all()
            total_data = job.objects.all().count()
            job1 = job.objects.all().order_by('date_added')
            page = request.GET.get('page', 1)
            paginator = Paginator(job1, 10)
            try:
                job1 = paginator.page(page)
            except PageNotAnInteger:
                job1 = paginator.page(1)
            except EmptyPage:
                job1 = paginator.page(paginator.num_pages)

            return render(request, "Show_Available_Jobs.html", {'our': our1,
                                                                'jobs': job1,
                                                                'today': today,
                                                                'total_data': total_data

                                                                })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive your request submitted'
        mes2 = 'Please refresh the page or try submitting it again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Job Application Failed"
        backg = "rgba(94,86,97,0.8)"

        return render(request, "error_page.html", {'our': our1,
                                                   'mes1': mes1,
                                                   'mes2': mes2,
                                                   'mes3': mes3,
                                                   'mes4': mes4,
                                                   'backg': backg
                                                   }
                      )##//


def home(request):
    try:
        our1 = our.objects.all()
        packages = package.objects.all().order_by('price')
        team1 = team.objects.all()
        carosel_image1 = carosel_image.objects.all().order_by('-date_added')

        maincarodis1 = maincarodis.objects.all().order_by('date_added')
        today = datetime.datetime.now()

        total_data = job.objects.all().count()
        job1 = job.objects.all().order_by('-date_added')[:9]
        services = service.objects.all().order_by("-date_added")
        return render(request, "index.html", {'our': our1,
                                              'packages': packages,
                                              'jobs': job1,
                                              'team': team1,
                                              'carosel': carosel_image1,
                                              'main': maincarodis1,
                                              'today': today,
                                              'total_data': total_data,
                                              'service': services

                                              })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our Site Is Down'
        mes2 = 'We Sincerely Apologize For The Downtime'
        mes3 = "IT'S NOT YOU"
        mes4 = "IT'S ME"

        backg = ' rgba(94,86,97,0.8)'

        return render(request, "error_page.html", {'our': our1,
                                                   'mes1': mes1,
                                                   'mes2': mes2,
                                                   'mes3': mes3,
                                                   'mes4': mes4,
                                                   'backg': backg
                                                   }
                      )


def show_available_jobs(request):
    try:
        today = datetime.datetime.now()
        our1 = our.objects.all()
        total_data = job.objects.all().count()
        job1 = job.objects.all().order_by('date_added')
        page = request.GET.get('page', 1)
        paginator = Paginator(job1, 12)
        try:
            job1 = paginator.page(page)
        except PageNotAnInteger:
            job1 = paginator.page(1)
        except EmptyPage:
            job1 = paginator.page(paginator.num_pages)

        return render(request, "Show_Available_Jobs.html", {'our': our1,
                                                            'jobs': job1,
                                                            'today': today,
                                                            'total_data': total_data

                                                            })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive your request submitted'
        mes2 = 'Please refresh the page or try submitting it again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Page Failed To Load"
        backg = "rgba(94,86,97,0.8)"

    return render(request, "error_page.html", {'our': our1,
                                               'mes1': mes1,
                                               'mes2': mes2,
                                               'mes3': mes3,
                                               'mes4': mes4,
                                               'backg': backg
                                               }
                  )


def apply(request):
    try:
        q = request.GET['cname']
        cate = request.GET['cate']

        pack = package.objects.all()
        today = datetime.datetime.now()
        our1 = our.objects.all()

        job1 = job.objects.filter(company_name__company_name__exact=q,
                                  company_category__company_category__exact=cate
                                  )

        return render(request, "cart.html", {'our': our1,
                                             'jobs': job1,
                                             'today': today,
                                             'packages': pack,
                                             'catei': cate

                                             })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive some data needed successfully'
        mes2 = 'Please refresh the page or try applying again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Program Failed To Apply For The Job"
        backg = "rgba(94,86,97,0.8)"

    return render(request, "error_page.html", {'our': our1,
                                               'mes1': mes1,
                                               'mes2': mes2,
                                               'mes3': mes3,
                                               'mes4': mes4,
                                               'backg': backg
                                               }
                  )


def search(request):
    try:
        q = request.GET['q']
        today = datetime.datetime.now()
        our1 = our.objects.all()
        job1 = job.objects.filter(
            Q(company_name__company_name__icontains=q)
            | Q(location__icontains=q)
            | Q(min_salary__icontains=q)
            | Q(max_salary__icontains=q)
            | Q(job_offer1__icontains=q)
            | Q(job_offer2__icontains=q)
            | Q(job_offer3__icontains=q)
            | Q(job_offer4__icontains=q)
            | Q(job_offer5__icontains=q)
            | Q(job_offer6__icontains=q)
            | Q(job_offer7__icontains=q)
            | Q(job_offer8__icontains=q)
            | Q(job_offer9__icontains=q)
            | Q(job_offer10__icontains=q)
            | Q(job_offer11__icontains=q)
            | Q(job_offer12__icontains=q)
            | Q(job_offer13__icontains=q)
            | Q(job_offer14__icontains=q)
            | Q(job_offer15__icontains=q)
            | Q(job_offer16__icontains=q)
            | Q(job_offer17__icontains=q)
            | Q(job_offer18__icontains=q)
            | Q(job_offer19__icontains=q)
            | Q(job_offer20__icontains=q)
            | Q(deadline__icontains=q)

        ) \
                   .order_by('date_added')[:15]

        return render(request, "search.html", {'our': our1,
                                               'jobs': job1, 'today': today

                                               })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive some data needed successfully'
        mes2 = 'Please refresh the page or try applying again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "K454G58A Failed"
        backg = "rgba(94,86,97,0.8)"

    return render(request, "error_page.html", {'our': our1,
                                               'mes1': mes1,
                                               'mes2': mes2,
                                               'mes3': mes3,
                                               'mes4': mes4,
                                               'backg': backg
                                               }
                  )


def packages(request):
    try:
        our1 = our.objects.all()
        packages = package.objects.all().order_by('price')
        team1 = team.objects.all()
        carosel_image1 = carosel_image.objects.all().order_by('date_added')
        maincarodis1 = maincarodis.objects.all().order_by('date_added')

        return render(request, "packages.html", {'our': our1,
                                                 'packages': packages,

                                                 'team': team1,
                                                 'carosel': carosel_image1,
                                                 'main': maincarodis1,

                                                 })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive some data needed successfully'
        mes2 = 'Please refresh the page or try applying again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Page Failed To Load"
        backg = "rgba(94,86,97,0.8)"

    return render(request, "error_page.html", {'our': our1,
                                               'mes1': mes1,
                                               'mes2': mes2,
                                               'mes3': mes3,
                                               'mes4': mes4,
                                               'backg': backg
                                               }
                  )


def about(request):
    try:
        our1 = our.objects.all()
        packages = package.objects.all().order_by('price')
        team1 = team.objects.all()
        carosel_image1 = carosel_image.objects.all().order_by('date_added')
        maincarodis1 = maincarodis.objects.all().order_by('date_added')

        return render(request, "about.html", {'our': our1,
                                              'packages': packages,

                                              'team': team1,
                                              'carosel': carosel_image1,
                                              'main': maincarodis1,

                                              })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive some data needed successfully'
        mes2 = 'Please refresh the page or try applying again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Page Failed To Load"
        backg = "rgba(94,86,97,0.8)"

    return render(request, "error_page.html", {'our': our1,
                                               'mes1': mes1,
                                               'mes2': mes2,
                                               'mes3': mes3,
                                               'mes4': mes4,
                                               'backg': backg
                                               }
                  )


def contact(request):
    try:
        our1 = our.objects.all()
        packages = package.objects.all().order_by('price')
        team1 = team.objects.all()
        carosel_image1 = carosel_image.objects.all().order_by('date_added')
        maincarodis1 = maincarodis.objects.all().order_by('date_added')

        return render(request, "contact.html", {'our': our1,
                                                'packages': packages,

                                                'team': team1,
                                                'carosel': carosel_image1,
                                                'main': maincarodis1,

                                                })
    except Exception:
        our1 = our.objects.all()
        mes1 = 'Our servers could not receive some data needed successfully'
        mes2 = 'Please refresh the page or try applying again. If problem still persist, please contact us ' \
               'through ' \
               'any of our ' \
               'enquiry forms or through our call lines '
        mes3 = "OOOOP'S"
        mes4 = "Page Failed To Load"
        backg = "rgba(94,86,97,0.8)"

    return render(request, "error_page.html", {'our': our1,
                                               'mes1': mes1,
                                               'mes2': mes2,
                                               'mes3': mes3,
                                               'mes4': mes4,
                                               'backg': backg
                                               }
                  )
