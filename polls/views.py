import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question, Tags
from django.shortcuts import render

def page4(request):
    return render(request, 'polls/page4.html', context=None)

def page3(request,id):
    resp=poll_details(id)
    q_id = {"id": id}
    resp.update(q_id)
    return render(request, 'polls/page3.html', {'detail': resp})

def graph(request,id):
    response=poll_details(id)
    return JsonResponse(response, safe=False, status=200)

@csrf_exempt
def poll_details(question_id):
    tag_list = []
    vote_list = []
    choice_dict = {}
    choice_list=[]
    question = Question.objects.get(id=question_id)
    tags = Tags.objects.filter(tag1_id=question_id)
    for i in tags:
        tag_list.append(i.tag)
    choice = Choice.objects.filter(question_id=question_id)
    for i in choice:
        choice_dict[i.choice_text] = i.votes
        vote_list.append(i.votes)
        choice_list.append((i.choice_text))
    response = {"Question": question.question_text, "OptionVote": choice_dict, "Tags": tag_list, "votes":vote_list, "choices":choice_list}

    return response


@csrf_exempt
def create_questions(request):
    if request.method == 'POST':
        tag_list = []
        received_json_data = json.loads(request.body)
        updating_question = Question(question_text=received_json_data['Question'], pub_date=timezone.now())
        updating_question.save()

        for key, value in received_json_data['OptionVote'].items():
            updating_choice = Choice(choice_text=key, votes=value, question_id=updating_question.id)
            updating_choice.save()

        for tag_val in received_json_data['Tags']:
            # print(received_json_data['Tags'])
            # print("rec")
            # print(tag_val)
            # print("tagval")
             x = tag_val.split(",")
            # print(x)
            # print("x")
            # print()
        for i in x:
            updating_tag = Tags(tag=i, tag1_id=updating_question.id)
            updating_tag.save()
            #print(updating_tag)
            #print()
        return JsonResponse("Saved successfully", safe=False, status=200)

    elif request.method == 'GET':
        tag_url_val = request.GET.get('Tags')

        if tag_url_val:
            list_of_dict = []
            tag_url_val = tag_url_val.split(",")
            tags = Tags.objects.filter(tag__in=tag_url_val)
            for each_tag in tags:
                a = each_tag.tag1_id
                response = poll_details(a)
                list_of_dict.append(response)
                res = []
                [res.append(x) for x in list_of_dict if x not in res]
            return JsonResponse(res, safe=False, status=200)

        else:
            all_questions = Question.objects.all()
            response_list = []
            for question in all_questions:
                response = poll_details(question.id)
                q_id ={"id": question.id}
                response.update(q_id)
                response_list.append(response)
            return JsonResponse(response_list, safe=False, status=200)


@csrf_exempt
def update_vote(request, id):
        if request.method == 'PUT':
            received_request = json.loads(request.body)
            option = received_request.get('incrementOption')
            choices = Choice.objects.filter(question=id, choice_text=option)
            for each_choice in choices:
                each_choice.votes += 1
                each_choice.save()
            return HttpResponse("yee", status=200)

        elif request.method == 'GET':
            resp = poll_details(id)
            q_id = {"id": id}
            resp.update(q_id)
            #print(resp)
            return render(request, 'polls/page2.html', {'detail': resp})
    # return JsonResponse(response, status=200)


@csrf_exempt
def get_list_all_tags(request):
    set_tags = []
    tags = Tags.objects.all()
    for i in tags:
        set_tags.append(i.tag)
    a = list(set(set_tags))
    response = {"Tags": a}
    return JsonResponse(response, status=200)

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#     def get_queryset(self):
#         """
#                 Excludes any questions that aren't published yet.
#                 """
#         return Question.objects.filter(pub_date__lte=timezone.now())

    '''def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})'''
    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    return HttpResponse("You're looking at question %s." % question_id)'''


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


'''def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)'''

'''def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': "you did'nt select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question, id,)))'''
