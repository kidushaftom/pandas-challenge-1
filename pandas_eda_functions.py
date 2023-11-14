
def get_data_info(df):
    
    """
    Function to produce 
       1.Column names
       2.Column data type
       3.Non-null count for each column
       4.Missing value for each column 
    """
    import pandas as pd
    
    info_df = pd.DataFrame({
    # column name list
    'Column': df.columns,  
    
    # Non-null count for each column
    'Non-Null Count': df.count().values,
    
    #Data type for each column
    'Dtype': df.dtypes.values, 
     
     #Missing value count          
    "Missing Count": df.isna().sum()})
    print("Let's look at data type and missing values count")
    print("_______________________________________________________________________________")
    print(info_df.reset_index(drop=True))

#######################################################################################################

def top_n_for_two_features(df,col1,col2,n):
    
    """
    Function to get top n of first column and fillters value to n and
    get top n of the second column
    """

    #get value count for first columns
    counts_df = df[col1].value_counts().\
    sort_values(ascending=False).\
        reset_index()
    
    #Get top 1 value  of first column
    top_category = counts_df.loc[counts_df['count'].idxmax()]

    print(f"Top catagory is: {top_category[col1]} with {top_category['count']} entry")
    print("__________________________________________________________________________________________________")
    print(counts_df)
    print("__________________________________________________________________________________________________")
    
    #Filter df using top 1 of first column
    top_category_data = df[col1] == top_category[col1]
    
    #get value count of second column
    subcategory_count = df.loc[top_category_data, :][col2].\
    value_counts().reset_index()
   

    top_subcategory = subcategory_count.loc[subcategory_count['count'].idxmax()]
    print(f"from {top_category['category']} Top sub_catagory is: {top_subcategory['subcategory']} with {top_subcategory['count']} entry")
    print('________________________________________________________________________________________________')
    print(subcategory_count)

###########################################################################################################################################

def top_n(df,col, n):
    
    """
    function to return top n of a given column
    """
    
    #value count and sort descending of a givencolumn
    client_df = df[col].value_counts().\
    sort_values(ascending=False).\
        reset_index().sort_values(by='count', ascending=False)
        
    print(f"top {n} {col} are")
    print("____________________________________________________________")
    print(client_df.head(n))
    
    #get list of top n of a given column
    return  list(client_df.head(n)[col])

############################################################################################################
def get_agg_value(df,cat,value,list_to_filter):
    """
    return a aggrigated value of a given columns and list 
    
    df is data frame
    cat is categorical column
    value is numerical value
    list_to_filter is list to fillter after aggrigation
    """
    #Aggrigate given category and value
    agg_data = df.groupby(cat)[value].sum().reset_index()
    
    #Return aggrigated value of a given list
    return agg_data[agg_data[cat].isin(list_to_filter)].reset_index(drop = True)
    
    
    





    


