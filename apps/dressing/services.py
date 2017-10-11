from stackapi import StackAPI
import pprint
SITE = StackAPI('stackoverflow')
SITE.max_pages = 1
SITE.page_size = 10

def get_stacked(lst):
    query = ''
    for i in range(0, len(lst)):
        if i == len(lst):
            query += lst[i]
        else:
            query += lst[i] + ';'
    questions = SITE.fetch('questions', sort='votes', tagged=query)
    titles_and_links = []
    for item in questions['items']:
        titles_and_links.append({
            'title': item['title'],
            'link': item['link']
        })
    pprint.pprint(titles_and_links)
    return titles_and_links