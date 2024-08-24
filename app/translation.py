from modeltranslation.translator import register,   TranslationOptions,translator
from .models import *

@register(Adti)
class AdtiTranslationOptions(TranslationOptions):
    fields = ('nomi','yili', 'malumot')

@register(Prorektor)    
class ProrektorTranslationOptions(TranslationOptions):
    fields = ('ism','malumot','lavozim_nomi')

@register(Rttm_malumot)
class Rttm_malumotTranslationOptions(TranslationOptions):
    fields = ('malumot','rasim')


@register(ATM_raxbar)
class ATM_raxbarTranslationOptions(TranslationOptions):
    fields = ('ism','malumot','lavozim_nomi')

@register(Xodimlari)  
class XodimlariTranslationOptions(TranslationOptions):
    fields = ('ism1','lavozimi','text')


@register (Servis)
class ServisTranslationOptions(TranslationOptions):
    fields = ('nomi','malumot')


@register  (Kompyuter)
class  KompyuterTranslationOptions(TranslationOptions):
    fields = ('nomi','soni')



