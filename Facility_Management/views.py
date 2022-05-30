import datetime

import ipware
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render

from Facility_Management.models import *
from home.models import *
# Create your views here.
from securejobs import settings


def facility_management(request):
    try:
        code1 = request.session.get('code', 'null')
        if code1 != 'null':
            del request.session['code']
        our1 = our.objects.all()
        mes1 = "Please Enter Your Company Identity Code Below"
        col1 = "black"
        return render(request, "facility_management_activation.html", {'our': our1,
                                                                       'mes': mes1,
                                                                       'col': col1

                                                                       })
    except Exception:
        a = ''


def order_facility(request):
    try:
        our1 = our.objects.all()
        try:
            code1 = request.GET['code']
        except Exception:
            code1 = request.session.get('code')
        try:
            today = request.GET['today']
        except Exception:
            today = request.session.get('today')

        codi = ""
        mes1 = "Please Enter Your Company Identity Code Below"
        today1 = datetime.datetime.now()
        your_ip = ipware.get_client_ip(request)
        maincarodis1 = facility_maincarodis.objects.all().order_by('date_added')

        services = facility_management_service.objects.all().order_by("-date_added")

        fac1 = facility_management_client.objects.filter(Q(company_identity_code__exact=code1))

        if fac1:

            cname1 = fac1.all()
            for i in cname1:
                the_cat = i.category
                the_name = i.company_name
                the_code = i.company_identity_code
                the_email = i.email
                the_contact = i.contact

            if request.method == "GET":
                codi = request.session.get('code', 'null')
            if codi != "null":
                facilty_management_category1 = facilty_management_category.objects.all()
                facilty_management_item1 = facilty_management_item.objects.all().order_by("item_name")
                h1_mes = "What do you want to order for today"
                col1 = "dodgerblue"
                return render(request, "facility_management.html",

                              {'our': our1,

                               'cname': cname1,
                               'main': maincarodis1,
                               'service': services,
                               'fac': facilty_management_category1,
                               'fac2': facilty_management_item1,
                               'h1_mes': h1_mes,
                               'col1': col1,
                               'today': today

                               })
            else:

                request.session['code'] = code1
                theirlogin = facility_management_clients_login()
                theirlogin.category = the_cat
                theirlogin.company_name = the_name
                theirlogin.company_identity_code = the_code
                theirlogin.email = the_email
                theirlogin.client_login_address = your_ip
                theirlogin.contact = the_contact
                theirlogin.date_time_login = today1

                theirlogin.save()
                facilty_management_category1 = facilty_management_category.objects.all()
                facilty_management_item1 = facilty_management_item.objects.all().order_by("item_name")
                request.session['today'] = str(today1)
                h1_mes = "What do you want to order for today"
                col1 = "dodgerblue"
                return render(request, "facility_management.html",

                              {'our': our1,

                               'cname': cname1,
                               'main': maincarodis1,
                               'service': services,
                               'fac': facilty_management_category1,
                               'fac2': facilty_management_item1,
                               'h1_mes': h1_mes,
                               'col1': col1,
                               'today': today1

                               })



        else:
            mes1 = "Incorrect Company Identity Code"
            col1 = "darkred"
            return render(request, "facility_management_activation.html", {'our': our1,
                                                                           'mes': mes1,
                                                                           'col': col1
                                                                           })
    except Exception:
     code1 = request.session.get('code', 'null')
    if code1 != 'null':
        del request.session['code']
    our1 = our.objects.all()
    mes1 = "Please Enter Your Company Identity Code Below"
    col1 = "black"
    return render(request, "facility_management_activation.html", {'our': our1,
                                                                   'mes': mes1,
                                                                   'col': col1

                                                                   })

