#!/usr/bin/env python3 


from pytube import YouTube

def download():
    link = input('Enter your link:')
    y = YouTube(link)

    try:
        print('Title=>',y.title)
        print('Views=>',y.views)
        print('rating=>',y.rating)
        dv = y.streams.get_highest_resolution()
        print('Downloading...')
        dv.download()


    except:
        print("[!] Connection Error")

    print('Task Completed!')

if __name__=='__main__':
    download()
