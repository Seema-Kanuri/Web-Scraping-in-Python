
# coding: utf-8

# In[ ]:
import pandas as pd
col_names =  ['CareTypeDesc',
 'CareTypeID',
 'Charge',
 'DefaultPricingDuration',
 'RoomType',
 'RoomTypeDescription',
 'RoomTypeId',
 'Page']
df_final  = pd.DataFrame(columns = col_names)

with open("P:/Text/List_part2.txt") as file:
#with open("C:/Users/Seema.Kanuri/Documents/a.txt") as file:
    for var in file:
        #print(var)
        from urllib.request import urlopen
        from urllib.request import Request, urlopen
        req = Request(var, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(webpage)
        import re
        for elem in soup(text=re.compile(r'RoomTypeId')):
            #print(elem.parent)
            mytext = elem.parent
        
        soup_string = str(mytext)
        sub_strig = re.sub(r'.*CommunityRoomPrices":', 'CommunityRoomPrices = ', soup_string)
        sub_strig1 = re.sub(',"Rating".*$', "", sub_strig)
        sub_strig2 = re.sub(r'.*\[{"RoomTypeId":', '[{"RoomTypeId":', sub_strig1)
        import ast
        user = ast.literal_eval(sub_strig2)
        import pandas as pd
        df = pd.DataFrame(user)
        df['Page'] = var
        df_final = df_final.append(df,ignore_index=True)
        #masterDF = masterDF.append(tempDF,ignore_index=True)
        print("----------------------------------------------------")
        print(var)
        
    


# In[ ]:


df_final.to_csv('P:/Output/List.csv', sep=',')


# In[ ]:


var


# In[ ]:


df_final


# In[ ]:


#del var

