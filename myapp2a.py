import streamlit as st
from PyPDF2 import PdfReader
from functionforDownloadButtons import download_button


uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True,type="pdf")
keywords = st.text_input(f"**Write Keywords with commas**")
print(keywords)

comb_pdf_list = []
title = []
title1 = []
for uploaded_file in uploaded_files:

    # print(type(uploaded_file.name))
    if uploaded_file and  keywords is not None:
        reader = PdfReader(uploaded_file)

# print(title)
        num_of_pages = len(reader.pages)
        text_list = []
        for i in range(num_of_pages):

            page = reader.pages[i]
            parts = []


            def visitor_body(text, cm, tm, fontDict, fontSize):
                y = tm[5]
                if y > 50 and y < 750:
                    parts.append(text)


            text = page.extract_text(visitor_text=visitor_body)
            text_list.append(parts)
        values = ' '.join(map(str, text_list))
        print(len(values))
        if len(values) > 10000:
            flat_list = []
            flat_list = [item for sublist in text_list for item in sublist]

            comb_pdf_list.append(flat_list)
            information = reader.metadata
            if len(information.title) > 30:
                title.append(information.title)
            else:
                title.append(uploaded_file.name)
        else:
            # information = reader.metadata
            # if len(information.title) > 30:
            #     title1.append(information.title)
            # else:
            title1.append(uploaded_file.name)
import re

# regex = re.compile(r'[0-9][0-9]+')
regex = re.compile(r'1[1-9]|[2-9]\d|[1-9]\d{2,}')
regex1 = re.compile(r'(\s|^|\.)([^\s\d.]+){3}(\.)')
regex2 = re.compile(r'[1-9](\.)')
g5_list = []
g8_list = []
fil1_list = []
heading_list = []
for i in range(len(comb_pdf_list)):
    filter_list = [city for city in comb_pdf_list[i] if len(city) > 2]
    g5_list.append(filter_list)
    filter_list2 = [city for city in comb_pdf_list[i] if len(city) > 8 and len(city) < 55]
    g8_list.append(filter_list)

# g8_list
for i in range(len(g8_list)):
    fil1 = [i for i in g8_list[i] if not (regex1.search(i) or regex.search(
        i) or '(' in i or ')' in i or '%' in i or '<' in i or '>' in i or '/' in i or '\\' in i or '{' in i or '}' in i or '[' in i or ']' in i or ',' in i or '\n' in i or '-' in i or '=' in i or 'Figure' in i or 'Table' in i)]
    fil1_list.append(fil1)
# fil1_list
n_cal = []
h_list = []
for i in range(len(fil1_list)):
    filtered = [i for i in fil1_list[i] if regex2.search(i) or ':' in i]
    # fil2=[i for i in filtered if not ( regex1.search(i) or regex.search(i) or'(' in i or ')' in i or '%' in i or '<' in i or '>' in i or '/' in i or '\\' in i or '{' in i or '}' in i or '[' in i or ']' in i  or ',' in i or '\n' in i or '-' in i or '=' in i or 'Figure'in i or 'Table' in i ) ]
    # print(len(filtered))
    if len(filtered) < 7:
        n_cal = []
        h_list = []
        # n_list = comb_pdf_list[i].index('\n')
        n_list = [l for l, e in enumerate(comb_pdf_list[i]) if e == '\n']

        for n in range(len(n_list) - 1):
            cal = n_list[n + 1] - n_list[n]
            n_cal.append(cal)
        n_ind_list = [l for l, e in enumerate(n_cal) if e == 2]
        for n in range(len(n_ind_list) - 1):
            h_list.append(comb_pdf_list[i][n_list[n_ind_list[n]] + 1])  # n_list[n_ind_list[n]+1]
        l3_list = [city for city in h_list if len(city) > 3]
        heading_list.append(l3_list)
    else:
        heading_list.append(filtered)

# print(n_list)
# print(n_cal)
# print(n_ind_list)
# print(h_list)
# heading_list
ind = []
for i in range(len(heading_list)):
    ind_sub = []
    for j in range(len(heading_list[i])):

        try:
            ind_sub.append(g5_list[i].index(heading_list[i][j]))

        except ValueError:
            print(heading_list[i][j])
            print('item not present')
    ind.append(ind_sub)

# print(ind)
# len(ind)
outer = []

# print('------------------')
for i in range(len(ind)):
    inner = []
    # print(len(ind[i]))
    for j in range(len(ind[i])):
        # print(j)
        if j < len(ind[i]) - 1:
            # print(ind[i][j])
            # print(g5_list[i][ind[i][j]:ind[i][j+1]])
            # print(ind[j])
            # print(len(ind[i]))
            # print(g5_list[i][0:2])

            inner.append(' '.join(g5_list[i][ind[i][j]:ind[i][j + 1]]))

    outer.append(inner)

# outer
# text_list
# print(outer)
# ------------------------------------------------------
Input = ['abstract']  #
Input_string = heading_list

Output = Input_string.copy()
temp_abs = []
temp_outer = []
# print(len(Input_string))

# Using iteration

