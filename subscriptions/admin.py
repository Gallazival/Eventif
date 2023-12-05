from django.contrib import admin
from django.utils.timezone import now
from subscriptions.models import Subscription
<<<<<<< HEAD


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',
                    'cpf', 'created_at', 'subscribed_today', 'paid']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone', 'cpf', 'created_at']
    list_filter = ['paid', 'created_at']

    actions = ['mark_as_paid',]

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

=======

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'cpf', 'created_at', 'subscribed_today', 'paid']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone', 'cpf', 'created_at']
    list_filter = ['paid','created_at',]

    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        return obj.created_at == now().date()
    
    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = "{} inscrição foi marcada como paga"
        else:
            msg = "{} inscrições foram marcadas como pagas"

        self.message_user

    mark_as_paid.short_description = 'Marcar como pago'
 
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = "{} inscrição foi marcada como paga"
        else:
            msg = "{} inscrições foram marcadas como pagas"

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar como pago'


admin.site.register(Subscription, SubscriptionModelAdmin)
