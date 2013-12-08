 # -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _ #引用国际化i18n
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import Book,UserProfile

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','isbn', 'author','publisher','available','create_time',
                    'borrower','borrow_date','return_date')
    #list_display = ('id','title','isbn', 'author',)
    list_filter = ('pubdate','publisher',)
    search_fields = ('id','title','isbn','author','translator','publisher','summary','author_intro',)
    ordering = ('id',)
    fields = ('title','isbn','author','author_intro','translator','price','publisher','pubdate',
              'summary','cover_img','available','borrower','borrow_date','return_date')
    list_per_page=20



class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    #fk_name = 'user'
    max_num = 1

class UserProfileAdmin(UserAdmin):
    #filter_horizontal = ('borrowed_book',)
    inlines = [UserProfileInline, ] #这样就可以在admin的用户管理页面中对扩展字段进行操作了





admin.site.unregister(User) #卸载user admin，并重新注册
admin.site.register(User, UserProfileAdmin)

admin.site.register(Book,BookAdmin)