def filterBible(scripture, book, chapter):
    my_filter=[]
    for i in range(0,len(scripture)):
        id_script=scripture[i]
        if book==id_script[0:2] and chapter==id_script[2:5]:
            my_filter.append(id_script)
    return my_filter

scripture=["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]
book="01"
chapter="001"
print(filterBible(scripture, book, chapter))
