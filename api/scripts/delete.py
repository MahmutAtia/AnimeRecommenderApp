from anime.models import Anime
def run():
    qs = Anime.objects.all()
    titles=[]
    qs_final = []
    qs_del = []
    for obj in qs:
        if obj.title in titles:
            qs_del.append(obj.id)
        else:
            titles.append(obj.title)
           
    delete_all = qs.filter(id__in = qs_del)
    print("all : " ,len(qs))
    print("titles : " ,len(titles))
    print("delet : " ,len(delete_all))
    # delete_all.delete()
    # print("deleted")
    

  

    