from .models import Setting

def global_data(request):
    data={
            'settingData': Setting.objects.first(),
    }

    return data