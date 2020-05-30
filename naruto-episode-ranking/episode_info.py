"""
Extract review, episode number and title from IMDb for every episode, using the Beautiful Soup
and requests packages.
"""


from bs4 import BeautifulSoup as bs
import requests


def get_ep_info(base_url):
    """
    Takes in a base URL, goes through every year, gets all episodes for each year and then gets
    the individual reviews, title and episode number.

    All this information is returned in a dictionary which has keys of episode numbers.
    """
    show_info = dict()
    year_urls = [base_url + str(i) for i in range(2009, 2018)]

    for year in year_urls:
        src = requests.get(year).content
        soup_obj = bs(src, 'lxml')

        # The main HTML structure we need to refer to
        structure = soup_obj.find('div', class_='list detail eplist')

        # Contains the HTMl structure where the episode titles and reviews
        # are contained
        branch_1 = structure.findAll('div', class_='info')
        titles = [ep.find('strong').getText() for ep in branch_1]
        reviews = [float(ep.find('span', class_='ipl-rating-star__rating').getText()) for ep in branch_1]

        # Contains the HTML structure where the episode numbers are contained
        branch_2 = structure.findAll('div', class_='hover-over-image zero-z-index')
        # Extracts the season and episode numbers, from the div
        numbers = [branch_2[i].find('div').getText() for i in range(len(branch_2))]

        # We ONLY want the episode numbers, since the season number is the same
        # for the whole series. So we need to separate the two, remove whitespace and only
        # get the numbers

        # This handles a special case for 2014, where there was an OVA included, which we
        # don't need
        if '2014' in year:
            numbers = [int(numbers[i].split(',')[1].strip()[2:]) for i in range(len(numbers) - 1)]
        else:
            numbers = [int(numbers[i].split(',')[1].strip()[2:]) for i in range(len(numbers))]

        for num, title, review in zip(numbers, titles, reviews):
            show_info[num] = (title, review)
    return show_info


def main():
    base = 'https://www.imdb.com/title/tt0988824/episodes?year='
    info = get_ep_info(base)


if __name__ == '__main__':
    main()