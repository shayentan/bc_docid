# http://192.168.20.24:9001/web_services/CategorySearch_universal_iro.php?
# catid=0&city=mumbai&area=MALAD&start=1&end=7&random1=0.66587&random2=0.98364&random3=0.89281&wap_flag=0&
# nearme_flag=0&
# nearme_latitude=0&nearme_longitude=0&search_option=0&catname_search=&json=1&sort_order=0&bd_flag
# =1&national_catid=10993991&catname=Refrigerator%20Repair%20&%20Services-Samsung
import pytest
import requests
import csv


def read_data_from_csv():
    test_data_zip_from_csv = []
    with open("Testdata/bc_doc_id.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        for row in data:
            test_data_zip_from_csv.append(row)
    return test_data_zip_from_csv


@pytest.mark.parametrize("doc_id,expected_response", read_data_from_csv())
def test_bc_doc_id_match_with_doc_id(
        doc_id, expected_response
):
    response = requests.get(
        f"http://192.168.8.227:700/mvc/services/company/getcards?docid={doc_id}")
    response_body = response.json()
    # bc = response_body["results"]["data"]["bc_docid"]
    # display_product = display_product_raw
    if response_body["results"]["data"]["bc_docid"] == expected_response:
        # print(response_body)
        assert True
    else:
        print(response_body)
        assert False

