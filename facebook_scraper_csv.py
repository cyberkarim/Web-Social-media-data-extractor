import csv
from facebook_scraper import get_posts

def main(account, num):
        file_csv = open('Results/facebook_data.csv', 'w', newline='')
        writer = csv.writer(file_csv)
        writer.writerow( [ "post_id", "post_url", "user_id", "time", "text", "link", "images", "video", "likes", "comments", "shares" ] )
        for post in get_posts(account, pages=num):
                pt = post["text"].replace('\n', ' ')
                for c in post["text"]:
                        if(c<chr(0) or c>chr(127)):
                                pt = pt.replace(c, ' ')
                writer.writerow( [ post["post_id"], post["post_url"], post["user_id"], post["time"], pt, post["link"], post["images"], post["video"], post["likes"], post["comments"], post["shares"] ] )

#main('WHO', 2)