len_temp = []
outer_temp = []
for elem in range(len(Input_string)):
    i = 0
    flag = 0
    for elem1 in Input_string[elem]:

        for n in Input:
            if n.lower() in elem1.lower():
                # print(elem1)
                s_text = "Title :  " + title[elem] + '\n\n ' + elem1 + '\n\n '
                # print(s_text)
                # print(g5_list[elem].index(elem1))
                ind_abs = g5_list[elem].index(elem1)
                ind_abs1 = g5_list[elem].index(heading_list[elem][i + 1])
                # print(g5_list[elem].index(heading_list[elem][i+1]))
                abs = g5_list[elem][ind_abs:ind_abs1]
                # print(' '.join(abs))
                print(abs)
                print(len(abs))
                abs1 = ' '.join(abs)
                print(abs1)
                temp_abs.append(abs1)
                print('main')
                flag = 1

        # i=i+1

        # else:
        # 	temp.append('No data found')
        i = i + 1
    # print('ele',elem)
    len_temp.append(len(temp_abs))
    # print(len_temp)

    if elem > 0:
        if len_temp[elem] - len_temp[elem - 1] == 0 or flag == 0:
            print('first if')
            ind_abs3 = g5_list[elem].index(heading_list[elem][0])
            ind_abs4 = g5_list[elem].index(heading_list[elem][2])
            abs = g5_list[elem][ind_abs3:ind_abs4]
            # print(abs)
            abs1 = ' '.join(abs)
            temp_abs.append(abs1)


    else:
        if len_temp[elem] == 0 and elem == 0:  #
            print('2nd if')
            ind_abs3 = g5_list[elem].index(heading_list[elem][0])
            ind_abs4 = g5_list[elem].index(heading_list[elem][1])###############
            abs = g5_list[elem][ind_abs3:ind_abs4]
            # print(abs)
            abs1 = ' '.join(abs)
            temp_abs.append(abs1)
# outer_temp.append(temp)
# print('abc')

# temp
# len_temp
def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


# ----------------------------------2nd----------------------------------------------------------
Input = ['conclusion']  #
Input_string = heading_list

Output = Input_string.copy()

# print(len(Input_string))

# Using iteration

len_temp = []
outer_temp_con = []

for elem in range(len(Input_string)):
    temp = []
    i = 0
    flag = 0
    temp2 = []
    count = sum('conclusion' in s.lower() for s in heading_list[elem])
    # print(count)
    if count > 1:
        abc = ['conclusion' in s.lower() for s in heading_list[elem]]
        # print(abc)
        cde = find_indices(abc, True)
        # print(cde)
        # print(cde[-1])
        # print(heading_list[elem][cde[-1]])
        ind_col = g5_list[elem].index(heading_list[elem][cde[-1]])
        # print(ind_col)
        ind_col1 = g5_list[elem].index(heading_list[elem][cde[-1] + 1])
        # print(ind_col1)
        conclu = g5_list[elem][ind_col:ind_col1]
        # print(conclu)
        temp.append(' '.join(conclu))
    elif count == 1:

        abc = ['conclusion' in s.lower() for s in heading_list[elem]]
        print(abc)
        cde = find_indices(abc, True)
        print(cde[-1])
        print(len(abc))
        if cde[-1] == len(abc) - 1:
            # print(cde[-1])
            print(heading_list[elem][cde[-1]])
            ind_col = g5_list[elem].index(heading_list[elem][cde[-1]])
            print(ind_col)
            # ind_col1 = g5_list[elem].index(heading_list[elem][cde[-1]+1])
            conclu = g5_list[elem][ind_col:len(g5_list[elem])]
            print(conclu)
            temp.append(' '.join(conclu))
        else:
            ind_col = g5_list[elem].index(heading_list[elem][cde[-1]])
            # print(ind_col)
            ind_col1 = g5_list[elem].index(heading_list[elem][cde[-1] + 1])
            # print(ind_col1)
            conclu = g5_list[elem][ind_col:ind_col1]
            temp.append(conclu)
    else:
        temp.append("Conclusion not Found")
    print(temp)
    outer_temp_con.append(' '.join(temp[0]))

# outer_temp_con
# key_words = input('Enter key_words of a list separated by space ')
# print("\n")
# user_list = key_words.split()
# print list
# print('Keyword list: ', user_list)
# Input = ['Scope and Method', 'abstract']  #
# Input_string = outer
user_list = keywords.split(", ")
# print list
# print('Keyword list: ', user_list)
Input = user_list  #
Input_string = outer

Output = Input_string.copy()
temp_final = []
# print(len(Input_string))

# Using iteration
for elem in range(len(Input_string)):
    for elem1 in Input_string[elem]:
        for n in Input:
            if n.lower() in elem1.lower():
                # print(elem1)
                s_text = "Title :  " + title[elem] + '\n\n ' + temp_abs[elem] + '\n\n ' + elem1 + '\n\n ' + \
                         outer_temp_con[elem] + '\n\n '
                temp_final.append(s_text)
# temp_final
# # Using iteration
# for elem in Input_string:
# 	for n in Input:
# 		if n.lower() in elem.lower():
# 			temp.append(elem)

used = set()
# # mylist = [u'nowplaying', u'PBS', u'PBS', u'nowplaying', u'job', u'debate', u'thenandnow']
unique = [x for x in temp_final if x not in used and (used.add(x) or True)]
# unique
st.write(f'**OutPut Text**',unique)

file = open('uique2.txt', 'w',encoding="utf-8")
for item in unique:
    file.write(item + "\n")
file.close()
if unique is not None:
    c29, c30, c31 = st.columns([1, 1, 2])


    with c29:
        with open('uique2.txt','rb') as f:
            st.download_button(f'**Download TXT File**', f)


st.write(f'**Not Processes Document List:**',title1)
