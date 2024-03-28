import instaloader


last_post_count = open("python.txt")
last_post_count_read = int(last_post_count.read())

L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, "filistinicin1000genc")


how_many_post_there = profile.get_posts().count - last_post_count_read
x = how_many_post_there

if how_many_post_there > 0:

    for post in profile.get_posts():

        if post.is_pinned:
            continue
        else:
            print(str(post.date))
            L.download_post(post, target=str(post.date))
            x = x - 1
            if x == 0:
                break

    a = open("python.txt", "w")
    a.close()

    f = open("python.txt", "a")
    f.write(str(int(last_post_count_read) + 1))


