import pandas as pd

def matrice_concordance(datframe):
    datframe=datframe.reset_index(drop=True)
    df_sortie=pd.DataFrame(index=datframe.columns,columns=datframe.columns)    
    a=0
    for i in df_sortie.columns:
        a+=1
        print(a/len(datframe.columns))
        for z in df_sortie.columns:
            count=0
            for m in range(len(datframe)):
                if datframe[i][m]==1 and datframe[z][m]==1:
                    count+=1 
            df_sortie[i][z]=count
    return df_sortie

def support(df,calculated=False):
    df_sortie=pd.DataFrame(columns=['Produit 1','Produit 2','Support'])
    if calculated:
        M=df
    else :
        M=matrice_concordance(df)
    for i in M.columns:
        for z in M.columns:
            df_sortie.loc[len(df_sortie)] = [i,z,M[i][z]]
    return df_sortie

def confiance(df,df_sortie):
    ret=[]
    for i in df.columns:
        cache=sum(df[i])
        for m in df.columns:
            ret.append(round(df[i][m]/cache,3))
    return df_sortie.assign(Confiance=ret)

def confiance_attendue(df,df_sortie):
    ret=[]
    for m in df_sortie['Produit 2']:
        ret.append(sum(df[m])/len(df))
    return df_sortie.assign(confiance_attendue=ret)    

def lift(df_sortie):
    return df_sortie.assign(Lift=df_sortie.Confiance/df_sortie.confiance_attendue) 