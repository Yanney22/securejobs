# Register your models here.
from django.contrib import admin

from .models import company_name, package, our, carosel_image, company_category, job, customer_employemnt_stage, \
    customer_employemnt_document, customer, team, maincarodis, enquiry, online_order, department, staff, daily_report, \
    company_records_type, company_record, budget, customer_own_job_request, service, terms_condition, procument


class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'company_name',
                    'address',
                    'contact',
                    'email',
                    'date_added'
                    )

    search_fields = ('id',
                     'address',
                     'contact',
                     'email',
                     'date_added'
                     )


class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Year',
        'department_name',
        'total_amount_for_this_whole_year',
        'total_amount_per_january',
        'january_procuments',
        'january_salaries_for_staff',
        'total_cost_for_amenities_used_in_january',
        'january_advertisement_plans',
        'january_advertisement_plans_attained',

        'total_cost_of_january_advertisement_plans',
        'other_cost',

        'the_first_amenity_used_in_january',

        'total_cost1',
        'second_amenity_in_january',
        'total_cost2',
        'third_amenity_used_in_january',
        'total_cost3',
        'fourth_amenity_used_in_january_amenities',
        'total_cost4',
        'fifth_used_in_january_amenities',

        'sixth_used_in_january_amenities',
        'total_cost6',
        'seventh_used_in_january_amenities',
        'total_cost7',
        'the_eigth_used_in_january_amenities',
        'total_cost8',
        'nineth_used_in_january_amenities',
        'total_cost9',
        'tenth_used_in_january_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_february',
        'february_procuments',
        'february_salaries_for_staff',
        'total_cost_for_amenities_used_in_february',
        'february_advertisement_plans',
        'february_advertisement_plans_attained',
        'total_cost_of_february_advertisement_plans',

        'the_first_amenity_used_in_february',
        'total_cost1',
        'second_amenity_in_february',
        'total_cost2',
        'third_amenity_used_in_february',
        'total_cost3',
        'fourth_amenity_used_in_february_amenities',
        'total_cost4',
        'fifth_used_in_february_amenities',

        'sixth_used_in_february_amenities',
        'total_cost6',
        'seventh_used_in_february_amenities',
        'total_cost7',
        'the_eigth_used_in_february_amenities',
        'total_cost8',
        'nineth_used_in_february_amenities',
        'total_cost9',
        'tenth_used_in_february_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_march',
        'march_procuments',
        'march_salaries_for_staff',
        'total_cost_for_amenities_used_in_march',
        'march_advertisement_plans',
        'march_advertisement_plans_attained',
        'total_cost_of_march_advertisement_plans',

        'the_first_amenity_used_in_march',
        'total_cost1',
        'second_amenity_in_march',
        'total_cost2',
        'third_amenity_used_in_march',
        'total_cost3',
        'fourth_amenity_used_in_march_amenities',
        'total_cost4',
        'fifth_used_in_march_amenities',

        'sixth_used_in_march_amenities',
        'total_cost6',
        'seventh_used_in_march_amenities',
        'total_cost7',
        'the_eigth_used_in_march_amenities',
        'total_cost8',
        'nineth_used_in_march_amenities',
        'total_cost9',
        'tenth_used_in_march_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_april',
        'april_procuments',
        'april_salaries_for_staff',
        'total_cost_for_amenities_used_in_april',
        'april_advertisement_plans',
        'april_advertisement_plans_attained',
        'total_cost_of_april_advertisement_plans',

        'the_first_amenity_used_in_april',
        'total_cost1',
        'second_amenity_in_april',
        'total_cost2',
        'third_amenity_used_in_april',
        'total_cost3',
        'fourth_amenity_used_in_april_amenities',
        'total_cost4',
        'fifth_used_in_april_amenities',

        'sixth_used_in_april_amenities',
        'total_cost6',
        'seventh_used_in_april_amenities',
        'total_cost7',
        'the_eigth_used_in_april_amenities',
        'total_cost8',
        'nineth_used_in_april_amenities',
        'total_cost9',
        'tenth_used_in_april_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_may',
        'may_procuments',
        'may_salaries_for_staff',
        'total_cost_for_amenities_used_in_may',
        'may_advertisement_plans',
        'may_advertisement_plans_attained',
        'total_cost_of_may_advertisement_plans',

        'the_first_amenity_used_in_may',
        'total_cost1',
        'second_amenity_in_may',
        'total_cost2',
        'third_amenity_used_in_may',
        'total_cost3',
        'fourth_amenity_used_in_may_amenities',
        'total_cost4',
        'fifth_used_in_may_amenities',

        'sixth_used_in_may_amenities',
        'total_cost6',
        'seventh_used_in_may_amenities',
        'total_cost7',
        'the_eigth_used_in_may_amenities',
        'total_cost8',
        'nineth_used_in_may_amenities',
        'total_cost9',
        'tenth_used_in_may_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_june',
        'june_procuments',
        'june_salaries_for_staff',
        'total_cost_for_amenities_used_in_june',
        'june_advertisement_plans',
        'june_advertisement_plans_attained',
        'total_cost_of_june_advertisement_plans',

        'the_first_amenity_used_in_june',
        'total_cost1',
        'second_amenity_in_june',
        'total_cost2',
        'third_amenity_used_in_june',
        'total_cost3',
        'fourth_amenity_used_in_june_amenities',
        'total_cost4',
        'fifth_used_in_june_amenities',

        'sixth_used_in_june_amenities',
        'total_cost6',
        'seventh_used_in_june_amenities',
        'total_cost7',
        'the_eigth_used_in_june_amenities',
        'total_cost8',
        'nineth_used_in_june_amenities',
        'total_cost9',
        'tenth_used_in_june_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_july',
        'july_procuments',
        'july_salaries_for_staff',
        'total_cost_for_amenities_used_in_july',
        'july_advertisement_plans',
        'july_advertisement_plans_attained',
        'total_cost_of_july_advertisement_plans',

        'the_first_amenity_used_in_july',
        'total_cost1',
        'second_amenity_in_july',
        'total_cost2',
        'third_amenity_used_in_july',
        'total_cost3',
        'fourth_amenity_used_in_july_amenities',
        'total_cost4',
        'fifth_used_in_july_amenities',

        'sixth_used_in_july_amenities',
        'total_cost6',
        'seventh_used_in_july_amenities',
        'total_cost7',
        'the_eigth_used_in_july_amenities',
        'total_cost8',
        'nineth_used_in_july_amenities',
        'total_cost9',
        'tenth_used_in_july_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_august',
        'august_procuments',
        'august_salaries_for_staff',
        'total_cost_for_amenities_used_in_august',
        'august_advertisement_plans',
        'august_advertisement_plans_attained',
        'total_cost_of_august_advertisement_plans',

        'the_first_amenity_used_in_august',
        'total_cost1',
        'second_amenity_in_august',
        'total_cost2',
        'third_amenity_used_in_august',
        'total_cost3',
        'fourth_amenity_used_in_august_amenities',
        'total_cost4',
        'fifth_used_in_august_amenities',

        'sixth_used_in_august_amenities',
        'total_cost6',
        'seventh_used_in_august_amenities',
        'total_cost7',
        'the_eigth_used_in_august_amenities',
        'total_cost8',
        'nineth_used_in_august_amenities',
        'total_cost9',
        'tenth_used_in_august_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_september',
        'september_procuments',
        'september_salaries_for_staff',
        'total_cost_for_amenities_used_in_september',
        'september_advertisement_plans',
        'september_advertisement_plans_attained',
        'total_cost_of_september_advertisement_plans',

        'the_first_amenity_used_in_september',
        'total_cost1',
        'second_amenity_in_september',
        'total_cost2',
        'third_amenity_used_in_september',
        'total_cost3',
        'fourth_amenity_used_in_september_amenities',
        'total_cost4',
        'fifth_used_in_september_amenities',

        'sixth_used_in_september_amenities',
        'total_cost6',
        'seventh_used_in_september_amenities',
        'total_cost7',
        'the_eigth_used_in_september_amenities',
        'total_cost8',
        'nineth_used_in_september_amenities',
        'total_cost9',
        'tenth_used_in_september_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_october',
        'october_procuments',
        'october_salaries_for_staff',
        'total_cost_for_amenities_used_in_october',
        'october_advertisement_plans',
        'october_advertisement_plans_attained',
        'total_cost_of_october_advertisement_plans',

        'the_first_amenity_used_in_october',
        'total_cost1',
        'second_amenity_in_october',
        'total_cost2',
        'third_amenity_used_in_october',
        'total_cost3',
        'fourth_amenity_used_in_october_amenities',
        'total_cost4',
        'fifth_used_in_october_amenities',

        'sixth_used_in_october_amenities',
        'total_cost6',
        'seventh_used_in_october_amenities',
        'total_cost7',
        'the_eigth_used_in_october_amenities',
        'total_cost8',
        'nineth_used_in_october_amenities',
        'total_cost9',
        'tenth_used_in_october_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_november',
        'november_procuments',
        'november_salaries_for_staff',
        'total_cost_for_amenities_used_in_november',
        'november_advertisement_plans',
        'november_advertisement_plans_attained',
        'total_cost_of_november_advertisement_plans',

        'the_first_amenity_used_in_november',
        'total_cost1',
        'second_amenity_in_november',
        'total_cost2',
        'third_amenity_used_in_november',
        'total_cost3',
        'fourth_amenity_used_in_november_amenities',
        'total_cost4',
        'fifth_used_in_november_amenities',

        'sixth_used_in_november_amenities',
        'total_cost6',
        'seventh_used_in_november_amenities',
        'total_cost7',
        'the_eigth_used_in_november_amenities',
        'total_cost8',
        'nineth_used_in_november_amenities',
        'total_cost9',
        'tenth_used_in_november_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_december',
        'december_procuments',
        'december_salaries_for_staff',
        'total_cost_for_amenities_used_in_december',
        'december_advertisement_plans',
        'december_advertisement_plans_attained',
        'total_cost_of_december_advertisement_plans',

        'the_first_amenity_used_in_december',
        'total_cost1',
        'second_amenity_in_december',
        'total_cost2',
        'third_amenity_used_in_december',
        'total_cost3',
        'fourth_amenity_used_in_december_amenities',
        'total_cost4',
        'fifth_used_in_december_amenities',

        'sixth_used_in_december_amenities',
        'total_cost6',
        'seventh_used_in_december_amenities',
        'total_cost7',
        'the_eigth_used_in_december_amenities',
        'total_cost8',
        'nineth_used_in_december_amenities',
        'total_cost9',
        'tenth_used_in_december_amenities',
        'total_cost10',
        'other_cost',

        'total_staff_salaries',
        'date_added')

    search_fields = (
        'id',
        'Year',
        'department_name',
        'total_amount_for_this_whole_year',
        'total_amount_per_january',
        'january_procuments',
        'january_salaries_for_staff',
        'total_cost_for_amenities_used_in_january',
        'january_advertisement_plans',
        'january_advertisement_plans_attained',

        'total_cost_of_january_advertisement_plans',
        'other_cost',

        'the_first_amenity_used_in_january',

        'total_cost1',
        'second_amenity_in_january',
        'total_cost2',
        'third_amenity_used_in_january',
        'total_cost3',
        'fourth_amenity_used_in_january_amenities',
        'total_cost4',
        'fifth_used_in_january_amenities',

        'sixth_used_in_january_amenities',
        'total_cost6',
        'seventh_used_in_january_amenities',
        'total_cost7',
        'the_eigth_used_in_january_amenities',
        'total_cost8',
        'nineth_used_in_january_amenities',
        'total_cost9',
        'tenth_used_in_january_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_february',
        'february_procuments',
        'february_salaries_for_staff',
        'total_cost_for_amenities_used_in_february',
        'february_advertisement_plans',
        'february_advertisement_plans_attained',
        'total_cost_of_february_advertisement_plans',

        'the_first_amenity_used_in_february',
        'total_cost1',
        'second_amenity_in_february',
        'total_cost2',
        'third_amenity_used_in_february',
        'total_cost3',
        'fourth_amenity_used_in_february_amenities',
        'total_cost4',
        'fifth_used_in_february_amenities',

        'sixth_used_in_february_amenities',
        'total_cost6',
        'seventh_used_in_february_amenities',
        'total_cost7',
        'the_eigth_used_in_february_amenities',
        'total_cost8',
        'nineth_used_in_february_amenities',
        'total_cost9',
        'tenth_used_in_february_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_march',
        'march_procuments',
        'march_salaries_for_staff',
        'total_cost_for_amenities_used_in_march',
        'march_advertisement_plans',
        'march_advertisement_plans_attained',
        'total_cost_of_march_advertisement_plans',

        'the_first_amenity_used_in_march',
        'total_cost1',
        'second_amenity_in_march',
        'total_cost2',
        'third_amenity_used_in_march',
        'total_cost3',
        'fourth_amenity_used_in_march_amenities',
        'total_cost4',
        'fifth_used_in_march_amenities',

        'sixth_used_in_march_amenities',
        'total_cost6',
        'seventh_used_in_march_amenities',
        'total_cost7',
        'the_eigth_used_in_march_amenities',
        'total_cost8',
        'nineth_used_in_march_amenities',
        'total_cost9',
        'tenth_used_in_march_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_april',
        'april_procuments',
        'april_salaries_for_staff',
        'total_cost_for_amenities_used_in_april',
        'april_advertisement_plans',
        'april_advertisement_plans_attained',
        'total_cost_of_april_advertisement_plans',

        'the_first_amenity_used_in_april',
        'total_cost1',
        'second_amenity_in_april',
        'total_cost2',
        'third_amenity_used_in_april',
        'total_cost3',
        'fourth_amenity_used_in_april_amenities',
        'total_cost4',
        'fifth_used_in_april_amenities',

        'sixth_used_in_april_amenities',
        'total_cost6',
        'seventh_used_in_april_amenities',
        'total_cost7',
        'the_eigth_used_in_april_amenities',
        'total_cost8',
        'nineth_used_in_april_amenities',
        'total_cost9',
        'tenth_used_in_april_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_may',
        'may_procuments',
        'may_salaries_for_staff',
        'total_cost_for_amenities_used_in_may',
        'may_advertisement_plans',
        'may_advertisement_plans_attained',
        'total_cost_of_may_advertisement_plans',

        'the_first_amenity_used_in_may',
        'total_cost1',
        'second_amenity_in_may',
        'total_cost2',
        'third_amenity_used_in_may',
        'total_cost3',
        'fourth_amenity_used_in_may_amenities',
        'total_cost4',
        'fifth_used_in_may_amenities',

        'sixth_used_in_may_amenities',
        'total_cost6',
        'seventh_used_in_may_amenities',
        'total_cost7',
        'the_eigth_used_in_may_amenities',
        'total_cost8',
        'nineth_used_in_may_amenities',
        'total_cost9',
        'tenth_used_in_may_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_june',
        'june_procuments',
        'june_salaries_for_staff',
        'total_cost_for_amenities_used_in_june',
        'june_advertisement_plans',
        'june_advertisement_plans_attained',
        'total_cost_of_june_advertisement_plans',

        'the_first_amenity_used_in_june',
        'total_cost1',
        'second_amenity_in_june',
        'total_cost2',
        'third_amenity_used_in_june',
        'total_cost3',
        'fourth_amenity_used_in_june_amenities',
        'total_cost4',
        'fifth_used_in_june_amenities',

        'sixth_used_in_june_amenities',
        'total_cost6',
        'seventh_used_in_june_amenities',
        'total_cost7',
        'the_eigth_used_in_june_amenities',
        'total_cost8',
        'nineth_used_in_june_amenities',
        'total_cost9',
        'tenth_used_in_june_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_july',
        'july_procuments',
        'july_salaries_for_staff',
        'total_cost_for_amenities_used_in_july',
        'july_advertisement_plans',
        'july_advertisement_plans_attained',
        'total_cost_of_july_advertisement_plans',

        'the_first_amenity_used_in_july',
        'total_cost1',
        'second_amenity_in_july',
        'total_cost2',
        'third_amenity_used_in_july',
        'total_cost3',
        'fourth_amenity_used_in_july_amenities',
        'total_cost4',
        'fifth_used_in_july_amenities',

        'sixth_used_in_july_amenities',
        'total_cost6',
        'seventh_used_in_july_amenities',
        'total_cost7',
        'the_eigth_used_in_july_amenities',
        'total_cost8',
        'nineth_used_in_july_amenities',
        'total_cost9',
        'tenth_used_in_july_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_august',
        'august_procuments',
        'august_salaries_for_staff',
        'total_cost_for_amenities_used_in_august',
        'august_advertisement_plans',
        'august_advertisement_plans_attained',
        'total_cost_of_august_advertisement_plans',

        'the_first_amenity_used_in_august',
        'total_cost1',
        'second_amenity_in_august',
        'total_cost2',
        'third_amenity_used_in_august',
        'total_cost3',
        'fourth_amenity_used_in_august_amenities',
        'total_cost4',
        'fifth_used_in_august_amenities',

        'sixth_used_in_august_amenities',
        'total_cost6',
        'seventh_used_in_august_amenities',
        'total_cost7',
        'the_eigth_used_in_august_amenities',
        'total_cost8',
        'nineth_used_in_august_amenities',
        'total_cost9',
        'tenth_used_in_august_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_september',
        'september_procuments',
        'september_salaries_for_staff',
        'total_cost_for_amenities_used_in_september',
        'september_advertisement_plans',
        'september_advertisement_plans_attained',
        'total_cost_of_september_advertisement_plans',

        'the_first_amenity_used_in_september',
        'total_cost1',
        'second_amenity_in_september',
        'total_cost2',
        'third_amenity_used_in_september',
        'total_cost3',
        'fourth_amenity_used_in_september_amenities',
        'total_cost4',
        'fifth_used_in_september_amenities',

        'sixth_used_in_september_amenities',
        'total_cost6',
        'seventh_used_in_september_amenities',
        'total_cost7',
        'the_eigth_used_in_september_amenities',
        'total_cost8',
        'nineth_used_in_september_amenities',
        'total_cost9',
        'tenth_used_in_september_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_october',
        'october_procuments',
        'october_salaries_for_staff',
        'total_cost_for_amenities_used_in_october',
        'october_advertisement_plans',
        'october_advertisement_plans_attained',
        'total_cost_of_october_advertisement_plans',

        'the_first_amenity_used_in_october',
        'total_cost1',
        'second_amenity_in_october',
        'total_cost2',
        'third_amenity_used_in_october',
        'total_cost3',
        'fourth_amenity_used_in_october_amenities',
        'total_cost4',
        'fifth_used_in_october_amenities',

        'sixth_used_in_october_amenities',
        'total_cost6',
        'seventh_used_in_october_amenities',
        'total_cost7',
        'the_eigth_used_in_october_amenities',
        'total_cost8',
        'nineth_used_in_october_amenities',
        'total_cost9',
        'tenth_used_in_october_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_november',
        'november_procuments',
        'november_salaries_for_staff',
        'total_cost_for_amenities_used_in_november',
        'november_advertisement_plans',
        'november_advertisement_plans_attained',
        'total_cost_of_november_advertisement_plans',

        'the_first_amenity_used_in_november',
        'total_cost1',
        'second_amenity_in_november',
        'total_cost2',
        'third_amenity_used_in_november',
        'total_cost3',
        'fourth_amenity_used_in_november_amenities',
        'total_cost4',
        'fifth_used_in_november_amenities',

        'sixth_used_in_november_amenities',
        'total_cost6',
        'seventh_used_in_november_amenities',
        'total_cost7',
        'the_eigth_used_in_november_amenities',
        'total_cost8',
        'nineth_used_in_november_amenities',
        'total_cost9',
        'tenth_used_in_november_amenities',
        'total_cost10',
        'other_cost',

        'total_amount_per_december',
        'december_procuments',
        'december_salaries_for_staff',
        'total_cost_for_amenities_used_in_december',
        'december_advertisement_plans',
        'december_advertisement_plans_attained',
        'total_cost_of_december_advertisement_plans',

        'the_first_amenity_used_in_december',
        'total_cost1',
        'second_amenity_in_december',
        'total_cost2',
        'third_amenity_used_in_december',
        'total_cost3',
        'fourth_amenity_used_in_december_amenities',
        'total_cost4',
        'fifth_used_in_december_amenities',

        'sixth_used_in_december_amenities',
        'total_cost6',
        'seventh_used_in_december_amenities',
        'total_cost7',
        'the_eigth_used_in_december_amenities',
        'total_cost8',
        'nineth_used_in_december_amenities',
        'total_cost9',
        'tenth_used_in_december_amenities',
        'total_cost10',
        'other_cost',

        'total_staff_salaries',
        'date_added')

    list_filter = ('Year',
                   'department_name',
                   'total_amount_for_this_whole_year',
                   'date_added')


class packagesAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'plan_name',
                    'individual_limit',
                    'price',
                    'days_to_get_job',
                    'plan_description1',
                    'plan_description2',
                    'plan_description3',
                    'plan_description4',
                    'plan_description5',
                    'plan_description6',
                    'plan_description7',
                    'plan_description8',
                    'plan_description9',
                    'plan_description10',
                    'date_added'
                    )

    search_fields = ('id',
                     'plan_name',
                     'individual_limit',
                     'price',
                     'days_to_get_job',
                     'plan_description1',
                     'plan_description2',
                     'plan_description3',
                     'plan_description4',
                     'plan_description5',
                     'plan_description6',
                     'plan_description7',
                     'plan_description8',
                     'plan_description9',
                     'plan_description10',
                     'date_added'
                     )
    list_filter = (
        "individual_limit",
        'date_added'
    )


class OurAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'location',
                    'happy_clents',
                    'partners',
                    'awards_won',
                    'travels_customer_document',
                    'other_customer_documents_submit',
                    'phonenumber',
                    'phonenumber2',
                    'facebookaddress',
                    'instagramaddress',

                    'date_added'
                    )

    search_fields = ('id',
                     'name',
                     'happy_clents',
                     'partners',
                     'awards_won',
                     'travels_customer_document',
                     'other_customer_documents_submit',
                     'phonenumber',
                     'phonenumber2',
                     'date_added'
                     )


