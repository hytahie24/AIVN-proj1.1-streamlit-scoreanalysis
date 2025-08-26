import matplotlib.pyplot as plt 
import pandas as pd 
import streamlit as st
st.title("Phân tích dữ liệu điểm số học sinh")
upload_file = st.file_uploader("chọn file Excel (có cột điểm số):", type = ["xlsx"])
def calc_average(scores): 
    return sum(scores)/len(scores)

def percentage_distribution(scores): 
    bins = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "<60": 0}
    for score in scores: 
        if score >= 90: 
            bins["90-100"] +=1
        elif score >= 80: 
            bins["80-89"] +=1
        elif score >= 70: 
            bins["70-79"] +=1
        elif score >= 60: 
            bins["60-69"] +=1
        else: bins["<60"] +=1
    return bins

#đọc file 
df = pd.read_excel(upload_file)

#xử lý danh sách điểm số 
scores = df["Điểm số"].dropna().astype(float).tolist()

#Hiển thị các chỉ số
st.write("Tổng số học sinh: ", len(scores))
st.write("Điểm trung bình: ", round(calc_average(score),2))

#vẽ biểu đồ 