from .models import Setting,Service

def global_data(request):
    data={
            'settingData': Setting.objects.first(),
            'menuServiceData': Service.objects.all(),
    }

    return data