from django.contrib import admin

from interactions.models import Fallback
from interactions.models import Followup
from interactions.models import TwilioNumber
from interactions.models import Action
from interactions.models import User
from interactions.models import Inbound
from interactions.models import Outbound


admin.site.register(Fallback)
admin.site.register(Followup)
admin.site.register(TwilioNumber)
admin.site.register(Action)
admin.site.register(User)
admin.site.register(Inbound)
admin.site.register(Outbound)


