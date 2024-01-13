# Tests for insterview
import pdb
from collections import Counter, defaultdict

## 1.
## Below is a master list of items. Then there are 2 tests containing more lists.
## One test contains a list where all items in the list are within the master list
## The other test contains a list where not all of the items are in the master list.
## Implement the 'contains_all_items' function in 3 different ways so that the tests pass.
MASTER_LIST = ['Cat', 'Dog', 'Apple', 'Bear', 'Goat', 'Fish', 'Elephant',
               'Quokka', 'Unicorn', 'Impala', 'Walrus', 'Yak', 'Giraffe', 'Zebra', 'Narwhal',
               'Rhinceros', 'Vulture', 'Tiger', 'Kangaroo', 'Lion', 'Sloth', 'Jaguar', 'Ostrich']


def contains_all_items_1(test_list):
    for item in test_list:
        if item not in MASTER_LIST:
            return False
    return True


def contains_all_items_2(test_list):
    return set(test_list).intersection(MASTER_LIST) == set(test_list)


def contains_all_items_3(test_list):
    # this way only works for unique MASTER_LIST and test_list
    different_elements = list(set(MASTER_LIST).difference(test_list))
    return (len(MASTER_LIST) - len(different_elements)) == len(test_list)


def test_list_contains_multiple_items():
    test_list = ['Apple', 'Jaguar', 'Bear', 'Fish', 'Narwhal']
    assert contains_all_items_1(test_list) == True
    assert contains_all_items_2(test_list) == True
    assert contains_all_items_3(test_list) == True


def test_list_does_not_contains_all_items():
    test_list = ['Apple', 'Jaguar', 'Buffalo', 'Fish', 'Nightingale']
    assert contains_all_items_1(test_list) == False
    assert contains_all_items_2(test_list) == False
    assert contains_all_items_3(test_list) == False


## 2.
## Below is a master list of addresses for a customer from a database
## Implement the 'most_frequent' function to provide the top 3 most frequent addresses in 3 different ways

ADDRESS_LIST = [
    '321 Oak Street, Perth, WA',
    '334 Sunset Avenue, Darwin, NT',
    '654 Cedar Lane, Gold Coast, QLD',
    '789 Maple Drive, Brisbane, QLD',
    '789 Maple Drive, Brisbane, QLD',
    '1122 Beach Road, Cairns, QLD',
    '123 Fake Street, Sydney, NSW',
    '789 Maple Drive, Brisbane, QLD',
    '789 Maple Drive, Brisbane, QLD',
    '334 Sunset Avenue, Darwin, NT',
    '321 Oak Street, Perth, WA',
    '123 Fake Street, Sydney, NSW',
    '654 Cedar Lane, Gold Coast, QLD',
    '654 Cedar Lane, Gold Coast, QLD',
    '321 Oak Street, Perth, WA',
    '1122 Beach Road, Cairns, QLD',
    '654 Cedar Lane, Gold Coast, QLD',
    '789 Maple Drive, Brisbane, QLD',
    '1122 Beach Road, Cairns, QLD',
    '321 Oak Street, Perth, WA',
    '123 Fake Street, Sydney, NSW'
]


def most_frequent_1(data_lst):
    address_counts = Counter(data_lst)
    return [item[0] for item in address_counts.most_common(3)]


def most_frequent_2(data_lst):
    # create an counter by dict
    address_counts = {}
    for address in data_lst:
        if address not in address_counts:
            address_counts[address] = 0
        address_counts[address] += 1
    # sort counter dict by item value
    sorted_addresses_dict = sorted(address_counts.items(), key=lambda item: item[1], reverse=True)
    # return top 3 keys of sorted dict
    return [key for key, value in sorted_addresses_dict[:3]]


