from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Company, Organization


class CompanySignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    address = forms.CharField(required=True)
    mobile_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = Company.objects.create(user=user)
        company.name = self.cleaned_data.get("name")
        company.email = self.cleaned_data.get("email")
        company.mobile_number = self.cleaned_data.get("mobile_number")
        company.address = self.cleaned_data.get("address")
        company.save()
        return user


class OrganizationSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    address = forms.CharField(required=True)
    mobile_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_organization = True
        user.save()
        organization = Organization.objects.create(user=user)
        organization.name = self.cleaned_data.get("name")
        organization.mobile_number = self.cleaned_data.get("mobile_number")
        organization.address = self.cleaned_data.get("address")
        organization.email = self.cleaned_data.get("email")
        organization.save()
        return user
