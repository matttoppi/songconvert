from search_net import google_scrape


def validate_new_url(convert_plat, newURL, origSong_obj):
    validity_score = 100

    glink_title = google_scrape(newURL)
    print(glink_title)

    if origSong_obj.name.split('.')[0] not in glink_title:
        # print("bad name\n")
        validity_score -= 10
    if origSong_obj.artist not in glink_title:
        # print("bad artist\n")
        validity_score -= 10
    if convert_plat not in newURL:
        # print("bad plat\n")
        validity_score -= 100

    print(f"Validity Score: {validity_score}")

    if validity_score > 79:
        return True
    else:
        return False
