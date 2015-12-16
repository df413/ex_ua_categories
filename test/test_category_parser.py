import unittest
from utils.csvReader import CSVReader
from parser.exUaParser import CategoryParser


class MyTestCase(unittest.TestCase):
    def test_parsing_content(self):

        html_file = open("sampleData/test_category_data.html", "rb")
        csv_data_file = open("expected_category_data", "rb")

        csv_reader = CSVReader(file_obj=csv_data_file)
        category_parser = CategoryParser(html_file)
        i = 0

        for name, link in csv_reader.dataGenerator():
            self.assertEqual(name.decode('utf-8'), category_parser.items[i]['name'])
            i += 1
        html_file.close()
        csv_data_file.close()

if __name__ == '__main__':
    unittest.main()
