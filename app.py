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

    # Aggregation 총계
    # Aggregation 06 총계처리 최대, 최소, 최빈, 중간
    # DIL.statistics.aggregation.Aggregation(datas).max("회원번호")
    # DIL.statistics.aggregation.Aggregation(datas).min("회원번호")
    # DIL.statistics.aggregation.Aggregation(datas).mode("회원번호")
    # DIL.statistics.aggregation.Aggregation(datas).mean("회원번호")
    # DIL.statistics.aggregation.Aggregation(datas).median("회원번호")
    # Aggregation 07 부분 총계 특정 행의 최대, 최소, 최빈, 중간
    # DIL.statistics.microAggregation.MicroAggregation(datas).max("회원번호",1)
    # DIL.statistics.microAggregation.MicroAggregation(datas).min("회원번호",1)
    # DIL.statistics.microAggregation.MicroAggregation(datas).mode("회원번호",1)
    # DIL.statistics.microAggregation.MicroAggregation(datas).mean("회원번호",1)
    # DIL.statistics.microAggregation.MicroAggregation(datas).median("회원번호",1)

    # Rounding 라운딩 올림, 내림, 반올림
    # Rounding 라운딩 08 올림, 내림, 반올림
    # DIL.rounding.Rounding(datas).up("회원번호", 1)
    # DIL.rounding.Rounding(datas).down("회원번호", 1)
    # DIL.rounding.Rounding(datas).off("회원번호", 1)
    # Rounding 랜덤 라운딩 09 올림, 내림, 반올림
    # DIL.rounding.Rounding(datas).random("회원번호", 2)
    # Rounding 제어 라운딩 10
    # 라운딩 기술 적용 시 해당 속성 값의 데이터 합계나 평균이 변하는 문제를 해결하기 위하여 원본과 합계, 평균이 일치하도록 라운딩 하는 기술
    # * 구현이 어렵고 복잡한 통계표의 적용이 어려워 실무에선 잘 사용하지 않음

    # 상하단코딩 11
    # 정규분포의 특성을 가진 속성 데이터에서 양쪽 끝에 치우친 정보가 식별성을 가질 수 있어, 이를 해결하기 위해 적은 수의 분포를 가진 양 끝단의 정보를 비식별화 기술을 적용하여 식별성을 낮추는 기법


    # Generalization 12 로컬 일반화
    # Generalization  14 숫자 데이터 범주화
    # DIL.generalization.Generalization(datas).local("회원번호",[1,100])
    # Generalization 15 문자 데이터 범주화
    # DIL.generalization.Generalization(datas).categorizion("주소", ["광주광역시 동구 소태동"], "도시")

    # 16 일방향/양방향 암호화
    # key = "testcode"
    # DIL.crypto.AES256(datas, key).encrypt("이름")
    print(datas.head())


if __name__ == "__main__":
    main()
