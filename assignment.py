import streamlit as st
st.title('Trà sữa CoTAI')
col1,col2 = st.columns(2)
with col1:
    st.image('https://i.imgur.com/lEpdPsT.jpeg')
with col2:
    size = str(st.radio('Kích cỡ',('Nhỏ (30K)','Vừa (40K)','Lớn (50K)'),horizontal=True))
    size_price = {"Nhỏ (30K)": 30, "Vừa (40K)": 40, "Lớn (50K)": 50}
    size_text = size.lower()
    size_text = size_text[:3]
    st.text('Thêm')
    col3,col4 = st.columns(2)
    with col3:
        S = st.checkbox('Sữa (5K)')
        C = st.checkbox('Cà phê (8K)')
    with col4:
        K = st.checkbox('Kem (10K)')
        T = st.checkbox('Trứng (15K)')
col5,col6 = st.columns(2)
with col5:

    list = st.multiselect('Topping',['Trân châu trắng (5K)','Trân châu đen (5K)','Thạch rau câu (6K)','Vải (7K)','Nhãn (8K)','Đào (10K)'])
with col6:
    quan = st.number_input('Số lượng',1)
note = st.text_area('Ghi chú','')
extra_items = []
extra_price = 0
if S: 
    extra_items.append('Sữa')
    extra_price += 5
if C: 
    extra_items.append('Cà phê')
    extra_price += 8
if K: 
    extra_items.append('Kem')
    extra_price += 10
if T: 
    extra_items.append('Trứng')
    extra_price += 15
topping = {'Trân châu trắng (5K)': 5, 'Trân châu đen (5K)': 5, 'Thạch rau câu (6K)': 6,'Vải (7K)': 7, 'Nhãn (8K)': 8, 'Đào (10K)': 10}
sum = size_price[size] + extra_price + sum(topping[i] for i in list)
total = sum*quan
if st.button('Đặt hàng',use_container_width=True):
    st.success(f'Cỡ {size_text} \n\nThêm: {', '.join(extra_items)} \n\nTopping: {', '.join(list)} \n\n{note}\n\nSố lượng: {quan}\n\nThành tiền: {total}K')