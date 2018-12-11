import pytumblr
import requests
import bs4
from tqdm import tqdm
import os
import sys
import time
import datetime
import config

def record_error_log(post_type,post_url):
    now = str(datetime.datetime.now())
    msg = '{} type:{} failed : {}'.format(now,post_type,post_url)
    print(msg)
    with open('error_log.txt', 'a') as f:
        f.write(msg+'\n')

def download_photo(post,save_path,sleep_time):
    
    save_path += '/photo'
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    try:
        photos = post['photos']
        for photo in photos:
            time.sleep(sleep_time)
            photo_orizinal_url = photo['original_size']['url']
            file_name = photo_orizinal_url.split('/')[-1]
            
            file_path = save_path + '/' + file_name
            r = requests.get(photo_orizinal_url, stream=True)
            if r.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(r.content)
    except:
        record_error_log('photo',post['post_url'])

def download_video(post,save_path,sleep_time):

    save_path += '/video'
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    try:
        time.sleep(sleep_time)
        video_url = post['video_url']
        file_name = video_url.split('/')[-1]
        file_path = save_path + '/' + file_name
        r = requests.get(video_url, stream=True)
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(r.content)
    except:
        record_error_log('video',post['post_url'])

def download_text(post,save_path,sleep_time):

    save_path += '/text_type'
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    try:
        time.sleep(sleep_time)
        text_body = post['body']
        bs_obj = bs4.BeautifulSoup(text_body,"html.parser")
        source_url = bs_obj.source['src']
        file_name = source_url.split('/')[-1]
        file_path = save_path + '/' + file_name
        r = requests.get(source_url, stream=True)
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(r.content)
    except:
        record_error_log('text',post['post_url'])

def receive_number_int_value(msg):
    while 1:
        input_num = input(msg)
        try:
            input_num = int(input_num)
        except:
            print('type it again')
            continue

        if input_num >= 0:
            break
        else:
            print('type it again')

    return input_num

def receive_number_float_value(msg):
    while 1:
        input_num = input(msg)
        try:
            input_num = float(input_num)
        except:
            print('type it again')
            continue

        if input_num >= 0:
            break
        else:
            print('type it again')

    return input_num

def input_setting_value(query_num):

    print("number of requests required :",query_num)

    start_request = receive_number_int_value('offset (request) : ')
    request_num = receive_number_int_value('number of requests  : ')
    sleep_time = receive_number_float_value('interval of download [s] : ')

    if start_request + request_num > query_num:
        request_num = query_num - start_request
    
    while 1:
        s = input('start downloading? (y/n) : ')
        if s == 'y':
            break
        elif s == 'n':
            break 
    if s == 'n':
        exit()
    
    return start_request,request_num,sleep_time

def make_save_directory(save_path):
    if not os.path.exists('download'):
        os.mkdir('download') 
    
    if not os.path.exists(save_path):
        os.mkdir(save_path)

def get_blog_media(client,blog_name):
    
    blog_info = client.blog_info(blog_name)
    
    if blog_info.get('meta'):
        print(blog_info['meta']['msg'])
        exit()
        
    post_num = blog_info['blog']['posts']
    query_num = int(post_num / 50) + 1
    
    start_request,request_num,sleep_time = input_setting_value(query_num)

    save_path = 'download/'+blog_name
    make_save_directory(save_path)

    for i in range(start_request,start_request+request_num):
        sys.stdout.write('\r{}{}/{} \n'.format('request : ',i+1,query_num))
        sys.stdout.flush()

        blog_posts = client.posts(blog_name, limit = 50, offset = i * 50)['posts']

        for post in tqdm(blog_posts):
            if post['type'] == 'photo':
                download_photo(post,save_path,sleep_time)
            elif post['type'] == 'video':
                download_video(post,save_path,sleep_time)
            elif post['type'] == 'text':
                download_text(post,save_path,sleep_time)
            
    print('Finish!')

def get_my_likes(client):

    my_info = client.info()
    
    likes_num = my_info['user']['likes']
    query_num = int(likes_num / 50) + 1

    start_request,request_num,sleep_time= input_setting_value(query_num)

    save_path = 'download/my_likes'
    make_save_directory(save_path)
        
    for i in range(start_request,start_request+request_num):
        sys.stdout.write('\r{}{}/{} \n'.format('request : ',i+1,query_num))
        sys.stdout.flush()

        like_posts = client.likes(limit = 50, offset = i * 50)['liked_posts']
        
        for post in tqdm(like_posts):
            if post['type'] == 'photo':
                download_photo(post,save_path,sleep_time)
            elif post['type'] == 'video':
                download_video(post,save_path,sleep_time)
            elif post['type'] == 'text':
                download_text(post,save_path,sleep_time)

    print('Finish!')

def main():
    client = pytumblr.TumblrRestClient(
        config.consumer_key,
        config.consumer_secret,
        config.oauth_token,
        config.oauth_secret
    )

    while 1:
        mode = input('select mode (0:get post / 1:get my likes) : ')
        try:
            mode = int(mode)
        except:
            print('type it again')
            continue

        if mode == 0 or mode == 1:
            break
        else:
            print('type it again')

    if mode == 0:
        blog_name = input('blog name : ')
        get_blog_media(client,blog_name)
    else:
        get_my_likes(client)

if __name__ == "__main__":
    main()