from django.contrib import admin
from django.utils.html import format_html
from core.models import Speaker, ContactSpeaker

class ContactInline(admin.TabularInline):
    model = ContactSpeaker
    extra = 1

class SpeakerModelAdmin(admin.ModelAdmin):
    inline = [ContactInline]
# Register your models here.
