from icrawler.builtin import GoogleImageCrawler
import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description='CNN implemented with Keras')
    parser.add_argument('--key', dest='key', type=str)
    parser.add_argument('--dir', dest='dir', type=str)
    parser.add_argument("--N", dest="N", type=int)
    args = parser.parse_args()
    return args


args = arg_parse()

crawler = GoogleImageCrawler(storage={"root_dir": args.dir})
crawler.crawl(keyword=args.key, max_num=args.N)