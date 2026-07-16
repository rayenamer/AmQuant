from __future__ import annotations
from amquant.dataDefinitions.universe import Instrument

UNIVERSE: list[Instrument] = [
    # ========================= FRENCH GROUP =========================
    Instrument(symbol="MC", yahoo_symbol="MC.PA", name="LVMH", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="TTE", yahoo_symbol="TTE.PA", name="TotalEnergies", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="SAN", yahoo_symbol="SAN.PA", name="Sanofi", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="OR", yahoo_symbol="OR.PA", name="L'Oreal", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="AIR", yahoo_symbol="AIR.PA", name="Airbus", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="BNP", yahoo_symbol="BNP.PA", name="BNP Paribas", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="AI", yahoo_symbol="AI.PA", name="Air Liquide", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="SU", yahoo_symbol="SU.PA", name="Schneider Electric", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="BN", yahoo_symbol="BN.PA", name="Danone", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="ML", yahoo_symbol="ML.PA", name="Michelin", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="RMS", yahoo_symbol="RMS.PA", name="Hermes International", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="ACCP", yahoo_symbol="AC.PA", name="Accor", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="CS", yahoo_symbol="CS.PA", name="AXA", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="ENGI", yahoo_symbol="ENGI.PA", name="Engie", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="VIE", yahoo_symbol="VIE.PA", name="Veolia", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="CAP", yahoo_symbol="CAP.PA", name="Capgemini", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="DG", yahoo_symbol="DG.PA", name="Vinci", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="SGO", yahoo_symbol="SGO.PA", name="Saint-Gobain", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="KER", yahoo_symbol="KER.PA", name="Kering", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="PUB", yahoo_symbol="PUB.PA", name="Publicis Groupe", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    # French Market
    Instrument(symbol="CAC40", yahoo_symbol="^FCHI", name="CAC 40 Index", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),

    # ========================= GERMAN GROUP =========================
    Instrument(symbol="SAP", yahoo_symbol="SAP.DE", name="SAP SE", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="SIE", yahoo_symbol="SIE.DE", name="Siemens", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="ALV", yahoo_symbol="ALV.DE", name="Allianz", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="VOW3", yahoo_symbol="VOW3.DE", name="Volkswagen", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="BAS", yahoo_symbol="BAS.DE", name="BASF", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="DBK", yahoo_symbol="DBK.DE", name="Deutsche Bank", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="BAYN", yahoo_symbol="BAYN.DE", name="Bayer", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="MBG", yahoo_symbol="MBG.DE", name="Mercedes-Benz Group", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="ADS", yahoo_symbol="ADS.DE", name="Adidas", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="BMW", yahoo_symbol="BMW.DE", name="BMW", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="IFX", yahoo_symbol="IFX.DE", name="Infineon Technologies", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="DTE", yahoo_symbol="DTE.DE", name="Deutsche Telekom", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="RWE", yahoo_symbol="RWE.DE", name="RWE", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="EOAN", yahoo_symbol="EOAN.DE", name="E.ON", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="DHL", yahoo_symbol="DHL.DE", name="DHL Group", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="MRK", yahoo_symbol="MRK.DE", name="Merck KGaA", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="HEN3", yahoo_symbol="HEN3.DE", name="Henkel", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="FRE", yahoo_symbol="FRE.DE", name="Fresenius", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="CON", yahoo_symbol="CON.DE", name="Continental", country="DE", exchange="XETRA", source="yahoo"),
    # German Market
    Instrument(symbol="DAX", yahoo_symbol="^GDAXI", name="DAX Index", country="DE", exchange="XETRA", source="yahoo"),

    # ========================= ITALIAN GROUP =========================
    Instrument(symbol="ENEL", yahoo_symbol="ENEL.MI", name="Enel", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="ENI", yahoo_symbol="ENI.MI", name="Eni", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="ISP", yahoo_symbol="ISP.MI", name="Intesa Sanpaolo", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="UCG", yahoo_symbol="UCG.MI", name="UniCredit", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="RACE", yahoo_symbol="RACE.MI", name="Ferrari", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="STLAM", yahoo_symbol="STLAM.MI", name="Stellantis", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="G", yahoo_symbol="G.MI", name="Generali", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="STM", yahoo_symbol="STMMI.MI", name="STMicroelectronics", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="PRY", yahoo_symbol="PRY.MI", name="Prysmian", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="TIT", yahoo_symbol="TIT.MI", name="Telecom Italia", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="MB", yahoo_symbol="MB.MI", name="Mediobanca", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="MONC", yahoo_symbol="MONC.MI", name="Moncler", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="TEN", yahoo_symbol="TEN.MI", name="Tenaris", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    Instrument(symbol="PST", yahoo_symbol="PST.MI", name="Poste Italiane", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),
    # Italian Market (Corrected)
    Instrument(symbol="FTSEMIB", yahoo_symbol="FTSEMIB.MI", name="FTSE MIB Index", country="IT", exchange="BORSA_ITALIANA", source="yahoo"),

    # ========================= SPANISH GROUP =========================
    Instrument(symbol="IBE", yahoo_symbol="IBE.MC", name="Iberdrola", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="SAN_ES", yahoo_symbol="SAN.MC", name="Banco Santander", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="ITX", yahoo_symbol="ITX.MC", name="Inditex", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="BBVA", yahoo_symbol="BBVA.MC", name="BBVA", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="REP", yahoo_symbol="REP.MC", name="Repsol", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="TEF", yahoo_symbol="TEF.MC", name="Telefonica", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="AMS", yahoo_symbol="AMS.MC", name="Amadeus IT Group", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="CABK", yahoo_symbol="CABK.MC", name="CaixaBank", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="FER", yahoo_symbol="FER.MC", name="Ferrovial", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="ELE", yahoo_symbol="ELE.MC", name="Endesa", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="MAP", yahoo_symbol="MAP.MC", name="Mapfre", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="NTGY", yahoo_symbol="NTGY.MC", name="Naturgy", country="ES", exchange="BME", source="yahoo"),
    Instrument(symbol="AENA", yahoo_symbol="AENA.MC", name="Aena", country="ES", exchange="BME", source="yahoo"),
    # Spanish Market
    Instrument(symbol="IBEX35", yahoo_symbol="^IBEX", name="IBEX 35 Index", country="ES", exchange="BME", source="yahoo"),

    # ========================= DUTCH GROUP =========================
    Instrument(symbol="ASML", yahoo_symbol="ASML.AS", name="ASML Holding", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    Instrument(symbol="HEIA", yahoo_symbol="HEIA.AS", name="Heineken", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    Instrument(symbol="AD", yahoo_symbol="AD.AS", name="Ahold Delhaize", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    Instrument(symbol="PHIA", yahoo_symbol="PHIA.AS", name="Philips", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    Instrument(symbol="INGA", yahoo_symbol="INGA.AS", name="ING Groep", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    Instrument(symbol="PRX", yahoo_symbol="PRX.AS", name="Prosus", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    Instrument(symbol="WKL", yahoo_symbol="WKL.AS", name="Wolters Kluwer", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    Instrument(symbol="RAND", yahoo_symbol="RAND.AS", name="Randstad", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    Instrument(symbol="AGN", yahoo_symbol="AGN.AS", name="Aegon", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),
    # Dutch Market
    Instrument(symbol="AEX", yahoo_symbol="^AEX", name="AEX Index", country="NL", exchange="EURONEXT_AMSTERDAM", source="yahoo"),

    # ========================= BELGIAN GROUP =========================
    Instrument(symbol="ABI", yahoo_symbol="ABI.BR", name="Anheuser-Busch InBev", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),
    Instrument(symbol="KBC", yahoo_symbol="KBC.BR", name="KBC Group", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),
    Instrument(symbol="UCB", yahoo_symbol="UCB.BR", name="UCB SA", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),
    Instrument(symbol="AGS", yahoo_symbol="AGS.BR", name="Ageas", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),
    Instrument(symbol="ARGX", yahoo_symbol="ARGX.BR", name="argenx", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),
    Instrument(symbol="ACKB", yahoo_symbol="ACKB.BR", name="Ackermans & van Haaren", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),
    Instrument(symbol="SOLB", yahoo_symbol="SOLB.BR", name="Solvay", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),
    Instrument(symbol="COFB", yahoo_symbol="COFB.BR", name="Cofinimmo", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),
    # Belgian Market
    Instrument(symbol="BEL20", yahoo_symbol="^BFX", name="BEL 20 Index", country="BE", exchange="EURONEXT_BRUSSELS", source="yahoo"),

    # ========================= SWISS GROUP =========================
    Instrument(symbol="NESN", yahoo_symbol="NESN.SW", name="Nestle", country="CH", exchange="SIX", source="yahoo"),
    Instrument(symbol="ROG", yahoo_symbol="ROG.SW", name="Roche", country="CH", exchange="SIX", source="yahoo"),
    Instrument(symbol="NOVN", yahoo_symbol="NOVN.SW", name="Novartis", country="CH", exchange="SIX", source="yahoo"),
    Instrument(symbol="UBSG", yahoo_symbol="UBSG.SW", name="UBS Group", country="CH", exchange="SIX", source="yahoo"),
    Instrument(symbol="ZURN", yahoo_symbol="ZURN.SW", name="Zurich Insurance Group", country="CH", exchange="SIX", source="yahoo"),
    Instrument(symbol="ABBN", yahoo_symbol="ABBN.SW", name="ABB", country="CH", exchange="SIX", source="yahoo"),
    Instrument(symbol="CFR", yahoo_symbol="CFR.SW", name="Richemont", country="CH", exchange="SIX", source="yahoo"),
    Instrument(symbol="SIKA", yahoo_symbol="SIKA.SW", name="Sika", country="CH", exchange="SIX", source="yahoo"),
    # Swiss Market
    Instrument(symbol="SMI", yahoo_symbol="^SSMI", name="Swiss Market Index", country="CH", exchange="SIX", source="yahoo"),

    # ========================= SWEDISH GROUP =========================
    Instrument(symbol="VOLVB", yahoo_symbol="VOLV-B.ST", name="Volvo", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="ERICB", yahoo_symbol="ERIC-B.ST", name="Ericsson", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="HMB", yahoo_symbol="HM-B.ST", name="H&M", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="ATCOA", yahoo_symbol="ATCO-A.ST", name="Atlas Copco", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="SAND", yahoo_symbol="SAND.ST", name="Sandvik", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="INVEB", yahoo_symbol="INVE-B.ST", name="Investor AB", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    # Swedish Market
    Instrument(symbol="OMXS30", yahoo_symbol="^OMX", name="OMX Stockholm 30 Index", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
]


def list_symbols(universe: list[Instrument] | None = None) -> list[str]:
    """Return every AMQuant symbol currently registered in the universe."""
    universe = universe if universe is not None else UNIVERSE
    return [inst.symbol for inst in universe]


if __name__ == "__main__":
    # Quick way to eyeball what's installed:
    #   python -m amquant.dataSources.universe_data
    symbols = list_symbols()
    print(f"{len(symbols)} instruments registered:\n")
    for inst in UNIVERSE:
        print(f"{inst.symbol:10s} {inst.yahoo_symbol:12s} {inst.name} ({inst.country})")