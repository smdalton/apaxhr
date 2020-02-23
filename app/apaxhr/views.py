from django.contrib.admindocs.views import ModelDetailView
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView


from core_hr.models import Employee


class HomePage(TemplateView):

    template_name = 'apaxhr/home.html'

    def dispatch(self, request, *args, **kwargs):
        self.access_tier = kwargs.get('access_tier', "access tier not present")
        return super(HomePage, self).dispatch(request, *args, **kwargs)
    tier_list = ['tier0','tier1','tier2','tier3','tier4',]

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        # TODO: Implement user request authentication here
        tier_list = ['tier0', 'tier1', 'tier2', 'tier3', 'tier4', ]
        def pop_session(save_tier='none'):
            for tier in tier_list:
                try:
                    self.request.session.pop(tier)
                    print(tier, " Deactivated")
                except:
                    print(tier, "Not Set")

        if self.access_tier == '0':
            pop_session()
            print('---> tier0 set')
            self.request.session['privilege_level'] = self.access_tier
            self.request.session['tier0']=True

        if self.access_tier == '1':
            pop_session()
            print('---> tier1 set')
            self.request.session['privilege_level'] = self.access_tier
            self.request.session['tier1']=True
            # context['user_is_tier1'] = self.request.user.groups.filter(name='Instructors').exists()
        if self.access_tier == '2':
            pop_session()
            print('---> tier2 set')
            self.request.session['privilege_level'] = self.access_tier
            self.request.session['tier2'] = True

        if self.access_tier == '3':
            pop_session()
            print('---> tier3 set')
            self.request.session['privilege_level'] = self.access_tier
            self.request.session['tier3'] = True

        if self.access_tier == '4':
            pop_session()
            print('---> tier4 set')
            self.request.session['privilege_level']= self.access_tier
            self.request.session['tier4'] = True

        context['privilege_level'] = self.access_tier

        return context