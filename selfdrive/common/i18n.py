import gettext


localedir = '../assets/locales'
local = ['ar_EG']
i18n = gettext.translation(localedir=localedir, fallback=True, languages=local)

i18n.install()

_ = i18n.gettext
