#| 
   Ønsker å finne ut hvilken grupperom skal jeg gå til, når jeg vet hvem er min læringsassistent.
   TA - kan være en entitet
   * group-responsibility :: String ("Gr1, Gr2, ...") //
   * name :: String
   GroupWork:
   * TA
   * room-id :: String
   
   group-responsibility ikke nødvendig for å løse problemet, slik den er formulert
   
|#

# Lager en ny type TA (Teaching Assistant)
data TA: teach-assist(gr-resp :: String, name :: String) end

# Lager en ny type GroupWork
data GroupWork: gw(ta :: TA, room-id :: String) end

# Lager mock-data for testing
ta1 = teach-assist("Gr1, Gr2", "Tom") # objekt av type TA
ta2 = teach-assist("Gr3, Gr4", "Ane") # objekt av type TA

group-work-1 = gw(ta1, "F1 022")
group-work-2 = gw(ta2, "F1 023")

# Forslag å bruke en type List<GroupWork)
gw-list = [list: group-work-1, group-work-2]

# INPUT: navn av TA; group-work-list, - velger også å ha data om relasjon mellom 
# TA og rom-id som input
# OUTPUT: room-id
fun get-room-nr(ta-name :: String, group-work-list :: List<GroupWork>) -> String:
  doc: "Tar navn til læringsassistent og en liste av koblinger mellom læringsassistent og rom-id som INPUT og returnerer relevant rom-id som OUTPUT"
  cases (List) group-work-list:
    | empty => raise("kan ikke prosessere tom liste")
    | link(f, r) => 
      # f er et element av type GroupWork, så f.room-id vil returnere rom-id
      # Sjekker om navn til TA er like navn fra group-work liste
      # og returnerer room-id fra instansen av GroupWork
      if f.ta.name == ta-name:
        f.room-id
      else:
        get-room-nr(ta-name, r)
      end
  end
where:
  get-room-nr("Tom", gw-list) is "F1 022"
  get-room-nr("Ane", gw-list) is "F1 023"
  get-room-nr("Roy", gw-list) raises "kan ikke prosessere tom liste"
  get-room-nr("Tom", empty) raises "kan ikke prosessere tom liste"
end