def most_frequent_3(data_lst):
    # create an counter by dict
    address_counts = {}
    for address in data_lst:
        if address not in address_counts:
            address_counts[address] = 0
        address_counts[address] += 1
    # format data with an structure string like: 'count - address'
    formatted_addresses_lst = []
    for address, count in address_counts.items():
        formatted_addresses_lst.append("{0}-{1}".format(count, address))
    # because all items start have count at beginning, so we can sort them
    sorted_addresses_lst = sorted(formatted_addresses_lst, reverse=True)
    # finally we split item by '-' to get address and return top 3 address
    return [item.split('-')[1] for item in sorted_addresses_lst[:3]]


def test_get_most_frequent():
    expected = ['789 Maple Drive, Brisbane, QLD', '321 Oak Street, Perth, WA', '654 Cedar Lane, Gold Coast, QLD']
    assert most_frequent_1(ADDRESS_LIST) == expected
    assert most_frequent_2(ADDRESS_LIST) == expected
    assert sorted(most_frequent_3(ADDRESS_LIST)) == sorted(expected)


## 3.
## Below is a master list of output from a database, of the jobs of a customer.
## The user needs to know the total price information, so the data needs to be transformed.
## There are 2 functions below which need completing. One transforms the information for one truck type.
## The other gives a summary of all truck types.
## Write the tests for the expected output of each function, including any parameters. Then write
## each function in 2 different ways, so the the tests beneath pass.

DB_OUTPUT = [
    {"id": 1, "date": "2022-02-15T08:24:57", "price_cents": 12775, "surcharge_cents": 1000, "tax_percent": 10,
     "truck_type": "Van"},
    {"id": 2, "date": "2022-02-10T20:46:29", "price_cents": 6414, "surcharge_cents": 300, "tax_percent": 10,
     "truck_type": "Ute"},
    {"id": 3, "date": "2022-02-12T17:30:01", "price_cents": 7146, "surcharge_cents": 300, "tax_percent": 10,
     "truck_type": "Pantech"},
    {"id": 4, "date": "2022-02-18T14:18:07", "price_cents": 3771, "surcharge_cents": 500, "tax_percent": 10,
     "truck_type": "Ute"},
    {"id": 6, "date": "2022-02-08T09:56:42", "price_cents": 11893, "surcharge_cents": 0, "tax_percent": 10,
     "truck_type": "Pantech"},
    {"id": 7, "date": "2022-02-21T06:42:52", "price_cents": 5490, "surcharge_cents": 500, "tax_percent": 10,
     "truck_type": "Van"},
    {"id": 8, "date": "2022-02-19T05:37:13", "price_cents": 4542, "surcharge_cents": 300, "tax_percent": 10,
     "truck_type": "Ute"},
    {"id": 9, "date": "2022-02-22T10:15:38", "price_cents": 6305, "surcharge_cents": 300, "tax_percent": 10,
     "truck_type": "Van"},
    {"id": 11, "date": "2022-02-06T19:24:01", "price_cents": 1684, "surcharge_cents": 500, "tax_percent": 10,
     "truck_type": "Pantech"},
    {"id": 13, "date": "2022-02-11T11:52:16", "price_cents": 7628, "surcharge_cents": 0, "tax_percent": 10,
     "truck_type": "Ute"},
    {"id": 14, "date": "2022-02-07T16:39:55", "price_cents": 3942, "surcharge_cents": 0, "tax_percent": 10,
     "truck_type": "Van"}
]


class Truck:
    def __init__(self, db_record: dict):
        self.id = None
        self.date = None
        self.price_cents = 0
        self.surcharge_cents = 0
        self.tax_percent = 0
        self.truck_type = 0

        for col, value in db_record.items():
            setattr(self, col, value)

    def get_price(self):
        return (self.price_cents + self.surcharge_cents) * (100 + self.tax_percent) / 100

    def get_truck_type(self):
        return self.truck_type

    def get_id(self):
        return self.id


