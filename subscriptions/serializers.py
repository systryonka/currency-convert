import rest_framework.serializers as serializers


from subscriptions.models import Subscription

class SubscriptionCreation(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('full_name', 'short_name')

class SubscriptionDetailedView(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('short_name', 'users')
