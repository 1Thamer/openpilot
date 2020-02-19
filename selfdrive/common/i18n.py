import gettext
from common import android

supported_language = ['en-US', 'ar-EG']
localedir = '../assets/locales'

is_android = android.ANDROID
local = android.getprop(ro.product.locale) #if is_android else 
i18n = gettext.translation('messages', localedir=localedir, fallback=True, languages=local)

i18n.install()

_ = i18n.gettext
