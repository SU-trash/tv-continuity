#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from show_continuity import Show


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='show_name', type=str,
                        help="Title of a show. A dict of the show's seasons/episodes will be pretty-printed.")
    args = parser.parse_args()

    show = Show.from_wikipedia(title=args.show_name)

    print('seasons={')
    for season_id, season_dict in show.seasons.items():
        color = season_dict['color'] if 'color' in season_dict else '#000000'
        print(f"    {repr(season_id)}: {{'color': {repr(color)},")
        print("        'episodes': {")
        for i, (ep_id, ep_title) in enumerate(season_dict['episodes'].items()):
            if i != len(season_dict['episodes']) - 1:
                print(f"            {repr(ep_id)}: {repr(ep_title)},")
            else:
                print(f"            {repr(ep_id)}: {repr(ep_title)}}}}},")
