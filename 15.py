# kaggle.com-dataset+code
# uci.com-only dataset
# huggingface-dataset and code for llm
import pandas as pd
rating=pd.read_csv(r'c:\Users\ADMIN\Downloads\archive\rating.csv')
print(rating.shape)
tag=pd.read_csv(r'c:\Users\ADMIN\Downloads\archive\tag.csv')
print(tag.shape)
movie=pd.read_csv(r'c:\Users\ADMIN\Downloads\archive\movie.csv')
print(movie.shape)
print(tag.iloc[0])