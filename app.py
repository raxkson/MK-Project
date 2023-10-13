import pandas
# from DIL import Suppression
# from DIL import

import DIL


def main():
    datas = pandas.read_csv('../data/test_100.csv')
    # Suppression 삭제
    # DIL.suppression.Suppression(datas).general(["이름"])
    # Suppression 부분 삭제
    # DIL.suppression.Suppression(datas).local("이름",[1,2])
    # Suppression 마스킹 ex) 임*은
    # DIL.suppression.Suppression(datas).masking("이름", [1,2])
    print(datas.head())


if __name__ == "__main__":
    main()
