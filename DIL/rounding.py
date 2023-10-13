import pandas, random

from util import DataSetting

DataFrame = pandas.DataFrame


class Rounding(DataSetting):
    """
    라운딩 기술(일반 라운딩, 랜덤 라운딩)을 구현한 클래스

    Args:
        datas (pandas.DataFrame) : 삭제 기술을 적용할 DataFrame 지정
    """
    def __intCheck(self, datas):
        """
        기술 적용하고자 하는 DataFrame이 'int64 타입'으로 되어있는지 확인하는 함수

        Args:
            datas (pandas.DataFrame) : int64 타입 검사를 진행할 DataFrame

        Returns:
            bool : int64 타입이면 True 리턴, int64 타입이 아니면 False 리턴
        """
        if datas.dtype == "int64":
            return True
        return False

    def off(self, column: str, seatNum: int):
        """
        라운딩 기술 중 반올림을 수행하는 메소드

        Args:
            column (str) : 반올림을 적용할 컬럼
            seatNum (int) : 반올림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns:
            bool : 기술 적용 성공 시 True 리턴
        """
        datas = self.datas[column]

        intFlag = False
        if self.__intCheck(datas):
            datas = datas.astype("str")
            intFlag = True

        result = list()
        for data in datas:
            data = list(str(data))
            if int(data[-seatNum]) >= 5:
                data[-seatNum - 1] = str(int(data[-seatNum - 1]) + 1)
                data[-seatNum:] = "0" * len(data[-seatNum:])
            else:
                data[-seatNum:] = "0" * len(data[-seatNum:])

            result.append("".join(data))

        if intFlag:
            result = list(map(int, result))

        self.datas[column] = result

        return True

    def up(self, column: str, seatNum: int):
        """
        라운딩 기술 중 올림을 수행하는 메소드

        Args:
            column (str) : 올림을 적용할 컬럼
            seatNum (int) : 올림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns:
            bool : 기술 적용 성공 시 True 리턴
        """
        datas = self.datas[column]

        intFlag = False
        if self.__intCheck(datas):
            datas = datas.astype("str")
            intFlag = True

        result = list()
        for data in datas:
            data = list(data)
            if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
                data[-seatNum - 1] = str(int(data[-seatNum - 1]) + 1)
                data[-seatNum:] = "0" * len(data[-seatNum:])

            result.append("".join(data))

        if intFlag:
            result = list(map(int, result))

        self.datas[column] = result

        return True

    def down(self, column: str, seatNum: int):
        """
        라운딩 기술 중 내림을 수행하는 메소드

        Args:
            column (str) : 내림을 수행할 숫자형 타입 데이터
            seatNum (int) : 내림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns:
            int : 내림이 적용된 숫자형 타입 데이터를 리턴
        """
        datas = self.datas[column]

        intFlag = False
        if self.__intCheck(datas):
            datas = datas.astype("str")
            intFlag = True

        result = list()
        for data in datas:
            data = list(str(data))
            if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
                data[-seatNum:] = "0" * len(data[-seatNum:])

            result.append("".join(data))

        if intFlag:
            result = list(map(int, result))

        self.datas[column] = result

        return True

    @staticmethod
    def partial_up(data: int, seatNum: int):
        """
        라운딩 기술 중 올림을 수행하여 값을 반환해주는 메소드

        Args:
            data (int) : 올림을 수행할 숫자형 타입 데이터
            seatNum (int) : 올림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns:
            int : 올림이 적용된 숫자형 타입 데이터를 리턴
        """
        data = list(str(data))
        if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
            data[-seatNum - 1] = str(int(data[-seatNum - 1]) + 1)
            data[-seatNum:] = "0" * len(data[-seatNum:])

        return int("".join(data))

    @staticmethod
    def partial_down(data: int, seatNum: int):
        """
        라운딩 기술 중 내림을 수행하여 값을 반환해주는 메소드

        Args:
            data (int) : 내림을 수행할 숫자형 타입 데이터
            seatNum (int) : 내림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns:
            int : 내림이 적용된 숫자형 타입 데이터를 리턴
        """
        data = list(str(data))
        if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
            data[-seatNum:] = "0" * len(data[-seatNum:])

        return int("".join(data))
    def random(self, column: str, seatNum: int):
        """
        라운딩 기술 중 무작위로 수행하는 메소드

        Args:
            column (str) : 내림을 수행할 숫자형 타입 데이터
            seatNum (int) : 무작위로 수행할 숫자형 타입 데이터의 자리수 위치

        Returns:
            bool : 기술 적용 성공 시 True 리턴
        """
        datas = self.datas.loc[:, column]

        result = []
        for data in datas:
            func = random.choice([Rounding.partial_up, Rounding.partial_down])
            result.append(func(data=data, seatNum=seatNum))

        self.datas.loc[:, column] = result

        return True
