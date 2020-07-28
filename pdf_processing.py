from text_processing import find_top_ngram
import glob
import re
from collections import Counter
from collections import defaultdict

PATH = "/data/datagouv/data_gouv_txt/Enedis"



def get_common_titles():
    titles = re.compile(r'((^[0-9])\.?\s+[A-Z][A-Za-z]+\s?.+)',
                        re.MULTILINE)  # +\s?[A-Za-z]+\s?[A-Za-z]+', re.MULTILINE)
    filos = glob.glob(f"{PATH}/*.txt")
    all_titles = []
    for f in filos:
        with open(f) as filo:
            text = filo.read()

        matcho = titles.findall(text)
        matcho = [(m[0].lower(), m[1]) for m in matcho if "\n" not in m[0]]
        # Rules
        if not matcho:
            # print("no match found")
            continue
        
        id_order = int(matcho[0][1])
        for t in matcho:
            temp = t[0].replace("intro duction", "introduction")
            temp = temp.replace("exp eriment", "experiment")
            temp = temp.replace("metho d", "method")
            temp = temp.replace("mo del", "model")
            if int(t[1]) >= id_order:
                all_titles.append(temp)
                id_order += 1
            # else:
                # print "\t\tno order!"

    # sorted_titles = sort_dict_value(dict(Counter(all_titles)))
    sorted_titles = dict(sorted(Counter(all_titles).items(), key=lambda k: f[1], reverse=True))
    for title, freq in sorted_titles.items():
        print(f"The title {title} was found {freq} times in the corpus.")

    #
    # I cannot remember what was up with this below :(
    #

    # sections_nb = sorted([int(i[0][0]) for i in all_titles])
    # print(Counter(sections_nb))
    # # Get a dictionary with each possible title for each section
    # index_title = defaultdict(list)
    # for tuplo, nb in sorted_titles:
    #     index = int(tuplo[0])
    #     title = tuplo[2:]
    #     index_title[index].append((title, nb))
    #
    # #We got a dicitonary with the section and the title found.
    # #We now try to discover the most important bigrams.
    # for title, txt in index_title.items():
    #     print(find_top_ngram(txt))
    # pass


if __name__ == "__main__":
    get_common_titles()