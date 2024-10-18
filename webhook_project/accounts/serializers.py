from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'account_id', 'account_name', 'app_secret_token', 'website']
        read_only_fields = ['account_id', 'app_secret_token']