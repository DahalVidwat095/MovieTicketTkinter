from Ticket_Management_System import *
def test_Namesp():
     ab= show_database_result("Birasat","Dahal")
     assert ab=="Pass"


def test_Namesf():
    pq = show_database_result("Vidwat", "Sapkota")
    assert pq == "Pass"

def test_Gender_Addressp():
    rs = show_database_result1("Male", "Balkot")
    assert rs == "Pass"

def test_Gender_Addressf():
    dt = show_database_result("Others", "Bhaktapur")
    assert dt == "Pass"

def test_Phone_Emailp():
        vu = show_database_result("9844242403", "dahalv@gmail.com")
        assert vu == "Pass"
