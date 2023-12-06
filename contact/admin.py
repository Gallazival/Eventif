from django.contrib import admin
from contact.models import Contato

class ContatoModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'numero', 'hr_enviada', 'mensagem']
    date_hierarchy = 'hr_enviada'
    search_fields = ['nome', 'email', 'numero', 'hr_enviada', 'mensagem']
    list_filter = ['hr_enviada']
    actions = ['respondido']


    def respondido(self, request, queryset):
        count = queryset.update(respondido=True)

        if count == 1:
            msg = "{} email foi respondido"
        else:
            msg = "{} emails já foram respondidos"

        self.message_user(request, msg.format(count))

    respondido.short_description = 'email respondido'

admin.site.register(Contato, ContatoModelAdmin)
