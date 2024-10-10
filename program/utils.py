def regroup(liste_regroup,data_store,col):
    for n in range(len(liste_regroup)):
        for i in range(len(data_store)):
            if data_store[col][i] in liste_regroup[n][1]:
                data_store[col][i]=liste_regroup[n][0]
    return data_store