def facility_management_client_order(request):
    our1 = our.objects.all()
    today = datetime.datetime.now()
    maincarodis1 = facility_maincarodis.objects.all().order_by('date_added')
    services = facility_management_service.objects.all().order_by("-date_added")

    if request.method == "POST":
        cust_name = request.POST['cname']
        ccat = request.POST['ccat']

        datetime_local1 = request.POST['clientordertime']
        option1 = request.POST['option1']
        quantity1 = request.POST['quantity1']
        # -------------
        option2 = request.POST['option2']
        quantity2 = request.POST['quantity2']
        # ------------------------
        option3 = request.POST['option3']
        quantity3 = request.POST['quantity3']
        # ------------------
        option4 = request.POST['option4']
        quantity4 = request.POST['quantity4']
        # ---------------------
        option5 = request.POST['option5']
        quantity5 = request.POST['quantity5']
        # ------------------------------
        option6 = request.POST['option6']
        quantity6 = request.POST['quantity6']
        # ----------------------------------
        option7 = request.POST['option7']
        quantity7 = request.POST['quantity7']
        # _______________________________
        option8 = request.POST['option8']
        quantity8 = request.POST['quantity8']
        # -----------------
        option9 = request.POST['option9']
        quantity9 = request.POST['quantity9']
        # ------------------------------------
        option10 = request.POST['option10']
        quantity10 = request.POST['quantity10']
        # -------------------------------------
        companyorderpassword = request.POST['companyorderpassword']
        message = request.POST['message']
        date_added = today

        try:
            codi = request.GET['code']
        except Exception:
            codi = request.session.get('code')
        try:
            today = request.GET['today']
        except Exception:
            today = request.session.get('today')

        checking = facility_management_client.objects.filter(company_name__company_name__exact=cust_name,
                                                             company_identity_code__exact=codi,
                                                             company_order_password__exact=companyorderpassword
                                                             )

        if checking:
            yourorder = facility_management_order()
            yourorder.cust_name = cust_name
            yourorder.category = ccat
            yourorder.datetime_local = datetime_local1
            # _______________________
            yourorder.option1 = option1
            yourorder.quantity1 = quantity1
            # _____________________________
            yourorder.option2 = option2
            yourorder.quantity2 = quantity2
            # _______________________
            yourorder.option3 = option3
            yourorder.quantity3 = quantity3
            # ___________
            yourorder.option4 = option4
            yourorder.quantity4 = quantity4
            # _____________________
            yourorder.option5 = option5
            yourorder.quantity5 = quantity5
            # __________________________
            yourorder.option6 = option6
            yourorder.quantity6 = quantity6
            # _____________________________
            yourorder.option7 = option7
            yourorder.quantity7 = quantity7
            # ___________________________
            yourorder.option8 = option8
            yourorder.quantity8 = quantity8
            # __________________________
            yourorder.option9 = option9
            yourorder.quantity9 = quantity9
            # ___________________________
            yourorder.option10 = option10
            yourorder.quantity10 = quantity10
            # ____________________________
            yourorder.companyorderpassword = companyorderpassword
            yourorder.message = message
            yourorder.date_added = date_added
            yourorder.save()

            cname1 = checking.all()
            for i in cname1:
                emailaddress = i.email
                company_name = i.company_name

            messages.success(request,
                             f"New Facility Management order from {company_name}")
            # Email

            subject = "Secure Express Ghana Order"

            message = f'Dear {company_name},your order has been received successfully.' \
                      f'Thank you for using Secure Express'
            from_email = settings.EMAIL_HOST_USER
            to_list = [emailaddress]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            mes1 = "Order Received Successfully"
            col1 = "darkgreen"
            facilty_management_category1 = facilty_management_category.objects.all()
            facilty_management_item1 = facilty_management_item.objects.all().order_by("item_name")

            return render(request, 'facility_management_orderincorrect.html', {'our': our1,

                                                                               'cname': cname1,
                                                                               'main': maincarodis1,
                                                                               'service': services,
                                                                               'fac': facilty_management_category1,
                                                                               'fac2': facilty_management_item1,
                                                                               'h1_mes': mes1,
                                                                               'col1': col1,
                                                                               'today': today

                                                                               })

        else:
            our1 = our.objects.all()
            code1 = request.session.get('code', 'null')
            if code1 != 'null':

                mes1 = "Incorrect Company Order Password"
                col1 = "darkred"
                maincarodis1 = facility_maincarodis.objects.all().order_by('date_added')

                services = facility_management_service.objects.all().order_by("-date_added")

                giti = facility_management_client.objects.filter(
                    company_identity_code__exact=codi
                )
                facilty_management_category1 = facilty_management_category.objects.all()
                facilty_management_item1 = facilty_management_item.objects.all().order_by("item_name")
                cname1 = giti.all()
                try:
                    today = request.GET['today']
                except Exception:
                    today = request.session.get('today')
                return render(request, 'facility_management_orderincorrect.html', {'our': our1,

                                                                                   'cname': cname1,
                                                                                   'main': maincarodis1,
                                                                                   'service': services,
                                                                                   'fac': facilty_management_category1,
                                                                                   'fac2': facilty_management_item1,
                                                                                   'h1_mes': mes1,
                                                                                   'col1': col1,
                                                                                   'today': today
                                                                                   })



    else:

        codi = request.session['code']
        our1 = our.objects.all()
        col1 = "dodgerblue"
        maincarodis1 = facility_maincarodis.objects.all().order_by('date_added')
        services = facility_management_service.objects.all().order_by("-date_added")

        h1_mes = "What do you want to order for today"
        fac1 = facility_management_client.objects.filter(
            company_identity_code__exact=codi
        )

        if fac1:

            cname1 = fac1.all()

            del request.session['code']
            for i in cname1:
                request.session['code'] = i.company_identity_code
        facilty_management_category1 = facilty_management_category.objects.all()
        facilty_management_item1 = facilty_management_item.objects.all().order_by("item_name")
        try:
            today = request.GET['today']
        except Exception:
            today = request.session.get('today')
        return render(request, "facility_management.html",

                      {'our': our1,

                       'cname': cname1,
                       'main': maincarodis1,
                       'service': services,
                       'fac': facilty_management_category1,
                       'fac2': facilty_management_item1,
                       'h1_mes': h1_mes,
                       'col1': col1,
                       'today': today

                       })


