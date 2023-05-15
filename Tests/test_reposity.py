import unittest
from Src.Services.Repo import repo

from Src.Models.Building  import building
from Src.Models.Contractor import contractor
from Src.Models.Executor import executor
from Src.Models.Act import act

#
# Набор модульных тестов для проверки Reposity
#
class reposity_tests(unittest.TestCase):


    # Проверить получение актов
    def test_get_acts(self):
        # Подготовка
        _repo = repo.create(is_demo=True)
        

        # Действие
        result = _repo.get_acts()

        # Проверки
        assert len(result) > 0





if __name__ == '__main__':
    unittest.main()



