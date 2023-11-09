from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("file")
    parser.add_argument(
        "-c", "--column", type=int, required=True, help="unicode column index"
    )
    args = parser.parse_args()

    code_index = args.index

    chars = []
    with open(args.file, "r") as f:
        for row in f:
            if row[0] == "#":
                continue
            code = row.split("\t")[code_index]
            c = chr(int(code, 16))
            if c.isprintable():
                chars.append(c)

    print("\n".join(chars))


if __name__ == "__main__":
    main()
