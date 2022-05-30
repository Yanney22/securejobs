# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class department(models.Model):
    department_name = models.CharField('Name of Department', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.department_name

    @staticmethod
    def autocomplete_search_fields():
        return 'department_name', 'date_added'


class staff(models.Model):
    full_name = models.CharField('Name of Staff', max_length=200)
    gender = models.CharField('Gender', max_length=200)
    date_of_birth = models.DateField()
    cv = models.FileField(upload_to=f"static\staffs\documents")
    voters_id = models.FileField(upload_to=f"static\staffs\documents")
    department_name = models.ForeignKey(department, on_delete=models.CASCADE)
    employement_contract = models.FileField(null=True, blank=True, upload_to=f"static\staffs\employement\contract")
    salary = models.FloatField('Salary of Staff')
    current_employment_status = models.BooleanField("Active")
    date_employed = models.DateField()
    date_of_resignation = models.DateField()
    HR_employed_under = models.CharField('Name of the Human Resource Manager Employed Under', max_length=200)
    document_archived_at = models.CharField('Document Archived At', max_length=200)

    def __str__(self):
        return self.full_name


class budget(models.Model):
    Year = models.IntegerField()
    department_name = models.ForeignKey(department, on_delete=models.CASCADE)
    total_amount_for_this_whole_year = models.FloatField('Total Budget For The Year In GHC', max_length=200)
    total_amount_per_january = models.FloatField('Total Budget For January This Year In GHC', max_length=200)
    january_procuments = models.TextField('Stuffs to Buy For January', max_length=2000)
    january_salaries_for_staff = models.FloatField('Total Staff Salaries for January', max_length=200)
    total_cost_for_amenities_used_in_january = models.FloatField('Total Cost For Amenities Used in for January',
                                                                 max_length=200)
    january_advertisement_plans = models.TextField('January Advertisement Plans ', max_length=2000)
    january_advertisement_plans_attained = models.TextField('January Advertisement Plans Attained ', max_length=2000)
    total_cost_of_january_advertisement_plans = models.FloatField('Total Cost of January Advertisement Plans',
                                                                  max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In January', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_january = models.CharField('Name of First Amenity Used In January', null=True, blank=True,
                                                         max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_january = models.CharField('Name of Second Amenity Used In January', null=True, blank=True,
                                                 max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_january = models.CharField('Name of Third Amenity Used In January', null=True, blank=True,
                                                     max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_january_amenities = models.CharField('Name of Fourth Amenity Used In January', null=True,
                                                                blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_january_amenities = models.CharField('Name of Fifth Amenity Used In January', null=True, blank=True,
                                                       max_length=200)

    sixth_used_in_january_amenities = models.CharField('Name of Sixth Amenity Used In January', null=True, blank=True,
                                                       max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_january_amenities = models.CharField('Name of Seventh Amenity Used In January', null=True,
                                                         blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_january_amenities = models.CharField('Name of Eighth Amenity Used In January', null=True,
                                                           blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_january_amenities = models.CharField('Name of Ninth Amenity Used In January', null=True, blank=True,
                                                        max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_january_amenities = models.CharField('Name of Tenth Amenity Used In January', null=True, blank=True,
                                                       max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In January', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_february = models.FloatField('Total Budget For February This Year In GHC', max_length=200)
    february_procuments = models.TextField('Stuffs to Buy For February', max_length=2000)
    february_salaries_for_staff = models.FloatField('Total Staff Salaries for February', max_length=200)
    total_cost_for_amenities_used_in_february = models.FloatField('Total Cost For Amenities Used in for February',
                                                                  max_length=200)
    february_advertisement_plans = models.TextField('February Advertisement Plans ', max_length=2000)
    february_advertisement_plans_attained = models.TextField('January Advertisement Plans Attained ', max_length=2000)
    total_cost_of_february_advertisement_plans = models.FloatField('Total Cost of January Advertisement Plans',
                                                                   max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In February', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_february = models.CharField('Name of First Amenity Used In February', null=True,
                                                          blank=True,
                                                          max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_february = models.CharField('Name of Second Amenity Used In January', null=True, blank=True,
                                                  max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_february = models.CharField('Name of Third Amenity Used In February', null=True, blank=True,
                                                      max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_february_amenities = models.CharField('Name of Fourth Amenity Used In February', null=True,
                                                                 blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_february_amenities = models.CharField('Name of Fifth Amenity Used In February', null=True, blank=True,
                                                        max_length=200)

    sixth_used_in_february_amenities = models.CharField('Name of Sixth Amenity Used In February', null=True, blank=True,
                                                        max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_february_amenities = models.CharField('Name of Seventh Amenity Used In February', null=True,
                                                          blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_february_amenities = models.CharField('Name of Eighth Amenity Used In February', null=True,
                                                            blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_february_amenities = models.CharField('Name of Ninth Amenity Used In February', null=True,
                                                         blank=True,
                                                         max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_february_amenities = models.CharField('Name of Tenth Amenity Used In February', null=True, blank=True,
                                                        max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In February', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_march = models.FloatField('Total Budget For March This Year In GHC', max_length=200)
    march_procuments = models.TextField('Stuffs to Buy For March', max_length=2000)
    march_salaries_for_staff = models.FloatField('Total Staff Salaries for March', max_length=200)
    total_cost_for_amenities_used_in_march = models.FloatField('Total Cost For Amenities Used in for March',
                                                               max_length=200)
    march_advertisement_plans = models.TextField('March Advertisement Plans ', max_length=2000)
    march_advertisement_plans_attained = models.TextField('March Advertisement Plans Attained ', max_length=2000)
    total_cost_of_march_advertisement_plans = models.FloatField('Total Cost of March Advertisement Plans',
                                                                max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In March', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_march = models.CharField('Name of First Amenity Used In March', null=True,
                                                       blank=True,
                                                       max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_march = models.CharField('Name of Second Amenity Used In March', null=True, blank=True,
                                               max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_march = models.CharField('Name of Third Amenity Used In March', null=True, blank=True,
                                                   max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_march_amenities = models.CharField('Name of Fourth Amenity Used In March', null=True,
                                                              blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_march_amenities = models.CharField('Name of Fifth Amenity Used In March', null=True, blank=True,
                                                     max_length=200)

    sixth_used_in_march_amenities = models.CharField('Name of Sixth Amenity Used In March', null=True, blank=True,
                                                     max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_march_amenities = models.CharField('Name of Seventh Amenity Used In March', null=True,
                                                       blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_march_amenities = models.CharField('Name of Eighth Amenity Used In March', null=True,
                                                         blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_march_amenities = models.CharField('Name of Ninth Amenity Used In March', null=True,
                                                      blank=True,
                                                      max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_march_amenities = models.CharField('Name of Tenth Amenity Used In March', null=True, blank=True,
                                                     max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In March', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_april = models.FloatField('Total Budget For April This Year In GHC', max_length=200)
    april_procuments = models.TextField('Stuffs to Buy For April', max_length=2000)
    april_salaries_for_staff = models.FloatField('Total Staff Salaries for April', max_length=200)
    total_cost_for_amenities_used_in_april = models.FloatField('Total Cost For Amenities Used in for April',
                                                               max_length=200)
    april_advertisement_plans = models.TextField('April Advertisement Plans ', max_length=2000)
    april_advertisement_plans_attained = models.TextField('April Advertisement Plans Attained ', max_length=2000)
    total_cost_of_april_advertisement_plans = models.FloatField('Total Cost of April Advertisement Plans',
                                                                max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In April', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_april = models.CharField('Name of First Amenity Used In April', null=True,
                                                       blank=True,
                                                       max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_april = models.CharField('Name of Second Amenity Used In April', null=True, blank=True,
                                               max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_april = models.CharField('Name of Third Amenity Used In April', null=True, blank=True,
                                                   max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_april_amenities = models.CharField('Name of Fourth Amenity Used In April', null=True,
                                                              blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_april_amenities = models.CharField('Name of Fifth Amenity Used In April', null=True, blank=True,
                                                     max_length=200)

    sixth_used_in_april_amenities = models.CharField('Name of Sixth Amenity Used In April', null=True, blank=True,
                                                     max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_april_amenities = models.CharField('Name of Seventh Amenity Used In April', null=True,
                                                       blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_april_amenities = models.CharField('Name of Eighth Amenity Used In April', null=True,
                                                         blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_april_amenities = models.CharField('Name of Ninth Amenity Used In April', null=True,
                                                      blank=True,
                                                      max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_april_amenities = models.CharField('Name of Tenth Amenity Used In April', null=True, blank=True,
                                                     max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In April', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_may = models.FloatField('Total Budget For May This Year In GHC', max_length=200)
    may_procuments = models.TextField('Stuffs to Buy For May', max_length=2000)
    may_salaries_for_staff = models.FloatField('Total Staff Salaries for May', max_length=200)
    total_cost_for_amenities_used_in_may = models.FloatField('Total Cost For Amenities Used in for May',
                                                             max_length=200)
    may_advertisement_plans = models.TextField('May Advertisement Plans ', max_length=2000)
    may_advertisement_plans_attained = models.TextField('May Advertisement Plans Attained ', max_length=2000)
    total_cost_of_may_advertisement_plans = models.FloatField('Total Cost of May Advertisement Plans',
                                                              max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In May', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_may = models.CharField('Name of First Amenity Used In May', null=True,
                                                     blank=True,
                                                     max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_may = models.CharField('Name of Second Amenity Used In May', null=True, blank=True,
                                             max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_may = models.CharField('Name of Third Amenity Used In May', null=True, blank=True,
                                                 max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_may_amenities = models.CharField('Name of Fourth Amenity Used In May', null=True,
                                                            blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_may_amenities = models.CharField('Name of Fifth Amenity Used In May', null=True, blank=True,
                                                   max_length=200)

    sixth_used_in_may_amenities = models.CharField('Name of Sixth Amenity Used In May', null=True, blank=True,
                                                   max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_may_amenities = models.CharField('Name of Seventh Amenity Used In May', null=True,
                                                     blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_may_amenities = models.CharField('Name of Eighth Amenity Used In May', null=True,
                                                       blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_may_amenities = models.CharField('Name of Ninth Amenity Used In May', null=True,
                                                    blank=True,
                                                    max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_may_amenities = models.CharField('Name of Tenth Amenity Used In May', null=True, blank=True,
                                                   max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In May', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_june = models.FloatField('Total Budget For June This Year In GHC', max_length=200)
    june_procuments = models.TextField('Stuffs to Buy For June', max_length=2000)
    june_salaries_for_staff = models.FloatField('Total Staff Salaries for June', max_length=200)
    total_cost_for_amenities_used_in_june = models.FloatField('Total Cost For Amenities Used in for June',
                                                              max_length=200)
    june_advertisement_plans = models.TextField('June Advertisement Plans ', max_length=2000)
    june_advertisement_plans_attained = models.TextField('June Advertisement Plans Attained ', max_length=2000)
    total_cost_of_june_advertisement_plans = models.FloatField('Total Cost of June Advertisement Plans',
                                                               max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In June', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_june = models.CharField('Name of First Amenity Used In June', null=True,
                                                      blank=True,
                                                      max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_june = models.CharField('Name of Second Amenity Used In June', null=True, blank=True,
                                              max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_june = models.CharField('Name of Third Amenity Used In June', null=True, blank=True,
                                                  max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_june_amenities = models.CharField('Name of Fourth Amenity Used In June', null=True,
                                                             blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_june_amenities = models.CharField('Name of Fifth Amenity Used In June', null=True, blank=True,
                                                    max_length=200)

    sixth_used_in_june_amenities = models.CharField('Name of Sixth Amenity Used In June', null=True, blank=True,
                                                    max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_june_amenities = models.CharField('Name of Seventh Amenity Used In June', null=True,
                                                      blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_june_amenities = models.CharField('Name of Eighth Amenity Used In June', null=True,
                                                        blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_june_amenities = models.CharField('Name of Ninth Amenity Used In June', null=True,
                                                     blank=True,
                                                     max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_june_amenities = models.CharField('Name of Tenth Amenity Used In June', null=True, blank=True,
                                                    max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In June', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_july = models.FloatField('Total Budget For July This Year In GHC', max_length=200)
    july_procuments = models.TextField('Stuffs to Buy For July', max_length=2000)
    july_salaries_for_staff = models.FloatField('Total Staff Salaries for July', max_length=200)
    total_cost_for_amenities_used_in_july = models.FloatField('Total Cost For Amenities Used in for July',
                                                              max_length=200)
    july_advertisement_plans = models.TextField('July Advertisement Plans ', max_length=2000)
    july_advertisement_plans_attained = models.TextField('July Advertisement Plans Attained ', max_length=2000)
    total_cost_of_july_advertisement_plans = models.FloatField('Total Cost of July Advertisement Plans',
                                                               max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In July', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_july = models.CharField('Name of First Amenity Used In July', null=True,
                                                      blank=True,
                                                      max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_july = models.CharField('Name of Second Amenity Used In July', null=True, blank=True,
                                              max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_july = models.CharField('Name of Third Amenity Used In July', null=True, blank=True,
                                                  max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_july_amenities = models.CharField('Name of Fourth Amenity Used In July', null=True,
                                                             blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_july_amenities = models.CharField('Name of Fifth Amenity Used In July', null=True, blank=True,
                                                    max_length=200)

    sixth_used_in_july_amenities = models.CharField('Name of Sixth Amenity Used In July', null=True, blank=True,
                                                    max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_july_amenities = models.CharField('Name of Seventh Amenity Used In July', null=True,
                                                      blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_july_amenities = models.CharField('Name of Eighth Amenity Used In July', null=True,
                                                        blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_july_amenities = models.CharField('Name of Ninth Amenity Used In July', null=True,
                                                     blank=True,
                                                     max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_july_amenities = models.CharField('Name of Tenth Amenity Used In July', null=True, blank=True,
                                                    max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In July', null=True, blank=True,
                                  max_length=2000)


    total_amount_per_august = models.FloatField('Total Budget For August This Year In GHC', max_length=200)
    august_procuments = models.TextField('Stuffs to Buy For August', max_length=2000)
    august_salaries_for_staff = models.FloatField('Total Staff Salaries for August', max_length=200)
    total_cost_for_amenities_used_in_august = models.FloatField('Total Cost For Amenities Used in for August',
                                                              max_length=200)
    august_advertisement_plans = models.TextField('August Advertisement Plans ', max_length=2000)
    august_advertisement_plans_attained = models.TextField('August Advertisement Plans Attained ', max_length=2000)
    total_cost_of_august_advertisement_plans = models.FloatField('Total Cost of August Advertisement Plans',
                                                               max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In July', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_august = models.CharField('Name of First Amenity Used In August', null=True,
                                                      blank=True,
                                                      max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_august = models.CharField('Name of Second Amenity Used In August', null=True, blank=True,
                                              max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_august = models.CharField('Name of Third Amenity Used In August', null=True, blank=True,
                                                  max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_august_amenities = models.CharField('Name of Fourth Amenity Used In August', null=True,
                                                             blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_august_amenities = models.CharField('Name of Fifth Amenity Used In August', null=True, blank=True,
                                                    max_length=200)

    sixth_used_in_august_amenities = models.CharField('Name of Sixth Amenity Used In August', null=True, blank=True,
                                                    max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_august_amenities = models.CharField('Name of Seventh Amenity Used In August', null=True,
                                                      blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_august_amenities = models.CharField('Name of Eighth Amenity Used In August', null=True,
                                                        blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_august_amenities = models.CharField('Name of Ninth Amenity Used In August', null=True,
                                                     blank=True,
                                                     max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_august_amenities = models.CharField('Name of Tenth Amenity Used In August', null=True, blank=True,
                                                    max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In August', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_september = models.FloatField('Total Budget For September This Year In GHC', max_length=200)
    september_procuments = models.TextField('Stuffs to Buy For September', max_length=2000)
    september_salaries_for_staff = models.FloatField('Total Staff Salaries for September', max_length=200)
    total_cost_for_amenities_used_in_september = models.FloatField('Total Cost For Amenities Used in for September',
                                                                max_length=200)
    september_advertisement_plans = models.TextField('September Advertisement Plans ', max_length=2000)
    september_advertisement_plans_attained = models.TextField('September Advertisement Plans Attained ', max_length=2000)
    total_cost_of_september_advertisement_plans = models.FloatField('Total Cost of September Advertisement Plans',
                                                                 max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In September', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_september = models.CharField('Name of First Amenity Used In September', null=True,
                                                        blank=True,
                                                        max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_september = models.CharField('Name of Second Amenity Used In September', null=True, blank=True,
                                                max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_september = models.CharField('Name of Third Amenity Used In September', null=True, blank=True,
                                                    max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_september_amenities = models.CharField('Name of Fourth Amenity Used In September', null=True,
                                                               blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_september_amenities = models.CharField('Name of Fifth Amenity Used In September', null=True, blank=True,
                                                      max_length=200)

    sixth_used_in_september_amenities = models.CharField('Name of Sixth Amenity Used In September', null=True, blank=True,
                                                      max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_september_amenities = models.CharField('Name of Seventh Amenity Used In September', null=True,
                                                        blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_september_amenities = models.CharField('Name of Eighth Amenity Used In September', null=True,
                                                          blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_september_amenities = models.CharField('Name of Ninth Amenity Used In September', null=True,
                                                       blank=True,
                                                       max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_september_amenities = models.CharField('Name of Tenth Amenity Used In September', null=True, blank=True,
                                                      max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In September', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_october = models.FloatField('Total Budget For October This Year In GHC', max_length=200)
    october_procuments = models.TextField('Stuffs to Buy For October', max_length=2000)
    october_salaries_for_staff = models.FloatField('Total Staff Salaries for October', max_length=200)
    total_cost_for_amenities_used_in_october = models.FloatField('Total Cost For Amenities Used in for October',
                                                                   max_length=200)
    october_advertisement_plans = models.TextField('October Advertisement Plans ', max_length=2000)
    october_advertisement_plans_attained = models.TextField('October Advertisement Plans Attained ',
                                                              max_length=2000)
    total_cost_of_october_advertisement_plans = models.FloatField('Total Cost of October Advertisement Plans',
                                                                    max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In October', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_october = models.CharField('Name of First Amenity Used In October', null=True,
                                                           blank=True,
                                                           max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_october = models.CharField('Name of Second Amenity Used In October', null=True, blank=True,
                                                   max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_october = models.CharField('Name of Third Amenity Used In October', null=True, blank=True,
                                                       max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_october_amenities = models.CharField('Name of Fourth Amenity Used In October', null=True,
                                                                  blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_october_amenities = models.CharField('Name of Fifth Amenity Used In October', null=True,
                                                         blank=True,
                                                         max_length=200)

    sixth_used_in_october_amenities = models.CharField('Name of Sixth Amenity Used In October', null=True,
                                                         blank=True,
                                                         max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_october_amenities = models.CharField('Name of Seventh Amenity Used In October', null=True,
                                                           blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_october_amenities = models.CharField('Name of Eighth Amenity Used In October', null=True,
                                                             blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_october_amenities = models.CharField('Name of Ninth Amenity Used In October', null=True,
                                                          blank=True,
                                                          max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_october_amenities = models.CharField('Name of Tenth Amenity Used In October', null=True,
                                                         blank=True,
                                                         max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In October', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_november = models.FloatField('Total Budget For November This Year In GHC', max_length=200)
    november_procuments = models.TextField('Stuffs to Buy For November', max_length=2000)
    november_salaries_for_staff = models.FloatField('Total Staff Salaries for November', max_length=200)
    total_cost_for_amenities_used_in_november = models.FloatField('Total Cost For Amenities Used in for November',
                                                                 max_length=200)
    november_advertisement_plans = models.TextField('November Advertisement Plans ', max_length=2000)
    november_advertisement_plans_attained = models.TextField('November Advertisement Plans Attained ',
                                                            max_length=2000)
    total_cost_of_november_advertisement_plans = models.FloatField('Total Cost of November Advertisement Plans',
                                                                  max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In November', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_november = models.CharField('Name of First Amenity Used In November', null=True,
                                                         blank=True,
                                                         max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_november = models.CharField('Name of Second Amenity Used In November', null=True, blank=True,
                                                 max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_november = models.CharField('Name of Third Amenity Used In November', null=True, blank=True,
                                                     max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_november_amenities = models.CharField('Name of Fourth Amenity Used In November', null=True,
                                                                blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_november_amenities = models.CharField('Name of Fifth Amenity Used In November', null=True,
                                                       blank=True,
                                                       max_length=200)

    sixth_used_in_november_amenities = models.CharField('Name of Sixth Amenity Used In November', null=True,
                                                       blank=True,
                                                       max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_november_amenities = models.CharField('Name of Seventh Amenity Used In November', null=True,
                                                         blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_november_amenities = models.CharField('Name of Eighth Amenity Used In November', null=True,
                                                           blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_november_amenities = models.CharField('Name of Ninth Amenity Used In November', null=True,
                                                        blank=True,
                                                        max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_november_amenities = models.CharField('Name of Tenth Amenity Used In November', null=True,
                                                       blank=True,
                                                       max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In November', null=True, blank=True,
                                  max_length=2000)

    total_amount_per_december = models.FloatField('Total Budget For December This Year In GHC', max_length=200)
    december_procuments = models.TextField('Stuffs to Buy For December', max_length=2000)
    december_salaries_for_staff = models.FloatField('Total Staff Salaries for December', max_length=200)
    total_cost_for_amenities_used_in_december = models.FloatField('Total Cost For Amenities Used in for December',
                                                                  max_length=200)
    december_advertisement_plans = models.TextField('December Advertisement Plans ', max_length=2000)
    december_advertisement_plans_attained = models.TextField('December Advertisement Plans Attained ',
                                                             max_length=2000)
    total_cost_of_december_advertisement_plans = models.FloatField('Total Cost of December Advertisement Plans',
                                                                   max_length=2000)
    other_cost = models.TextField('Any Other Costs Incurred In December', null=True, blank=True, max_length=2000)

    the_first_amenity_used_in_december = models.CharField('Name of First Amenity Used In December', null=True,
                                                          blank=True,
                                                          max_length=200)
    total_cost1 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    second_amenity_in_december = models.CharField('Name of Second Amenity Used In December', null=True, blank=True,
                                                  max_length=200)
    total_cost2 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    third_amenity_used_in_december = models.CharField('Name of Third Amenity Used In December', null=True, blank=True,
                                                      max_length=200)
    total_cost3 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fourth_amenity_used_in_december_amenities = models.CharField('Name of Fourth Amenity Used InDecember', null=True,
                                                                 blank=True, max_length=200)
    total_cost4 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    fifth_used_in_december_amenities = models.CharField('Name of Fifth Amenity Used In December', null=True,
                                                        blank=True,
                                                        max_length=200)

    sixth_used_in_december_amenities = models.CharField('Name of Sixth Amenity Used In December', null=True,
                                                        blank=True,
                                                        max_length=200)
    total_cost6 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    seventh_used_in_december_amenities = models.CharField('Name of Seventh Amenity Used In December', null=True,
                                                          blank=True, max_length=200)
    total_cost7 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    the_eigth_used_in_december_amenities = models.CharField('Name of Eighth Amenity Used In December', null=True,
                                                            blank=True, max_length=200)
    total_cost8 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    nineth_used_in_december_amenities = models.CharField('Name of Ninth Amenity Used In December', null=True,
                                                         blank=True,
                                                         max_length=200)
    total_cost9 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    tenth_used_in_december_amenities = models.CharField('Name of Tenth Amenity Used In December', null=True,
                                                        blank=True,
                                                        max_length=200)
    total_cost10 = models.FloatField('Total Cost', null=True, blank=True, max_length=200)
    other_cost = models.TextField('Any Other Amenities And Their Cost Incurred In December', null=True, blank=True,
                                  max_length=2000)

    total_staff_salaries = models.FloatField('Total Salaries For The Year In GHC', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.total_amount_per_january


class daily_report(models.Model):
    date = models.DateTimeField()
    department_name = models.ForeignKey(department, on_delete=models.CASCADE)
    staff_name = models.ForeignKey(staff, on_delete=models.CASCADE)
    what_you_did = models.TextField('What you did for today', max_length=2000)
    total = models.IntegerField()
    total_cost_if_any = models.FloatField('Total Cost if Any', null=True, blank=True, max_length=200)
    money_gained = models.FloatField('Money Gained If Any', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.staff_name

    @staticmethod
    def autocomplete_search_fields():
        return 'date',
        'department_name',

    'staff_name',
    'what_you_did',
    'total',
    'total_cost_if_any',
    'money_gained'


class procument(models.Model):
    product_brought = models.CharField('Product Brought', max_length=200)
    cost = models.FloatField('Total Cost', max_length=200)
    price_per_unit = models.FloatField('Price Per Unit', max_length=200)
    store_bought = models.CharField('Store', max_length=200)
    personnel_in_charge_of_purchase = models.ForeignKey(staff, on_delete=models.CASCADE)
    accountant_in_charge_of_purchase = models.CharField('Accountant In Charge Of The Purchase', max_length=200)
    quantity = models.IntegerField()
    day_bought = models.DateTimeField()
    location_stored_at = models.CharField('Location Stored at', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.product_brought


class enquiry(models.Model):
    fullname = models.CharField('Customer Full Name', max_length=200)
    phonenumber = models.CharField('Phone Number', blank=True, null=True, max_length=200)
    emailaddress = models.EmailField('Email', blank=True, null=True, max_length=200)
    option = models.CharField('Option Choosen', blank=True, null=True, max_length=200)
    message = models.TextField('message', max_length=200)
    date_added = models.DateTimeField()
    read = models.BooleanField("Read", blank=True, null=True)

    def __str__(self):
        return self.fullname


class company_category(models.Model):
    company_category = models.CharField('Comapany Category', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.company_category


class company_name(models.Model):
    category = models.ForeignKey(company_category, on_delete=models.CASCADE)
    company_name = models.CharField('Name Of The Company', max_length=200)

    address = models.CharField('Location', max_length=200)
    contact = models.CharField('Contact', max_length=100)
    email = models.EmailField('Email', blank=True, null=True, max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.company_name


class job(models.Model):
    Id = models.IntegerField(primary_key=True, auto_created=True)
    company_name = models.ForeignKey(company_name, on_delete=models.CASCADE)
    location = models.CharField('Location', max_length=200)
    company_image = models.ImageField(blank=True, null=True, upload_to=f"static\Company_Images")
    company_category = models.ForeignKey(company_category, on_delete=models.CASCADE)
    min_salary = models.FloatField()
    max_salary = models.FloatField()

    job_offer1 = models.CharField('Job Opening 1', max_length=200)
    job_offer2 = models.CharField('Job Opening 2', blank=True, null=True, max_length=200)
    job_offer3 = models.CharField('Job Opening 3', blank=True, null=True, max_length=200)
    job_offer4 = models.CharField('Job Opening 4', blank=True, null=True, max_length=200)
    job_offer5 = models.CharField('Job Opening 5', blank=True, null=True, max_length=200)
    job_offer6 = models.CharField('Job Opening 6', blank=True, null=True, max_length=200)
    job_offer7 = models.CharField('Job Opening 7', blank=True, null=True, max_length=200)
    job_offer8 = models.CharField('Job Opening 8', blank=True, null=True, max_length=200)
    job_offer9 = models.CharField('Job Opening 9', blank=True, null=True, max_length=200)
    job_offer10 = models.CharField('Job Opening 10', blank=True, null=True, max_length=200)

    job_offer11 = models.CharField('Job Opening 11', blank=True, null=True, max_length=200)
    job_offer12 = models.CharField('Job Opening 12', blank=True, null=True, max_length=200)
    job_offer13 = models.CharField('Job Opening 13', blank=True, null=True, max_length=200)
    job_offer14 = models.CharField('Job Opening 14', blank=True, null=True, max_length=200)
    job_offer15 = models.CharField('Job Opening 15', blank=True, null=True, max_length=200)
    job_offer16 = models.CharField('Job Opening 16', blank=True, null=True, max_length=200)
    job_offer17 = models.CharField('Job Opening 17', blank=True, null=True, max_length=200)
    job_offer18 = models.CharField('Job Opening 18', blank=True, null=True, max_length=200)
    job_offer19 = models.CharField('Job Opening 19', blank=True, null=True, max_length=200)
    job_offer20 = models.CharField('Job Opening 20', blank=True, null=True, max_length=200)

    date_added = models.DateTimeField()

    deadline = models.DateTimeField()

    def __str__(self):
        return self.job_offer1



class terms_condition(models.Model):
    serv_name = models.CharField('Service Name', max_length=200)
    serv_policy = models.TextField('Policy', max_length=9000)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.serv_name


class package(models.Model):
    plan_name = models.CharField('Plan Name', max_length=200)
    individual_limit = models.IntegerField()
    price = models.FloatField('Price', max_length=200)
    days_to_get_job = models.CharField('Days To Get The Job', max_length=200)
    plan_description1 = models.CharField('Plan Description 1', blank=True, null=True, max_length=30)
    plan_description2 = models.CharField('Plan Description 2', blank=True, null=True, max_length=30)
    plan_description3 = models.CharField('Plan Description 3', blank=True, null=True, max_length=30)
    plan_description4 = models.CharField('Plan Description 4', blank=True, null=True, max_length=30)
    plan_description5 = models.CharField('Plan Description 5', blank=True, null=True, max_length=30)
    plan_description6 = models.CharField('Plan Description 6', blank=True, null=True, max_length=30)
    plan_description7 = models.CharField('Plan Description 7', blank=True, null=True, max_length=30)
    plan_description8 = models.CharField('Plan Description 8', blank=True, null=True, max_length=30)
    plan_description9 = models.CharField('Plan Description 9', blank=True, null=True, max_length=30)
    plan_description10 = models.CharField('Plan Description 10', blank=True, null=True, max_length=30)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.plan_name


class our(models.Model):
    name = models.CharField('Name', max_length=200)
    happy_clents = models.IntegerField()
    partners = models.IntegerField()
    awards_won = models.IntegerField()
    phonenumber2 = models.CharField('Second Number', max_length=200)
    phonenumber = models.CharField('Phone Number', max_length=200)
    travels_customer_document = models.CharField('The documents a travels customer should submit', max_length=200)
    other_customer_documents_submit = models.CharField('The documents a job customer should submit', max_length=200)

    facebookaddress = models.URLField('Facebook Link', null=True, blank='True', max_length=250)
    instagramaddress = models.URLField('Instagram link', null=True, blank='True', max_length=250)
    about_image = models.ImageField('About Image', upload_to=f"static\image_about")
    chooseus_image = models.ImageField('Choose Us Image', upload_to=f"static\choose_image")
    location = models.CharField('Location', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.name


class team(models.Model):
    fullname = models.CharField('Full Name', max_length=200)
    designation = models.CharField('Designation', max_length=200)

    picture = models.ImageField(upload_to=f"static\Team")
    date_added = models.DateTimeField()

    def __str__(self):
        return self.fullname


class carosel_image(models.Model):
    name = models.CharField('name', max_length=200)
    small_message = models.CharField('Titled message', max_length=200)
    jumbotron = models.CharField('Jumbotron', max_length=200)
    img = models.ImageField(upload_to=f"static\caroselle")

    date_added = models.DateTimeField()

    def __str__(self):
        return self.name


class maincarodis(models.Model):
    name = models.CharField('name', max_length=200)
    small_message = models.CharField('Titled message', max_length=200)
    jumbotron = models.CharField('Jumbotron', max_length=200)
    img = models.ImageField(upload_to=f"static\maincaroselle")

    date_added = models.DateTimeField()

    def __str__(self):
        return self.name


class customer_employemnt_stage(models.Model):
    employemnt_stage = models.CharField('Employemnt Stage', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.employemnt_stage


class customer_employemnt_document(models.Model):
    employemnt_document = models.CharField('Employemnt Documents', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.employemnt_document


class customer(models.Model):
    customer_name = models.CharField('Customer Name', max_length=200)
    customer_img = models.FileField('Customer Passport Picture',upload_to=f"static\customers")
    Date_of_Birth = models.DateField()
    address = models.CharField('Address', max_length=200)
    occupation = models.CharField('Occupation', max_length=200)
    phone_number = models.CharField('Phone Number', max_length=200)
    customer_email = models.EmailField('Email', blank=True, null=True, max_length=200)
    package_choosen = models.ForeignKey(package, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    Doc1 = models.ForeignKey(customer_employemnt_document, on_delete=models.CASCADE)
    upload1 = models.FileField(blank=True, null=True, upload_to=f"static\customers\documents")
    acadamic_level = models.CharField('Acadamic level', max_length=200)
    acadamic_certificate = models.FileField(blank=True, null=True, upload_to=f"static\customers\documents")
    employemnet_form = models.FileField('Secure Express Employment Form',upload_to=f"static\customers\documents")
    other_document = models.FileField(blank=True, null=True, upload_to=f"static\customers\documents")
    other_document2 = models.FileField(blank=True, null=True, upload_to=f"static\customers\documents")
    formal_employee = models.CharField('Formal Employee', blank=True, null=True, max_length=200)
    current_employement_stage = models.ForeignKey(customer_employemnt_stage, on_delete=models.CASCADE)
    company_which_employed_customer = models.ForeignKey(company_name, on_delete=models.CASCADE)
    customer_salary = models.FloatField('Customer salary by employee', blank=True, null=True, max_length=200)
    amount_to_deduct_from_salary =  models.FloatField('Amount to take from customers salary', blank=True, null=True, max_length=200)
    period_to_deduct =  models.CharField('Period to deduct', max_length=200)
    starting_date_to_deduct = models.DateTimeField(blank=True, null=True)
    next_date_to_deduct = models.DateTimeField (blank=True, null=True)
    current_number_of_month_deducted = models.IntegerField(blank=True, null=True)

    guarantor_name = models.CharField('Name of Guarantor', blank=True, null=True, max_length=200)
    guarantor_address = models.CharField('Address of Guarantor', blank=True, null=True, max_length=200)
    guarantor_contacts = models.CharField('Phone Number of Guarantor', blank=True, null=True, max_length=200)
    guarantor_img = models.ImageField(blank=True, null=True, upload_to=f"static\customers\guarantor")
    guarantor_form_img = models.FileField(blank=True, null=True, upload_to=f"static\customers\guarantor")
    next_of_kin = models.CharField('Next Of Kin', max_length=200)
    activation_code = models.CharField('Activation Code',blank=True, null=True, unique=True, max_length=50)
    Archive = models.CharField('Documents Archive in', max_length=200)

    workstatus = models.BooleanField("IS this Person Placed in Company", blank=True, null=True)

    date_added = models.DateTimeField()

    def __str__(self):
        return self.customer_name


class online_order(models.Model):
    job_ID = models.CharField('Job_ID', max_length=200)
    company_name =  models.CharField('Name of The Company', max_length=200)
    company_category =  models.CharField('Company Category', max_length=200)
    fullname = models.CharField('Full Name of Customer', max_length=200)
    email = models.EmailField('Email of Customer', blank=True, null=True, max_length=200)
    phonenumber = models.CharField('Phone Number Of Customer', max_length=200)
    pack_choosen = models.CharField('Package Choosen', max_length=70)
    cv = models.ImageField(blank=True, null=True, upload_to=f"static\customers\cv")
    jobexpect = models.CharField('jobexpect', max_length=200)
    salaryexpect = models.FloatField()
    date_added = models.DateTimeField()
    read = models.BooleanField("Read", blank=True, null=True)
    accepted = models.BooleanField("Accepted", blank=True, null=True)
    activation_code = models.CharField('Activation Code',unique=True, max_length=50)
    starting_date = models.DateTimeField( blank=True, null=True)

    def __str__(self):
        return self.fullname


class company_records_type(models.Model):
    documentname = models.CharField('Name of the Document', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.documentname


class company_record(models.Model):
    document_name = models.CharField('Name of the Document', max_length=200)
    document_type = models.ForeignKey(company_records_type, on_delete=models.CASCADE)
    for_what_department = models.ForeignKey(department, on_delete=models.CASCADE)

    Doc_1 = models.FileField(upload_to=f"static\Company\Records")
    document1 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat = models.CharField('Archive at', null=True, blank="True", max_length=200)

    Doc_2 = models.FileField(upload_to=f"static\Company\Records")
    document2 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat2 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_3 = models.FileField(upload_to=f"static\Company\Records")
    document3 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat3 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_4 = models.FileField(upload_to=f"static\Company\Records")
    document4 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat4 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_5 = models.FileField(upload_to=f"static\Company\Records")
    document5 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat5 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_6 = models.FileField(upload_to=f"static\Company\Records")
    document6 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat7 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_7 = models.FileField(upload_to=f"static\Company\Records")
    document7 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat7 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_8 = models.FileField(upload_to=f"static\Company\Records")
    document8 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat8 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_9 = models.FileField(upload_to=f"static\Company\Records")
    document9 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat9 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_10 = models.FileField(upload_to=f"static\Company\Records")
    document10 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat10 = models.CharField('Archive at', null=True, blank="True", max_length=200)

    Doc_11 = models.FileField(upload_to=f"static\Company\Records")
    document11 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat11 = models.CharField('Archive at', null=True, blank="True", max_length=200)

    Doc_12 = models.FileField(upload_to=f"static\Company\Records")
    document12 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat12 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_13 = models.FileField(upload_to=f"static\Company\Records")
    document13 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat13 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_14 = models.FileField(upload_to=f"static\Company\Records")
    document14 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat14 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_15 = models.FileField(upload_to=f"static\Company\Records")
    document15 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat15 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    Doc_16 = models.FileField(upload_to=f"static\Company\Records")

    document16 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat16 = models.CharField('Archive at', null=True, blank="True", max_length=200)

    Doc_17 = models.FileField(upload_to=f"static\Company\Records")
    document17 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat17 = models.CharField('Archive at', null=True, blank="True", max_length=200)

    Doc_18 = models.FileField(upload_to=f"static\Company\Records")
    document18 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat18 = models.CharField('Archive at', null=True, blank="True", max_length=200)

    Doc_19 = models.FileField(upload_to=f"static\Company\Records")
    document19 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat19 = models.CharField('Archive at', null=True, blank="True", max_length=200)

    Doc_20 = models.FileField(upload_to=f"static\Company\Records")
    document20 = models.TextField('What is it for', null=True, blank="True", max_length=200)
    archivedat20 = models.CharField('Archive at', null=True, blank="True", max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.document_name


class customer_own_job_request(models.Model):
    fullname = models.CharField('Full Name of Customer', max_length=200)
    email = models.EmailField('Email of Customer', blank=True, null=True, max_length=200)
    phonenumber = models.CharField('Phone Number Of Customer', max_length=200)
    pack_choosen = models.CharField('Package Chosen', max_length=70)
    cv = models.ImageField(blank=True, null=True, upload_to=f"static\customer_own_job\cv")
    jobexpect = models.CharField('The Job the customer wants ', max_length=200)
    salaryexpect = models.FloatField()
    date_added = models.DateTimeField()
    read = models.BooleanField("Read", blank=True, null=True)
    accepted = models.BooleanField("Accepted", blank=True, null=True)
    company_that_the_customer_will_be_placed_in = models.ForeignKey(company_name, on_delete=models.CASCADE, blank=True,
                                                                    null=True)
    location_of_company = models.CharField('Location of the company', max_length=50, blank=True, null=True)
    actual_salary = models.CharField('Actual Salary given to customer', blank=True, null=True, max_length=200)
    activation_code = models.CharField('Activation Code', unique=True ,blank=True, null=True, max_length=50)
    starting_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class service(models.Model):
    services_name = models.CharField('Enter Service Name', max_length=50)
    img = models.ImageField(upload_to=f'static\Our_Company\Services')
    about_service = models.TextField('About Service ', max_length=300)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.services_name
