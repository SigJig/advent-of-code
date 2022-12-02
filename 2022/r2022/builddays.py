
def main():
    for i in range(3, 26):
        with open(f'./src/days/day_{i}.rs', 'w') as fp ,\
            open(f'./input/day_{i}.txt', 'w') as _:
            fp.write('\n\npub fn run() {\n\n}')

if __name__ == '__main__':
    main()
