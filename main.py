import streamlit as st
import numpy as np
import pandas as pd
 
"""
都道府県コード    object
都道府県名      object
元号         object
和暦（年）       int64
西暦（年）       int64
注          object
人口（総数）      int64
人口（男）       int64
人口（女）       int64
"""
 
 
# CSVの読み込み
df = pd.read_csv("c01.csv", encoding="shift_jis")
 
# 全国データのみの抜き出し
region_name = st.text_input("都道府県名を入力してください", "全国")
df = df[
    df["都道府県名"] == region_name
]
# 行を西暦で並び替え
df = df.sort_values("西暦（年）")
 
# 不要な列の削除
df = df[["西暦（年）", "人口（総数）", "人口（男）", "人口（女）"]]
 
# Viewer
st.title(f"{region_name}の人口動態の推移")
 
if st.toggle("生データの表示"):
    st.dataframe(df)
 
st.header("国勢調査の結果")
st.area_chart(df, x="西暦（年）")