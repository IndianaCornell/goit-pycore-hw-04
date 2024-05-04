def get_cats_info(path):
    try:
        with open (path, "r", encoding="utf-8") as f:
            cats_f = [el.strip() for el in f.readlines()]
            cats_count = len(cats_f)

            if cats_count:

                cats_info_list = []

                for cat in cats_f: 
                    cat_info = cat.split(",")
                    cat_dict= {"id": cat_info[0], "name": cat_info[1], "age":cat_info[2]}
                    cats_info_list.append(cat_dict)
                    
                print(cats_info_list)

            else: 
                print("Ваш файл порожній.")
    except FileNotFoundError:
        print("Файл не знайдено.")
  

get_cats_info("task02/cats.txt")
