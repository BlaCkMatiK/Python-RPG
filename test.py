import curses

def print_menu(stdscr, selected_row_idx, options):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    for idx, option in enumerate(options):
        x = w // 2 - len(option) // 2
        y = h // 2 - len(options) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, option)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_idx = 0
    options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

    print_menu(stdscr, current_row_idx, options)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(options)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, "You selected '{}'".format(options[current_row_idx]))
            stdscr.refresh()
            stdscr.getch()
            break

        print_menu(stdscr, current_row_idx, options)

curses.wrapper(main)
