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
    Instrument(symbol="STM", yahoo_symbol="STM.PA", name="STMicroelectronics", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="HO", yahoo_symbol="HO.PA", name="Thales", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="RI", yahoo_symbol="RI.PA", name="Pernod Ricard", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
    Instrument(symbol="EL", yahoo_symbol="EL.PA", name="EssilorLuxottica", country="FR", exchange="EURONEXT_PARIS", source="yahoo"),
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
    Instrument(symbol="MTX", yahoo_symbol="MTX.DE", name="MTU Aero Engines", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="DB1", yahoo_symbol="DB1.DE", name="Deutsche Boerse", country="DE", exchange="XETRA", source="yahoo"),
    Instrument(symbol="QIA", yahoo_symbol="QIA.DE", name="Qiagen", country="DE", exchange="XETRA", source="yahoo"),
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
    # Italian Market
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
    Instrument(symbol="LONN", yahoo_symbol="LONN.SW", name="Lonza Group", country="CH", exchange="SIX", source="yahoo"),
    # Swiss Market
    Instrument(symbol="SMI", yahoo_symbol="^SSMI", name="Swiss Market Index", country="CH", exchange="SIX", source="yahoo"),

    # ========================= SWEDISH GROUP =========================
    Instrument(symbol="VOLVB", yahoo_symbol="VOLV-B.ST", name="Volvo", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="ERICB", yahoo_symbol="ERIC-B.ST", name="Ericsson", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="HMB", yahoo_symbol="HM-B.ST", name="H&M", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="ATCOA", yahoo_symbol="ATCO-A.ST", name="Atlas Copco", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="SAND", yahoo_symbol="SAND.ST", name="Sandvik", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="INVEB", yahoo_symbol="INVE-B.ST", name="Investor AB", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    Instrument(symbol="ASSA-B", yahoo_symbol="ASSA-B.ST", name="Assa Abloy", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),
    # Swedish Market
    Instrument(symbol="OMXS30", yahoo_symbol="^OMX", name="OMX Stockholm 30 Index", country="SE", exchange="NASDAQ_STOCKHOLM", source="yahoo"),

    # ========================= UNITED KINGDOM =========================
    Instrument(symbol="AZN", yahoo_symbol="AZN.L", name="AstraZeneca", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="SHELL", yahoo_symbol="SHEL.L", name="Shell", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="HSBA", yahoo_symbol="HSBA.L", name="HSBC Holdings", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="ULVR", yahoo_symbol="ULVR.L", name="Unilever", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="LLOY", yahoo_symbol="LLOY.L", name="Lloyds Banking Group", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="BARC", yahoo_symbol="BARC.L", name="Barclays", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="BP", yahoo_symbol="BP.L", name="BP", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="GSK", yahoo_symbol="GSK.L", name="GSK", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="REL", yahoo_symbol="REL.L", name="RELX", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="BT-A", yahoo_symbol="BT-A.L", name="BT Group", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="RIO", yahoo_symbol="RIO.L", name="Rio Tinto", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="GLEN", yahoo_symbol="GLEN.L", name="Glencore", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="VOD", yahoo_symbol="VOD.L", name="Vodafone", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="III", yahoo_symbol="III.L", name="3i Group", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="CPG", yahoo_symbol="CPG.L", name="Compass Group", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="ABF", yahoo_symbol="ABF.L", name="Associated British Foods", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="IMB", yahoo_symbol="IMB.L", name="Imperial Brands", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="EXPN", yahoo_symbol="EXPN.L", name="Experian", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="FLTR", yahoo_symbol="FLTR.L", name="Flutter Entertainment", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="AHT", yahoo_symbol="AHT.L", name="Ashtead Group", country="UK", exchange="LSE", source="yahoo"),
    Instrument(symbol="SSE", yahoo_symbol="SSE.L", name="SSE", country="UK", exchange="LSE", source="yahoo"),
    # UK Market
    Instrument(symbol="FTSE100", yahoo_symbol="^FTSE", name="FTSE 100 Index", country="UK", exchange="LSE", source="yahoo"),

    # ========================= UNITED STATES =========================
    Instrument(symbol="AAPL", yahoo_symbol="AAPL", name="Apple", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="MSFT", yahoo_symbol="MSFT", name="Microsoft", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="NVDA", yahoo_symbol="NVDA", name="NVIDIA", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="GOOGL", yahoo_symbol="GOOGL", name="Alphabet", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="AMZN", yahoo_symbol="AMZN", name="Amazon", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="META", yahoo_symbol="META", name="Meta Platforms", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="TSLA", yahoo_symbol="TSLA", name="Tesla", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="BRK-B", yahoo_symbol="BRK-B", name="Berkshire Hathaway", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="JPM", yahoo_symbol="JPM", name="JPMorgan Chase", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="V", yahoo_symbol="V", name="Visa", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="MA", yahoo_symbol="MA", name="Mastercard", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="XOM", yahoo_symbol="XOM", name="Exxon Mobil", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="UNH", yahoo_symbol="UNH", name="UnitedHealth Group", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="PG", yahoo_symbol="PG", name="Procter & Gamble", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="JNJ", yahoo_symbol="JNJ", name="Johnson & Johnson", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="HD", yahoo_symbol="HD", name="Home Depot", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="AVGO", yahoo_symbol="AVGO", name="Broadcom", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="LLY", yahoo_symbol="LLY", name="Eli Lilly", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="COST", yahoo_symbol="COST", name="Costco", country="US", exchange="NASDAQ", source="yahoo"),
    #Instrument(symbol="NFLX", yahoo_symbol="NFLX", name="Netflix", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="AMD", yahoo_symbol="AMD", name="Advanced Micro Devices", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="CRM", yahoo_symbol="CRM", name="Salesforce", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="TMO", yahoo_symbol="TMO", name="Thermo Fisher", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="ABT", yahoo_symbol="ABT", name="Abbott Laboratories", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="ACN", yahoo_symbol="ACN", name="Accenture", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="LIN", yahoo_symbol="LIN", name="Linde", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="MCD", yahoo_symbol="MCD", name="McDonald's", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="NKE", yahoo_symbol="NKE", name="Nike", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="DIS", yahoo_symbol="DIS", name="Walt Disney", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="WMT", yahoo_symbol="WMT", name="Walmart", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="KO", yahoo_symbol="KO", name="Coca-Cola", country="US", exchange="NYSE", source="yahoo"),
    # US Market
    Instrument(symbol="SPX", yahoo_symbol="^GSPC", name="S&P 500 Index", country="US", exchange="INDEX", source="yahoo"),
    Instrument(symbol="NDX", yahoo_symbol="^IXIC", name="Nasdaq Composite", country="US", exchange="INDEX", source="yahoo"),
    Instrument(symbol="DJI", yahoo_symbol="^DJI", name="Dow Jones", country="US", exchange="INDEX", source="yahoo"),
    Instrument(symbol="SPY", yahoo_symbol="SPY", name="S&P 500 ETF", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="QQQ", yahoo_symbol="QQQ", name="Nasdaq-100 ETF", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="IWM", yahoo_symbol="IWM", name="Russell 2000 ETF", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="DIA", yahoo_symbol="DIA", name="Dow Jones ETF", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="TLT", yahoo_symbol="TLT", name="20+ Year Treasury ETF", country="US", exchange="NASDAQ", source="yahoo"),
    Instrument(symbol="GLD", yahoo_symbol="GLD", name="Gold ETF", country="US", exchange="NYSE", source="yahoo"),
    Instrument(symbol="USO", yahoo_symbol="USO", name="Oil ETF", country="US", exchange="NYSE", source="yahoo"),

    # ========================= JAPAN =========================
    Instrument(symbol="7203", yahoo_symbol="7203.T", name="Toyota Motor", country="JP", exchange="TSE", source="yahoo"),
    Instrument(symbol="9983", yahoo_symbol="9983.T", name="Fast Retailing", country="JP", exchange="TSE", source="yahoo"),
    Instrument(symbol="8306", yahoo_symbol="8306.T", name="Mitsubishi UFJ", country="JP", exchange="TSE", source="yahoo"),
    Instrument(symbol="6758", yahoo_symbol="6758.T", name="Sony", country="JP", exchange="TSE", source="yahoo"),
    Instrument(symbol="8035", yahoo_symbol="8035.T", name="Tokyo Electron", country="JP", exchange="TSE", source="yahoo"),
    Instrument(symbol="6861", yahoo_symbol="6861.T", name="Keyence", country="JP", exchange="TSE", source="yahoo"),
    Instrument(symbol="9433", yahoo_symbol="9433.T", name="KDDI", country="JP", exchange="TSE", source="yahoo"),
    Instrument(symbol="4063", yahoo_symbol="4063.T", name="Shin-Etsu Chemical", country="JP", exchange="TSE", source="yahoo"),
    # Japan Market
    Instrument(symbol="N225", yahoo_symbol="^N225", name="Nikkei 225", country="JP", exchange="INDEX", source="yahoo"),

    # ========================= CHINA & HONG KONG =========================
    Instrument(symbol="BABA", yahoo_symbol="BABA", name="Alibaba", country="CN", exchange="NYSE", source="yahoo"),
    Instrument(symbol="9988", yahoo_symbol="9988.HK", name="Alibaba HK", country="CN", exchange="HKEX", source="yahoo"),
    Instrument(symbol="0700", yahoo_symbol="0700.HK", name="Tencent", country="CN", exchange="HKEX", source="yahoo"),
    Instrument(symbol="3690", yahoo_symbol="3690.HK", name="Meituan", country="CN", exchange="HKEX", source="yahoo"),
    Instrument(symbol="9618", yahoo_symbol="9618.HK", name="JD.com", country="CN", exchange="HKEX", source="yahoo"),
    Instrument(symbol="1024", yahoo_symbol="1024.HK", name="Kuaishou", country="CN", exchange="HKEX", source="yahoo"),
    Instrument(symbol="1211", yahoo_symbol="1211.HK", name="BYD", country="CN", exchange="HKEX", source="yahoo"),
    # China / HK Market
    Instrument(symbol="HSI", yahoo_symbol="^HSI", name="Hang Seng", country="HK", exchange="INDEX", source="yahoo"),
    Instrument(symbol="000001", yahoo_symbol="000001.SS", name="Shanghai Composite", country="CN", exchange="INDEX", source="yahoo"),

    # ========================= INDIA =========================
    Instrument(symbol="RELIANCE", yahoo_symbol="RELIANCE.NS", name="Reliance Industries", country="IN", exchange="NSE", source="yahoo"),
    Instrument(symbol="HDFCBANK", yahoo_symbol="HDFCBANK.NS", name="HDFC Bank", country="IN", exchange="NSE", source="yahoo"),
    Instrument(symbol="INFY", yahoo_symbol="INFY", name="Infosys", country="IN", exchange="NYSE", source="yahoo"),
    Instrument(symbol="TCS", yahoo_symbol="TCS.NS", name="Tata Consultancy", country="IN", exchange="NSE", source="yahoo"),
    Instrument(symbol="ICICIBANK", yahoo_symbol="ICICIBANK.NS", name="ICICI Bank", country="IN", exchange="NSE", source="yahoo"),
    Instrument(symbol="HINDUNILVR", yahoo_symbol="HINDUNILVR.NS", name="Hindustan Unilever", country="IN", exchange="NSE", source="yahoo"),
    Instrument(symbol="BHARTIARTL", yahoo_symbol="BHARTIARTL.NS", name="Bharti Airtel", country="IN", exchange="NSE", source="yahoo"),
    # India Market
    Instrument(symbol="BSESN", yahoo_symbol="^BSESN", name="BSE Sensex", country="IN", exchange="INDEX", source="yahoo"),

    # ========================= AUSTRALIA =========================
    Instrument(symbol="BHP", yahoo_symbol="BHP.AX", name="BHP Group", country="AU", exchange="ASX", source="yahoo"),
    Instrument(symbol="CBA", yahoo_symbol="CBA.AX", name="Commonwealth Bank", country="AU", exchange="ASX", source="yahoo"),
    Instrument(symbol="CSL", yahoo_symbol="CSL.AX", name="CSL Limited", country="AU", exchange="ASX", source="yahoo"),
    Instrument(symbol="RIO.AU", yahoo_symbol="RIO.AX", name="Rio Tinto Australia", country="AU", exchange="ASX", source="yahoo"),
    Instrument(symbol="MQG", yahoo_symbol="MQG.AX", name="Macquarie Group", country="AU", exchange="ASX", source="yahoo"),
    Instrument(symbol="WBC", yahoo_symbol="WBC.AX", name="Westpac Banking", country="AU", exchange="ASX", source="yahoo"),
    # Australia Market
    Instrument(symbol="ASX200", yahoo_symbol="^AXJO", name="S&P/ASX 200", country="AU", exchange="INDEX", source="yahoo"),

    # ========================= CANADA =========================
    Instrument(symbol="RY", yahoo_symbol="RY.TO", name="Royal Bank of Canada", country="CA", exchange="TSX", source="yahoo"),
    Instrument(symbol="TD", yahoo_symbol="TD.TO", name="Toronto-Dominion Bank", country="CA", exchange="TSX", source="yahoo"),
    Instrument(symbol="SHOP", yahoo_symbol="SHOP", name="Shopify", country="CA", exchange="NYSE", source="yahoo"),
    Instrument(symbol="ENB", yahoo_symbol="ENB.TO", name="Enbridge", country="CA", exchange="TSX", source="yahoo"),
    Instrument(symbol="CNQ", yahoo_symbol="CNQ.TO", name="Canadian Natural Resources", country="CA", exchange="TSX", source="yahoo"),
    # Canada Market
    Instrument(symbol="TSX", yahoo_symbol="^GSPTSE", name="S&P/TSX Composite", country="CA", exchange="INDEX", source="yahoo"),

    # ========================= LATIN AMERICA =========================
    Instrument(symbol="VALE", yahoo_symbol="VALE", name="Vale", country="BR", exchange="NYSE", source="yahoo"),
    Instrument(symbol="ITUB", yahoo_symbol="ITUB", name="Itau Unibanco", country="BR", exchange="NYSE", source="yahoo"),
    Instrument(symbol="PBR", yahoo_symbol="PBR", name="Petrobras", country="BR", exchange="NYSE", source="yahoo"),
    Instrument(symbol="BBAS3", yahoo_symbol="BBAS3.SA", name="Banco do Brasil", country="BR", exchange="B3", source="yahoo"),
    Instrument(symbol="MXX", yahoo_symbol="^MXX", name="IPC Mexico", country="MX", exchange="INDEX", source="yahoo"),

    # ========================= COMMODITIES & CRYPTO =========================
    Instrument(symbol="GC", yahoo_symbol="GC=F", name="Gold Futures", country="GLOBAL", exchange="COMEX", source="yahoo"),
    Instrument(symbol="CL", yahoo_symbol="CL=F", name="Crude Oil Futures", country="GLOBAL", exchange="NYMEX", source="yahoo"),
    Instrument(symbol="SI", yahoo_symbol="SI=F", name="Silver Futures", country="GLOBAL", exchange="COMEX", source="yahoo"),
    Instrument(symbol="HG", yahoo_symbol="HG=F", name="Copper Futures", country="GLOBAL", exchange="COMEX", source="yahoo"),
    Instrument(symbol="ZW", yahoo_symbol="ZW=F", name="Wheat Futures", country="GLOBAL", exchange="CBOT", source="yahoo"),
    Instrument(symbol="KC", yahoo_symbol="KC=F", name="Coffee Futures", country="GLOBAL", exchange="ICE", source="yahoo"),
    Instrument(symbol="BTC", yahoo_symbol="BTC-USD", name="Bitcoin", country="GLOBAL", exchange="CRYPTO", source="yahoo"),
    Instrument(symbol="ETH", yahoo_symbol="ETH-USD", name="Ethereum", country="GLOBAL", exchange="CRYPTO", source="yahoo"),
    Instrument(symbol="SOL", yahoo_symbol="SOL-USD", name="Solana", country="GLOBAL", exchange="CRYPTO", source="yahoo"),
    Instrument(symbol="XRP", yahoo_symbol="XRP-USD", name="Ripple", country="GLOBAL", exchange="CRYPTO", source="yahoo"),
    Instrument(symbol="VIX", yahoo_symbol="^VIX", name="CBOE Volatility Index", country="US", exchange="INDEX", source="yahoo"),
]

def list_symbols(universe: list[Instrument] | None = None) -> list[str]:
    """Return every AMQuant symbol currently registered in the universe."""
    universe = universe if universe is not None else UNIVERSE
    return [inst.symbol for inst in universe]

if __name__ == "__main__":
    symbols = list_symbols()
    print(f"{len(symbols)} instruments registered:\n")
    for inst in UNIVERSE:
        print(f"{inst.symbol:12s} {inst.yahoo_symbol:15s} {inst.name} ({inst.country})")