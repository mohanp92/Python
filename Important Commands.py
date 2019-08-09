Missing value function
--------------------------------------------------------------
def missingvalue(df):
    total=df.isnull().sum().sort_values(ascending=False)
    percent=round((df.isnull().sum().sort_values(ascending=False)/(len(df))*100), 2)
    missing_df=pd.concat([total,percent], axis=1, keys=['Total','Precent'])
    return missing_df
    -----------------------------
    
Replace missing value
titanic.Survived.replace(to_replace= ["yes", "no"], value = [1, 0], inplace = True)

Rename the columns
summer.rename(columns = {"Athlete Name": "Athlete_Name"}, inplace = True)
---------------------------------------------------------------------------
summer.Medal.replace(to_replace= "Gold Medal", value = "Gold", inplace = True)
-----------------------------------------------------------------------------
To Replace string from the column
titanic.Fare = titanic.Fare.str.replace("$", "")
------------------------------------------------------------------------------
To Search something from the column  then use str.contain(")
summer.loc[summer.Athlete.str.contains("HAJOS")]
---------------------------------------------------------------
Convert the vlaues in to numeric then use pd.numeric
 pd.to_numeric(titanic.Fare)
--------------------------------------------------
To Change the data type of column then
pd.to_numeric(titanic.Fare) then
use astype titanic["Fare"] = titanic.Fare.astype("float")
 --------------------------------------------------------
 we will get the only missing value rows and columns
  titanic.loc[titanic.isna().any(axis=1)]
 ------------------------------------------------------------
                                                          
                                                          
                                                          
                                                          
                                                          
    
