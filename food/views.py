from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
# Create your views here.
import requests


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('index')

# @csrf_protect
# def upload(request):
#     img = request.GET['submit']
#     return render(request,'result.html',{'img':img},content_type='application/xhtml+xml')


def index(request):
    # MEDIA_URL = '/home/manjeet/Manjeet/django/DishPrediction/media/'
    # urls_list = [
    #     MEDIA_URL + image_path for image_path in Post.objects.values_list('foodimage', flat=True)]
    # print(urls_list)
    # api_key = 'acc_26d9c07fbcb2472'
    # api_secret = 'ad2cffbb1101269a0203b25cf0a59c55'
    # image_path = urls_list[-1]
    # print(image_path)
    # response = requests.post('https://api.imagga.com/v2/tags',auth=(api_key, api_secret),files={'image': open(image_path, 'rb')})
    # print(response.json())
    # results = response.json()
    # result = results["result"]["tags"]
    res = [{'confidence': 65.4449005126953, 'tag': {'en': 'sidecar'}}, {'confidence': 60.8709297180176, 'tag': {'en': 'motorcycle'}}, {'confidence': 55.051586151123, 'tag': {'en': 'vehicle'}}, {'confidence': 51.8417320251465, 'tag': {'en': 'moped'}}, {'confidence': 51.1893043518066, 'tag': {'en': 'conveyance'}}, {'confidence': 48.0009727478027, 'tag': {'en': 'motor scooter'}}, {'confidence': 40.6870384216309, 'tag': {'en': 'minibike'}}, {'confidence': 38.4730529785156, 'tag': {'en': 'wheeled vehicle'}}, {'confidence': 35.9828338623047, 'tag': {'en': 'car'}}, {'confidence': 35.8463287353516, 'tag': {'en': 'transportation'}}, {'confidence': 30.9685859680176, 'tag': {'en': 'motor'}}, {'confidence': 26.3434295654297, 'tag': {'en': 'bike'}}, {'confidence': 25.9723949432373, 'tag': {'en': 'engine'}}, {'confidence': 23.7330932617188, 'tag': {'en': 'transport'}}, {'confidence': 23.5702362060547, 'tag': {'en': 'wheel'}}, {'confidence': 22.9556331634521, 'tag': {'en': 'auto'}}, {'confidence': 22.0151233673096, 'tag': {'en': 'automobile'}}, {'confidence': 21.7201652526855, 'tag': {'en': 'metal'}}, {'confidence': 21.3198223114014, 'tag': {'en': 'motor vehicle'}}, {'confidence': 21.0551567077637, 'tag': {'en': 'speed'}}, {'confidence': 20.766393661499, 'tag': {'en': 'road'}}, {'confidence': 19.5310840606689, 'tag': {'en': 'wheels'}}, {'confidence': 18.7441120147705, 'tag': {'en': 'motorbike'}}, {'confidence': 16.7830772399902, 'tag': {'en': 'power'}}, {'confidence': 16.6391067504883, 'tag': {'en': 'seat'}}, {'confidence': 16.3676624298096, 'tag': {'en': 'windshield'}}, {'confidence': 16.067512512207, 'tag': {'en': 'drive'}}, {'confidence': 15.9813871383667, 'tag': {'en': 'pillion'}}, {'confidence': 15.0682106018066, 'tag': {'en': 'chrome'}}, {'confidence': 14.1875782012939, 'tag': {'en': 'machine'}}, {'confidence': 13.7448225021362, 'tag': {'en': 'wreck'}}, {'confidence': 13.635422706604, 'tag': {'en': 'danger'}}, {'confidence': 12.6697101593018, 'tag': {'en': 'travel'}}, {'confidence': 12.6029939651489, 'tag': {'en': 'ride'}}, {'confidence': 11.9687757492065, 'tag': {'en': 'metallic'}}, {'confidence': 11.9636535644531, 'tag': {'en': 'safety'}}, {'confidence': 11.9403190612793, 'tag': {'en': 'support'}}, {'confidence': 11.6801557540894, 'tag': {'en': 'tire'}}, {'confidence': 11.4894199371338, 'tag': {'en': 'steel'}}, {'confidence': 11.4168910980225, 'tag': {'en': 'man'}}, {'confidence': 10.916579246521, 'tag': {'en': 'screen'}}, {'confidence': 10.9100971221924, 'tag': {'en': 'protection'}}, {'confidence': 10.8432559967041, 'tag': {'en': 'biker'}}, {'confidence': 10.8009052276611, 'tag': {'en': 'hood'}}, {'confidence': 10.6788339614868, 'tag': {'en': 'driver'}}, {
        'confidence': 10.5945301055908, 'tag': {'en': 'people'}}, {'confidence': 10.4451522827148, 'tag': {'en': 'traffic'}}, {'confidence': 10.2443981170654, 'tag': {'en': 'industry'}}, {'confidence': 9.87130069732666, 'tag': {'en': 'chopper'}}, {'confidence': 9.7796516418457, 'tag': {'en': 'crash'}}, {'confidence': 9.75727558135986, 'tag': {'en': 'cycle'}}, {'confidence': 9.71897411346436, 'tag': {'en': 'mechanical'}}, {'confidence': 9.64251899719238, 'tag': {'en': 'broken'}}, {'confidence': 9.57766914367676, 'tag': {'en': 'repair'}}, {'confidence': 9.54759979248047, 'tag': {'en': 'race'}}, {'confidence': 9.34299659729004, 'tag': {'en': 'fast'}}, {'confidence': 9.05864143371582, 'tag': {'en': 'sport'}}, {'confidence': 9.01132297515869, 'tag': {'en': 'black'}}, {'confidence': 8.90318393707275, 'tag': {'en': 'technology'}}, {'confidence': 8.80695056915283, 'tag': {'en': 'parts'}}, {'confidence': 8.71461582183838, 'tag': {'en': 'weapon'}}, {'confidence': 8.70895290374756, 'tag': {'en': 'powerful'}}, {'confidence': 8.70308494567871, 'tag': {'en': 'insurance'}}, {'confidence': 8.6950569152832, 'tag': {'en': 'shiny'}}, {'confidence': 8.68725776672363, 'tag': {'en': 'light'}}, {'confidence': 8.68669319152832, 'tag': {'en': 'military'}}, {'confidence': 8.6637487411499, 'tag': {'en': 'helmet'}}, {'confidence': 8.64822483062744, 'tag': {'en': 'protective covering'}}, {'confidence': 8.5523796081543, 'tag': {'en': 'outside'}}, {'confidence': 8.55065822601318, 'tag': {'en': 'uniform'}}, {'confidence': 8.27985382080078, 'tag': {'en': 'street'}}, {'confidence': 8.18982791900635, 'tag': {'en': 'device'}}, {'confidence': 8.16972732543945, 'tag': {'en': 'industrial'}}, {'confidence': 8.03986740112305, 'tag': {'en': 'detail'}}, {'confidence': 7.94665098190308, 'tag': {'en': 'lifestyle'}}, {'confidence': 7.865234375, 'tag': {'en': 'forces'}}, {'confidence': 7.8204870223999, 'tag': {'en': 'racing'}}, {'confidence': 7.81587505340576, 'tag': {'en': 'cars'}}, {'confidence': 7.79549074172974, 'tag': {'en': 'army'}}, {'confidence': 7.74591493606567, 'tag': {'en': 'traveling'}}, {'confidence': 7.72770500183105, 'tag': {'en': 'driving'}}, {'confidence': 7.68992757797241, 'tag': {'en': 'war'}}, {'confidence': 7.66498279571533, 'tag': {'en': 'special'}}, {'confidence': 7.66138458251953, 'tag': {'en': 'old'}}, {'confidence': 7.64912271499634, 'tag': {'en': 'sky'}}, {'confidence': 7.61319637298584, 'tag': {'en': 'engineering'}}, {'confidence': 7.60247421264648, 'tag': {'en': 'dangerous'}}, {'confidence': 7.46466732025146, 'tag': {'en': 'iron'}}, {'confidence': 7.41691923141479, 'tag': {'en': 'lights'}}, {'confidence': 7.08685731887817, 'tag': {'en': 'person'}}, {'confidence': 7.06243896484375, 'tag': {'en': 'work'}}]
    # food = res[0]['tag']['en']
    food = 'banana'
    results = {}
    import requests
    URL = f"https://www.indianhealthyrecipes.com/{food}/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    ingredient_p = soup.find(
        'div', attrs={'class': 'wprm-recipe-ingredient-group'})
    ingre_inpu = ingredient_p.findAll('input')
    ingredient = []
    for i in ingre_inpu:
        if i.has_attr("aria-label"):
            ingredient.append(i['aria-label'])
    print('ingredient\n\n')
    print(ingredient)
    print('\n')
    results['ingredient'] = ingredient
    instruction_p = soup.findAll(
        'div', attrs={'class': 'wprm-recipe-instruction-group'})
    pre_inpu = instruction_p[0].findAll('input')
    preparation = []
    for i in pre_inpu:
        if i.has_attr("aria-label"):
            preparation.append(i['aria-label'])
    print('preparation\n\n')
    print(preparation)
    print('\n')
    results['preparation'] = preparation
    final_inpu = instruction_p[1].findAll('input')
    final = []
    for i in final_inpu:
        if i.has_attr('aria-label'):
            final.append(i['aria-label'])
    print('making banana bread\n\n')
    print(final)
    print('\n')
    results['final'] = final
    # print(result['hits'][0]['recipe'])
    # results = result['hits']
    print(results)
    return render(request, 'result.html', {'result': results})
