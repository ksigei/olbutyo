from django.contrib import admin
from curriculum.models import Standard, Subject, Lesson, Comment, Reply, WorkingDays, TimeSlots, SlotSubject
# Register your models here.


admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(WorkingDays)
admin.site.register(TimeSlots)
admin.site.register(SlotSubject)
