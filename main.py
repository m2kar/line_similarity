#!python3
import difflib
import streamlit as st

def lines_similarity(raw_str,threshold) -> str:
    lines=raw_str.split('\n')
    lines=[line.strip() for line in lines if len(line.strip())>0]
    sim_list=[]
    for i in range(len(lines)-1):
        for j in range(i+1,len(lines)):
            sim_list.append((i,j,str_similarity(lines[i],lines[j])))
    
    sim_list=[sim for sim in sim_list if sim[2]>=threshold]
    sim_list.sort(key=lambda x:x[2],reverse=True)
    result="相似度大于{}的行:\n".format(threshold)
    for sim in sim_list:
        # result+=f"{sim[2]:.2f}:\t {sim[0]} <--> {sim[1]}\n".
        result+="{:.2f}:\t 第{}行 <--> 第{}行\n".format(sim[2],sim[0],sim[1])
        # result+=f"第{sim[0]}行:\t{lines[sim[0]]}\n"
        result+="第{}行:\t{}\n".format(sim[0],lines[sim[0]])
        # result+=f"第{sim[1]}行:\t{lines[sim[1]]}\n"
        result+="第{}行:\t{}\n".format(sim[1],lines[sim[1]])
        result+="\n"
    return result


def str_similarity(s1, s2):
    seq = difflib.SequenceMatcher(None, s1, s2)
    return seq.ratio()

def main():
    st.title("重复文献计算——基于行相似度")
    raw_str = st.text_area("输入文本")
    threshold = st.slider("相似度阈值", 0.0, 1.0, 0.6, 0.1)
    if st.button("查找重复文献"):
        result = lines_similarity(raw_str, threshold)
        st.text_area("重复文献", result,disabled=True,height=400)

        
if __name__ == "__main__":
    main()
