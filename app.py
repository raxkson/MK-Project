import DIL
import pandas


def main():
    datas = pandas.read_csv('../data/test_100.csv')
    # Suppression 삭제
    # Suppression 01 삭제 ex) 모든행 삭제
    # DIL.suppression.Suppression(datas).general(["이름"])
    # Suppression 02 부분 삭제 ex) 임리은 => 임은
    # DIL.suppression.Suppression(datas).partial("이름", [1,1])
    # Suppression 03 부분 데이터 삭제 ex) 2~3행 삭제
    # DIL.suppression.Suppression(datas).record(0)
    # Suppression 04 부분 데이터 삭제 ex) 2~3열 이름 항목 삭제
    # DIL.suppression.Suppression(datas).local("이름",[1,2])
    # Suppression 주소 삭제 ex) 광주광역시 동구 소태동 -> 광주광역시
    # DIL.suppression.Suppression(datas).address("주소", 1)
    # Suppression 05 마스킹 ex) 임*은
    # DIL.suppression.Suppression(datas).masking("이름", [1,2])
    # Aggregation 부분 총계
    DIL.statistics.aggregation.Aggregation(datas).max("생일")
    # DIL.statistics.aggregation.Aggregation(datas).min()
    # DIL.statistics.aggregation.Aggregation(datas).mode()
    # DIL.statistics.aggregation.Aggregation(datas).mean()
    # DIL.statistics.aggregation.Aggregation(datas).median()
    print(datas.head())


if __name__ == "__main__":
    main()
