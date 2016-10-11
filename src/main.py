import IO
import game


def main():
    args = IO.IN()

    data = ''

    try:
        with open(args.file) as file:
            data = file.read()
    except Exception:
        IO.OUT('Hmm, I cant read that file!')

    IO.OUT('Okey, lets go!')

    game.create(data, min=args.min, max=args.max)


if __name__ == '__main__':
    main()
