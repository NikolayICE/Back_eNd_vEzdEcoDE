import vk_api

access_token = 'ZSj6ZxtwjToFVLfsUn9fngs40fKCSRzCrmofYjSzyJc_AQDngwUZRW5ar0XjClMM2usrxaQkrfSWID71exnJZOj' \
               '3A6Swe_lD4pV2NO5vH77FGZYPZUdlc4pAycQFruCi7g6TQgnq3FrPA5lYcu2LN1FrbMYuG9GCQolFjfExRQgc'
vk_session = vk_api.VkApi('login', 'password') # вместо login и password нужно ввести ваши даннные для входа в VK
vk_session.auth()
api = vk_session.get_api()

mem_photo_link = ['https://vk.com/photo-197700721_457240646', 'https://vk.com/photo-197700721_457240647',
                  'https://vk.com/photo-197700721_457240648', 'https://vk.com/album-197700721_281940823',
                  'https://vk.com/photo-197700721_457240650', 'https://vk.com/photo-197700721_457240652',
                  'https://vk.com/photo-197700721_457240653', 'https://vk.com/photo-197700721_457240659',
                  'https://vk.com/photo-197700721_457240660', 'https://vk.com/photo-197700721_457240664',
                  'https://vk.com/photo-197700721_457240665', 'https://vk.com/photo-197700721_457240667',
                  'https://vk.com/photo-197700721_457240669', 'https://vk.com/photo-197700721_457240671',
                  'https://vk.com/photo-197700721_457240672', 'https://vk.com/photo-197700721_457240673',
                  'https://vk.com/photo-197700721_457240674', 'https://vk.com/photo-197700721_457240675',
                  'https://vk.com/photo-197700721_457240676', 'https://vk.com/photo-197700721_457240677',
                  'https://vk.com/photo-197700721_457240678', 'https://vk.com/photo-197700721_457240679',
                  'https://vk.com/photo-197700721_457240680', 'https://vk.com/photo-197700721_457240681',
                  'https://vk.com/photo-197700721_457240682', 'https://vk.com/photo-197700721_457240683',
                  'https://vk.com/photo-197700721_457240684', 'https://vk.com/photo-197700721_457240685',
                  'https://vk.com/photo-197700721_457240686', 'https://vk.com/photo-197700721_457240687',
                  'https://vk.com/photo-197700721_457240688', 'https://vk.com/photo-197700721_457240690',
                  'https://vk.com/photo-197700721_457240691', 'https://vk.com/photo-197700721_457240692',
                  'https://vk.com/photo-197700721_457240693', 'https://vk.com/photo-197700721_457240695',
                  'https://vk.com/photo-197700721_457240696', 'https://vk.com/photo-197700721_457240697',
                  'https://vk.com/photo-197700721_457240698', 'https://vk.com/photo-197700721_457240700',
                  'https://vk.com/photo-197700721_457240701', 'https://vk.com/photo-197700721_457240702',
                  'https://vk.com/photo-197700721_457240703', 'https://vk.com/photo-197700721_457240705',
                  'https://vk.com/photo-197700721_457240706', 'https://vk.com/photo-197700721_457240707',
                  'https://vk.com/photo-197700721_457240708', 'https://vk.com/photo-197700721_457240709',
                  'https://vk.com/photo-197700721_457240712', 'https://vk.com/photo-197700721_457240713']


# чтобы поставить лайк на фото, необходимо в командную строку написать "Like" (регистр неважен)
# чтобы пропустить фото, необходимо командную строку написать "Skip" (также в любом регистре)


def get_likes_command(answer_test):
    ans_pol = answer_test
    if ans_pol == "like":
        api.likes.add(type="photo", owner_id=8197666, access_token=access_token)
        print("Фото добавлено в понравившиеся")
    elif ans_pol == "skip":
        pass
    else:
        print("Неверная команда")


for page_url_n in mem_photo_link:
    likers = api.likes.getList(type="photo", owner_id=8197666, access_token=access_token, filter="likes",
                               page_url=page_url_n)
    # onwer_id - ID standlone приложения
    like_json = likers.json()
    ans_1 = like_json["likes"]
    author = api.wall.checkCopyrightLink(link=page_url_n)
    ans_2 = author.json()
    print(ans_1, ans_2)
    answer_test = input('Ведите команду:').lower()
    get_likes_command(answer_test)


def get_likes_command():
    ans_pol = input().lower()
    if ans_pol == "like":
        api.likes.add(type="photo", owner_id=8197666, access_token=access_token)
        print("Фото добавлено в понравившиеся")
    elif ans_pol == "skip":
        pass
    else:
        print("Неверная команда")


# t = r["response"][0]["items"][0]["id"]