def job_price_for_truck_type_1(job_list, truck_type):
    ''' Returns a list of the following structure for trucks matching "truck_type":
            { "id": <int>, "price": <int> }

            where "price" is "(price_cents + surcharge_cents) * (100 + tax_percent)/100" converted to dollars
        '''
    formatted_job_list = {}
    for job in job_list:
        truck = Truck(job)
        if truck.get_truck_type() not in formatted_job_list:
            formatted_job_list[truck.get_truck_type()] = []
        if truck.get_id():
            formatted_job_list[truck.get_truck_type()].append({
                'id': truck.get_id(),
                'price': truck.get_price()
            })
    return formatted_job_list[truck_type] if truck_type in formatted_job_list else []


def job_price_for_truck_type_2(job_list, truck_type):
    ''' Returns a list of the following structure for trucks matching "truck_type":
            { "id": <int>, "price": <int> }

            where "price" is "(price_cents + surcharge_cents) * (100 + tax_percent)/100" converted to dollars
        '''
    filtered_truck_type_list = []
    for job in job_list:
        truck = Truck(job)
        if truck.get_truck_type() == truck_type and truck.get_id():
            filtered_truck_type_list.append({
                'id': truck.get_id(),
                'price': truck.get_price()
            })
    return filtered_truck_type_list


def total_price_by_truck_1(job_list):
    ''' Returns a list of the following structures:
        { "truck_type": <truck type>, "total_jobs": <int>, "total_price": <int> }

        where "total_jobs" is the total number of jobs for the truck type
        and "total_price" is the total price for the truck type
    '''
    formatted_job_list = {}
    for job in job_list:
        truck = Truck(job)
        if truck.get_truck_type() not in formatted_job_list:
            formatted_job_list[truck.get_truck_type()] = {
                'total_jobs': 0,
                'total_price': 0,
            }
        if truck.get_id():
            formatted_job_list[truck.get_truck_type()]['total_jobs'] += 1
            formatted_job_list[truck.get_truck_type()]['total_price'] += truck.get_price()
    return [{'truck_type': key, **value} for key, value in formatted_job_list.items()]


def total_price_by_truck_2(job_list):
    result_dict = defaultdict(lambda: {"total_jobs": 0, "total_price": 0})
    for job in job_list:
        truck = Truck(job)
        truck_type = truck.get_truck_type()
        result_dict[truck_type]["total_jobs"] += 1
        result_dict[truck_type]["total_price"] += truck.get_price()
    return [{"truck_type": key, **value} for key, value in result_dict.items()]


def test_job_price_for_truck_types():
    expected_van_jobs = [{'id': 1, 'price': 15152.5}, {'id': 7, 'price': 6589.0}, {'id': 9, 'price': 7265.5},
                         {'id': 14, 'price': 4336.2}]

    assert job_price_for_truck_type_1(DB_OUTPUT, "Van") == expected_van_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Van") == expected_van_jobs

    expected_ute_jobs = [{'id': 2, 'price': 7385.4}, {'id': 4, 'price': 4698.1}, {'id': 8, 'price': 5326.2},
                         {'id': 13, 'price': 8390.8}]

    assert job_price_for_truck_type_1(DB_OUTPUT, "Ute") == expected_ute_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Ute") == expected_ute_jobs

    expected_pantech_jobs = [{'id': 3, 'price': 8190.6}, {'id': 6, 'price': 13082.3}, {'id': 11, 'price': 2402.4}]

    assert job_price_for_truck_type_1(DB_OUTPUT, "Pantech") == expected_pantech_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Pantech") == expected_pantech_jobs


def test_total_price_by_truck():
    expected_list = [
        {"truck_type": "Van", "total_jobs": 4, "total_price": 33343.2},
        {"truck_type": "Ute", "total_jobs": 4, "total_price": 25800.5},
        {"truck_type": "Pantech", "total_jobs": 3, "total_price": 23675.300000000003},
    ]

    assert total_price_by_truck_1(DB_OUTPUT) == expected_list
    assert total_price_by_truck_2(DB_OUTPUT) == expected_list