class Caroselimage(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'img',
                    'date_added'
                    )

    search_fields = ('id',
                     'name',
                     'img',
                     'date_added'
                     )


class CompanyCat(admin.ModelAdmin):
    list_display = ('id',
                    'company_category',
                    'date_added',
                    )

    search_fields = ('id',
                     'company_category',
                     'date_added',
                     )


class JobAdmin(admin.ModelAdmin):
    list_display = ('Id',
                    'company_name',

                    'location',
                    'company_category',
                    'company_image',
                    'job_offer1',
                    'job_offer2',
                    'job_offer3',
                    'job_offer4',
                    'job_offer5',
                    'job_offer6',
                    'job_offer7',
                    'job_offer8',
                    'job_offer9',
                    'job_offer10',
                    'job_offer11',
                    'job_offer12',
                    'job_offer13',
                    'job_offer14',
                    'job_offer15',
                    'job_offer16',
                    'job_offer17',
                    'job_offer18',
                    'job_offer19',
                    'job_offer20',
                    'min_salary',
                    'max_salary',

                    'date_added',
                    'deadline'

                    )
    search_fields = ('Id',
                     'company_name__company_name',
                     'job_offer1',
                     'location',
                     'company_category__company_category',
                     'deadline',
                     )
    list_filter = ('company_name__company_name',
                   'job_offer1',
                   'date_added',
                   'deadline',
                   'company_category__company_category'

                   )

    list_editable = (

        'location',
        'company_category',
        'date_added',
        'deadline')


