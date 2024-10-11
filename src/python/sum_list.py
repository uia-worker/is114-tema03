import time
import sys
"""

For å kunne utføre testing må du installere pytest module.
Gå til Verktøy->Administrere pakker ... og søk etter pytest.
Klikke på lenken pytest og på knappen Installer.
Tester må skrives i en funksjon som begynner med "test_".
I Shell (vanligvis under definisjonsvinduet, dvs. dette vinduet) skriv
>>> !pytest sum_list.py

OBS! ">>>" er strengen som representerer promt og er ikke en del av kommandoen

"""

def sum_list(numlist : list[int]) -> int:
    """summer en liste med tall"""
    total = 0
    for num in numlist:
        total = total + num
    return total

def sum_list_rec(numlist : list[int], total : int = 0) -> int:
    if len(numlist) != 0:
        first = numlist[0]
        del numlist[0]
        total = first + sum_list_rec(numlist, total)
    return total

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list_iter([1, 2, 3]) == 6
    assert sum_list_iter([-1, 2, 3]) == 4
    
sys.setrecursionlimit(1999)
start_time = time.time()
sum_list_rec(list(range(0,1600)))
end_time = time.time()
elapsed = end_time - start_time
elapsed_sc_not = "{:e}".format(elapsed)
print("Tiden for rekursiv version er:", elapsed_sc_not, "sekunder")
start_time = time.time()
sum_list(list(range(0,1600)))
end_time = time.time()
print("Tiden for iterasjonsversjon er:", end_time - start_time, "sekunder")
