from datetime import datetime
from Src.Models.Period import period
from Src.Models.Building import building
from Src.Models.Executor import executor
from Src.Models.Contractor import contractor
from Src.Models.Act import act

import unittest
import json

#
# Набор модульных для проверки конвертиции структур в Json
#
class json_convert_tests(unittest.TestCase):

    #
    # Проверить конвертацию в Json объекта типа period
    #
    def test_period_to_json(self):
        # Подготовка
        test_period = datetime(2020,1,1)
        object = period(test_period)

        # Действие
        result = object.toJSON()

        # Проверки
        assert result is not None
        assert result == "2020-01-01 00:00:00"

    #
    # Проверить конвертацию в Json объекта типа builder
    #
    def test_building_to_json(self):
        # Подготовка
        object = building.create("test")
        
        # Действие
        result = object.toJSON()

        # Проверки
        assert result is not None
        act = json.loads(result)
        assert act is not None
        print(result)
        print(act)

    #
    # Проверить конвертицию в Json объекта типа executor
    #
    def test_executor_to_json(self):
        # Подготовка
        parent = contractor.create(name="test", parent=None)
        object = executor.create(name="test", _contractor=parent)

        # Действие
        result = object.toJSON()

        # Проверки
        assert result is not None
        act = json.loads(result)
        assert act is not None
        print(result)
        print(act)

    #
    # Проверить конвертацию в Json объекта типа contractor
    #
    def test_contractor_to_json(self):
        # Подготовка
        _parent = contractor.create(name="test", parent=None)
        object = contractor.create(name="test", parent=_parent)

        # Действие
        result = object.toJSON()

         # Проверки
        assert result is not None
        act = json.loads(result)
        assert act is not None
        print(result)
        print(act)


    #
    # Порверить конвертацию в Json объекта типа act
    #
    def test_act_to_json(self):
        # Подготовка
        contractor_parent = contractor.create(name="test1", parent=None)
        contractor_act = contractor.create(name="test2", parent=contractor_parent)
        executor_act = executor.create(name="test3", _contractor=contractor_act)
        building_act = building.create(name="test4")
        object = act.create(_executor=executor_act, _building=building_act)


        # Действие
        result = object.toJSON()

         # Проверки
        assert result is not None
        restore = json.loads(result)
        assert restore is not None

        print(result)
        print(restore)


if __name__ == '__main__':
    unittest.main()