class TermsConditionsAdmin(admin.ModelAdmin):
    list_display = ('serv_name',
                    'serv_policy',
                    'date_added')
    search_fields = \
        ('serv_name',
         'serv_policy',
         'date_added')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'full_name',
                    'gender',
                    'date_of_birth',
                    'cv',
                    'voters_id',
                    'department_name',
                    'employement_contract',
                    'salary',
                    'current_employment_status',
                    'date_employed',
                    'date_of_resignation',
                    'HR_employed_under')

    search_fields = ('id',
                     'full_name',
                     'gender',
                     'date_of_birth',
                     'cv',
                     'voters_id',
                     'department_name',
                     'employement_contract',
                     'salary',
                     'current_employment_status',
                     'date_employed',
                     'date_of_resignation',
                     'HR_employed_under')

    list_filter = (
        'gender',
        'date_of_birth',

        'department_name',

        'salary',
        'current_employment_status',
        'date_employed',
        'date_of_resignation',
        'HR_employed_under')


class DailyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'department_name',
        'staff_name',
        'what_you_did',
        'total',
        'total_cost_if_any',
        'money_gained'
    )

    search_fields = (
        'id',
        'date',
        'department_name',
        'staff_name',
        'what_you_did',
        'total',
        'total_cost_if_any',
        'money_gained'
    )

    list_filter = ('date',
                   'department_name',
                   'staff_name'
                   )


class EmpAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'employemnt_stage',
                    'date_added'
                    )

    search_fields = ('id',
                     'employemnt_stage',
                     'date_added',
                     )


class Empdoc(admin.ModelAdmin):
    list_display = ('id',
                    'employemnt_document',
                    'date_added'
                    )

    search_fields = ('id',
                     'employemnt_document',
                     'date_added',
                     )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'fullname',
                    'designation',
                    'picture'
                    )

    search_fields = ('id',
                     'fullname',
                     'designation',
                     'picture'
                     )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'customer_name',

                    'Date_of_Birth',
                    'address',
                    'phone_number',
                    'occupation',
                    'package_choosen',
                    'amount_paid',

                    'acadamic_level',
                    'employemnet_form',
                    'other_document',
                    'other_document2',
                    'formal_employee',
                    'current_employement_stage',
                    'company_which_employed_customer',
                    'customer_salary',

                    'amount_to_deduct_from_salary',

                    'period_to_deduct',
                    'starting_date_to_deduct',
                    'next_date_to_deduct',
                    'current_number_of_month_deducted',
                    'guarantor_name',
                    'guarantor_address',
                    'guarantor_contacts',
                    'next_of_kin',
                    'activation_code',
                    'Archive',
                    'workstatus'

                    )

    search_fields = (
        'id',
        'customer_name',
        'address',
        'phone_number',
        'guarantor_name',
        'guarantor_address',
        'guarantor_contacts',
        'next_of_kin',
        'activation_code',
        'Archive',
        'workstatus'

    )
    list_filter = (
        'package_choosen',
        'acadamic_level',
        'occupation',
        'current_employement_stage',
        'company_which_employed_customer',
        'customer_salary',
        'starting_date_to_deduct',
        'next_date_to_deduct',
        'Archive',
        'workstatus'

    )