def facility_logout(request):
  try:
        try:
            code1 = request.GET['code']
        except Exception:
            code1 = request.session.get('code')
        try:
            today = request.GET['today']
        except Exception:
            today = request.session.get('today')

        rightnow = datetime.datetime.now()

        checking = facility_management_clients_login.objects.filter(company_identity_code__exact=code1,
                                                                    date_time_login__exact=today)
        cname1 = checking.all()
        for i in cname1:
            myid = i.Id
            comcategory = i.category
            company_name = i.company_name
            emaili = i.email
            firstip = i.client_login_address
            yocontact = i.contact
        if request.method == "POST" or request.method == "GET":
            if checking != 'null':
                reg = facility_management_clients_login(
                    Id=myid,
                    category=comcategory,
                    company_name=company_name,
                    email=emaili,
                    client_login_address=firstip,
                    company_identity_code=code1,
                    date_time_login=today,
                    contact=yocontact,
                    date_time_logout=rightnow
                )
                reg.save()
                del request.session['code']
                del request.session['today']

                our1 = our.objects.all()
                mes1 = "You have successfully logout"
                col1 = "darkgreen"
                return render(request, "facility_management_activation.html", {'our': our1,
                                                                               'mes': mes1,
                                                                               'col': col1
                                                                               })




  except Exception:
      code1 = request.session.get('code', 'null')
      if code1 != 'null':
          del request.session['code']
      our1 = our.objects.all()
      mes1 = "Please Enter Your Company Identity Code Below"
      col1 = "black"
      return render(request, "facility_management_activation.html", {'our': our1,
                                                                     'mes': mes1,
                                                                     'col': col1

                                                                     })