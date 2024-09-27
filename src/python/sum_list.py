"""

For å kunne utføre testing må du installere pytest module.
Gå til Verktøy->Administrere pakker ... og søk etter pytest.
Klikke på lenken pytest og på knappen Installer.
Tester må skrives i en funksjon som begynner med "test_".
I Shell (vanligvis under definisjonsvinduet, dvs. dette vinduet) skriv
>>> !pytest sum_list.py

OBS! ">>>" er strengen som representerer promt og er ikke en del av kommandoen

"""

def sum_list(numlist : list) -> float:
    """summer en liste med tall"""
    total = 0
    for num in numlist:
        total = total + num
    return total

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