class MainCarosedis(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'img',
                    'date_added'
                    )

    search_fields = ('id',
                     'name',
                     'img',
                     'date_added'
                     )


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'fullname',
                    'phonenumber',
                    'emailaddress',
                    'option',
                    'message',
                    'date_added',
                    'read'
                    )

    search_fields = ('id',
                     'fullname',
                     'phonenumber',
                     'emailaddress',
                     'option',
                     'message',
                     'date_added',
                     'read'
                     )
    list_filter = (
        'option',
        'date_added',
        'read'
    )


class onlineorderAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'company_name',
                    'job_ID',
                    'company_category',
                    'fullname',
                    'phonenumber',
                    'email',
                    'pack_choosen',
                    'cv',
                    'jobexpect',
                    'salaryexpect',
                    'date_added',
                    'read',
                    'accepted',
                    'activation_code',
                    'starting_date'

                    )

    search_fields = ('id',
                     'fullname',
                     'phonenumber',
                     'email',
                     'pack_choosen',
                     'cv',
                     'jobexpect',
                     'salaryexpect',
                     'date_added',
                     'read',
                     'accepted',
                     'activation_code',
                     'starting_date'
                     )
    list_filter = (
        'pack_choosen',
        'date_added',
        'read',
        'accepted',
        'starting_date'

    )


class DepartAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'department_name',
                    'date_added'
                    )

    search_fields = ('id',
                     'department_name',
                     'date_added'
                     )


class ProcumentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product_brought',
        'cost',
        'price_per_unit',
        'store_bought',
        'personnel_in_charge_of_purchase',
        'accountant_in_charge_of_purchase',
        'quantity',
        'day_bought',
        'location_stored_at',
        'date_added')

    search_fields = (
        'id',
        'product_brought',
        'cost',
        'price_per_unit',
        'store_bought',
        'personnel_in_charge_of_purchase',
        'accountant_in_charge_of_purchase',
        'quantity',
        'day_bought',
        'location_stored_at',
        'date_added')
    list_filter = (
        'date_added',
        'location_stored_at'
    )


class ComRegAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'documentname',
        'date_added'
    )
    search_fields = (
        'id',
        'documentname',
        'date_added'
    )


class CrecAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'document_name',
        'document_type',
        'for_what_department',

        'Doc_1',
        'document1',

        'Doc_2',
        'document2',
        'Doc_3',
        'document3',
        'Doc_4',
        'document4',
        'Doc_5',
        'document5',
        'Doc_6',
        'document6',
        'Doc_7',
        'document7',
        'Doc_8',
        'document8',
        'Doc_9',
        'document9',
        'Doc_10',
        'document10',

        'Doc_11',
        'document11',
        'Doc_12',
        'document12',
        'Doc_13',
        'document13',
        'Doc_14',
        'document14',
        'Doc_15',
        'document15',
        'Doc_16',
        'document17',
        'Doc_17',
        'document18',
        'Doc_18',
        'document18',
        'Doc_19',
        'document19',
        'Doc_20',
        'document20',
        'date_added')

    search_fields = (
        'id',
        'document_name',
        'document_type',
        'for_what_department',

        'Doc_1',
        'document1',

        'Doc_2',
        'document2',
        'Doc_3',
        'document3',
        'Doc_4',
        'document4',
        'Doc_5',
        'document5',
        'Doc_6',
        'document6',
        'Doc_7',
        'document7',
        'Doc_8',
        'document8',
        'Doc_9',
        'document9',
        'Doc_10',
        'document10',

        'Doc_11',
        'document11',
        'Doc_12',
        'document12',
        'Doc_13',
        'document13',
        'Doc_14',
        'document14',
        'Doc_15',
        'document15',
        'Doc_16',
        'document16',
        'Doc_17',
        'document17',
        'Doc_18',
        'document18',
        'Doc_19',
        'document19',
        'Doc_20',
        'document20',
        'date_added')

    list_filter = ('document_name',
                   'document_type',
                   'for_what_department',
                   'date_added'
                   )


class CustomerOwnJobAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fullname',
        'email',
        'phonenumber',
        'pack_choosen',
        'cv',
        'jobexpect',
        'salaryexpect',
        'date_added',
        'read',
        'accepted',
        'company_that_the_customer_will_be_placed_in',
        'location_of_company',
        'actual_salary',
        'activation_code',
        'starting_date'

    )


    search_fields = (
        'id',
        'fullname',
        'email',
        'phonenumber',
        'pack_choosen',
        'cv',
        'jobexpect',
        'salaryexpect',
        'date_added',
        'read',
        'accepted',
        'company_that_the_customer_will_be_placed_in',
        'location_of_company',
        'actual_salary',
        'activation_code',
        'starting_date')

    list_filter = (
        'pack_choosen',
        'date_added',
        'read',
        'accepted',
        'starting_date'

    )


class SevicesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'services_name',
        'img',
        'about_service',
        'date_added'
    )
    search_fields = (
        'id',
        'services_name',
        'img',
        'about_service',
        'date_added'
    )


admin.site.register(terms_condition, TermsConditionsAdmin)
admin.site.register(service, SevicesAdmin)
admin.site.register(customer_own_job_request, CustomerOwnJobAdmin)
admin.site.register(budget, BudgetAdmin)

admin.site.register(company_record, CrecAdmin)
admin.site.register(company_records_type, ComRegAdmin)
admin.site.register(daily_report, DailyAdmin)
admin.site.register(staff, StaffAdmin)
admin.site.register(department, DepartAdmin)
admin.site.register(enquiry, EnquiryAdmin)
admin.site.register(online_order, onlineorderAdmin)
admin.site.register(procument, ProcumentAdmin)
admin.site.register(company_name, CompanyNameAdmin)
admin.site.register(package, packagesAdmin)
admin.site.register(our, OurAdmin)
admin.site.register(carosel_image, Caroselimage)
admin.site.register(maincarodis, MainCarosedis)
admin.site.register(company_category, CompanyCat)
admin.site.register(job, JobAdmin)
admin.site.register(customer_employemnt_stage, EmpAdmin)
admin.site.register(customer_employemnt_document, Empdoc)

admin.site.register(customer, CustomerAdmin)

admin.site.register(team, TeamAdmin)
