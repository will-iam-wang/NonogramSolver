from selenium import webdriver
from bs4 import BeautifulSoup
import sys


def crawl_color_panel(soup: BeautifulSoup) -> dict:
    color_panel_ele = soup.find('table', {'class': 'nonogram_color_table'})
    colors = color_panel_ele.findAll('td')
    ans = {'#ffffff': 0}  # initial with the white color
    for i, color in enumerate(colors, start=1):
        ans[color['style'].split(';')[0].split(':')[1]] = i
    return ans


def crawl_row_groups(soup: BeautifulSoup, color_panel: dict) -> list:
    rows_ele = soup.find('td', {'class': 'nmtl'}).findAll('tr')
    row_groups = []
    for row in rows_ele:
        cur_row = []
        for cell in row.findAll('td'):
            if not cell.has_attr('style'):
                continue
            cell_color = cell['style'].split(';')[0].split(':')[1]
            cur_row.append((int(cell.text), color_panel[cell_color]))
        row_groups.append(cur_row)
    return row_groups


def crawl_col_groups(soup: BeautifulSoup, color_panel: dict) -> list:
    cols_ele = soup.find('td', {'class': 'nmtt'}).findAll('tr')
    temp = []
    for row in cols_ele:
        cur_row = []
        for cell in row.findAll('td'):
            if not cell.has_attr('style'):
                cur_row.append((-1, 0))
            else:
                cell_color = cell['style'].split(';')[0].split(':')[1]
                cur_row.append((int(cell.text), color_panel[cell_color]))
        temp.append(cur_row)
    return [[(i, j) for i, j in col if i * j != 0] for col in zip(*temp)]


def main():
    # Testing without browser
    argv = sys.argv
    puzzle_id = argv[1]

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(options=op)
    black_white_puzzle_url = 'https://www.nonograms.org/nonograms/i/'
    # driver.get(f'https://www.nonograms.org/nonograms2/i/{puzzle_id}')

    driver.get(black_white_puzzle_url + puzzle_id)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # color_panel = crawl_color_panel(soup)
    color_panel = 
    row_groups = crawl_row_groups(soup, color_panel)
    col_groups = crawl_col_groups(soup, color_panel)
    m, n = len(row_groups), len(col_groups)  # size of the puzzle
    with open(f'./puzzle/{puzzle_id}.txt', 'w') as f:
        for k in color_panel:
            f.write(f'{k}\n')
        f.write(f'-\n')

        for row_group in row_groups:
            for x, y in row_group:
                f.write(f'{x}:{y},')
            f.write('\n')

        f.write('-\n')

        for col_group in col_groups:
            for x, y in col_group:
                f.write(f'{x}:{y},')
            f.write('\n')


if __name__ == '__main__':
    main()
