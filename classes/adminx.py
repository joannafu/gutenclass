import xadmin
from .models import Class
#from attachments.admin import AttachmentInlines

class ClassOptions(object):
    pass

xadmin.site.register(Class, ClassOptions)
