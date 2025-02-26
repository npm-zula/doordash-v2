from django.contrib.sessions.backends.db import SessionStore as DbSessionStore
from user.models import CartItem


class SessionStore(DbSessionStore):
    def cycle_key(self):
        old_session_key = super(SessionStore, self).session_key
        super(SessionStore, self).cycle_key()
        self.save()

        CartItem.objects.filter(session_key=old_session_key).update(
            session_key=self.session_key)
