#!/usr/bin/env python

import argparse
import getpass

SITE_LIST=[
    'bash.org.ru',
    'bash.org.ua',
    'bebo.com',
    'blip.com',
    'break.com',
    'delicious.com',
    'digg.com',
    'facebook.com',
    'fb.com'
    'flickr.com',
    'forums.somethingawful.com',
    'friendster.com',
    'habrahabr.ru',
    'hi5.com',
    'infoq.com',
    'korrespondent.net',
    'lenta.ru',
    'linkedin.com',
    'livejournal.com',
    'meetup.com',
    'myspace.com',
    'news.ycombinator.com',
    'newsru.com',
    'plurk.com',
    'reddit.com',
    'slashdot.com',
    'somethingawful.com',
    'stickam.com',
    'stumbleupon.com',
    'twitter.com',
    'vimeo.com',
    'vk.com', 'vkontakte.ru',
    'yelp.com',
    'youtube.com',
]

HOST_FILE = '/etc/hosts';
START_TOKEN = '## start-gsd';
END_TOKEN = '## end-gsd';


class ModeAction(argparse.Action):
    def __call__(self, parser, namespace, values=None, option_string=None):
        if getpass.getuser() != 'root':
            raise Exception('Script should be executed as the root')
        if values == 'work':
            f = open(HOST_FILE, 'r')
            content = f.read()
            f.close()
            if START_TOKEN in content and END_TOKEN in content:
                raise Exception('Work mode already set')
            elif START_TOKEN in content or END_TOKEN in content:
                raise Exception('Smth goes wrong - 1 token is in file, but second - not')
            else:
                f = open(HOST_FILE, 'w')
                new_content = []
                new_content.append(START_TOKEN+'\n')
                for site in SITE_LIST:
                    new_content.append("127.0.0.1\t%s\n" % site)
                    new_content.append("127.0.0.1\twww.%s\n" % site)
                new_content.append(END_TOKEN+'\n')
                f.write(content+"".join(new_content))

        elif values == 'play':
            f = open(HOST_FILE, 'r')
            content = f.read()
            f.close()
            if not START_TOKEN in content and not END_TOKEN in content:
                raise Exception('Play mode already set')
            elif START_TOKEN in content and END_TOKEN in content:
                f = open(HOST_FILE, 'r')
                lines = f.readlines()
                f.close()
                f = open(HOST_FILE, 'w')
                inside_token = False
                new_content = []
                for line in lines:
                    if START_TOKEN in line:
                        inside_token = True
                    if not inside_token:
                        new_content.append(line)
                    if END_TOKEN in line:
                        inside_token = False
                f.write("".join(new_content))
            elif START_TOKEN in content or END_TOKEN in content:
                raise Exception('Smth goes wrong - 1 token is in file, but second - not')

def main():

    parser = argparse.ArgumentParser(description='Get shit done.')
    parser.add_argument('-m, --mode', action=ModeAction,
                        choices=['work', 'play'],
                        help='switch to mode')

    args = parser.parse_args()

if __name__ == "__main__":
    main()
