Missing value function
--------------------------------------------------------------
def missingvalue(df):
    total=df.isnull().sum().sort_values(ascending=False)
    percent=round((df.isnull().sum().sort_values(ascending=False)/(len(df))*100), 2)
    missing_df=pd.concat([total,percent], axis=1, keys=['Total','Precent'])
    return missing_df
    -----------------------------

    
