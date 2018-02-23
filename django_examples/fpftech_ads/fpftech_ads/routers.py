class DatabaseRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['accounts', 'auth']:
            return 'accounts'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['accounts', 'auth']:
            return 'accounts'
        return None
