from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from forma.db import get_db
from forma.utils import FieldTypes, take_forms


def get_all_forms(request):
    return HttpResponse(
        [f'{i}\n' for i in get_db().all()],
        content_type='text/plain; charset=utf8'
    )


@csrf_exempt
def get_form(request, *args, **kwargs):
    context = {'result': ''}
    if request.method == "POST":
        requests_post = request.POST.copy()
        requests_post.pop('csrfmiddlewaretoken', None)
        db = get_db()
        if requests_post:
            keys = requests_post.keys()
            for k in keys:
                requests_post[k] = FieldTypes.get_type(requests_post[k])  
            result_forms = take_forms(db.all(), requests_post)
            if result_forms:
                context['result'] = (
                    'Подходящие формы для вас:\n '+'\n '.join(result_forms)
                )
            else:
                context['result'] = (
                    "К сожалению, форма не найдена, по вашему  запросу \n"
                    "должна быть такая форма \n{\n      "+',\n      '.join(
                        [f'{x}: {y}' for x, y in requests_post.items()])+'\n}'
                )
        else:
            context['result'] = 'Запрос не может быть пустым'
    return HttpResponse(context['result'])
