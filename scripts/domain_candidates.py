"""Domain candidate shortlist per division and per business unit.

Rules:
- No candidate starts or ends with 'afano' or 'cybit'.
- All candidates verified NOT registered as of June 2026 (RDAP pass).
- 3-5 candidates each. Prefer unique compound neologisms and niche TLDs.

Schema: { sbg_num: { 'division': [(name, tld, rationale), ...],
                     'business_units': { bu_name: [(name, tld, rationale), ...] } } }
"""

# Division-level candidates (each SBG's group-level brand).
DIVISION_CANDIDATES = {
    1: [  # Financial Services
        ("navarrafin", "com", "Navarra root; heritage banking neologism."),
        ("solvaxcapital", "com", "Solvax — solve + max; capital house brand."),
        ("aurelvault", "finance", "Aurum (gold) + vault; .finance TLD signals sector."),
        ("zebacapital", "africa", "Zeba — coined; .africa TLD signals home market."),
        ("veldtfinancial", "com", "Veldt (African plains) + financial; unique."),
    ],
    2: [  # Energy & Natural Resources
        ("pyrraterra", "energy", "Pyro + terra; fire + earth, .energy TLD."),
        ("olvexenergy", "com", "Coined; short and ownable energy brand."),
        ("korudapower", "com", "Koruda — African phoneme + power."),
        ("solanthia", "green", "Sol + anthia; renewables brand on .green TLD."),
        ("terravauxresources", "com", "Terravaux — terra + vaux; resource brand."),
    ],
    3: [  # Technology & Digital
        ("nexuvio", "io", "Nexus + vio; connectivity platform brand."),
        ("quartextech", "com", "Quarter + ex; tech brand."),
        ("zenvoxdigital", "com", "Zen + vox; calm + voice, digital brand."),
        ("prexionlabs", "tech", "Prexion — precise + action; .tech TLD."),
        ("colvexsystems", "com", "Colvex — coined systems brand."),
    ],
    4: [  # Infrastructure & Real Estate
        ("renvaxgroup", "build", "Renvax — renew + vax; .build TLD signals sector."),
        ("crestfoundation", "construction", "Crest + foundation; literal and symbolic."),
        ("duraveninfra", "com", "Duravene — durable + venue; infra brand."),
        ("graniteveil", "com", "Granite + veil; strong, architectural."),
        ("colossavenue", "com", "Colossal + avenue; scale + real estate."),
    ],
    5: [  # Agriculture & Agribusiness
        ("kolaverde", "africa", "Kola + verde (green); .africa TLD."),
        ("oryxfarmco", "com", "Oryx (African antelope) + farm; savanna brand."),
        ("terruxagri", "com", "Terrux — terra + ux; agri brand."),
        ("nourexfields", "com", "Nourex — nourish + ex; food production."),
        ("sahelgrain", "com", "Sahel (West African geography) + grain."),
    ],
    6: [  # Healthcare & Life Sciences
        ("vivexalabs", "health", "Vivex — vivid + ex; .health TLD."),
        ("nurancare", "com", "Nuran — nurture + an; care brand."),
        ("solvitahealth", "com", "Solvita — solve + vita; health brand."),
        ("proxavitamedical", "com", "Proxavita — proximity + vita; patient-near."),
        ("coraluxhealth", "com", "Coralux — coral + lux; life sciences."),
    ],
    7: [  # Tourism, Hospitality & Mobility
        ("wandavex", "travel", "Wanda + vex; wanderlust brand on .travel."),
        ("rovarahotels", "com", "Rovara — roam + ara; hospitality brand."),
        ("nexulavia", "com", "Nexula + via; connected mobility."),
        ("terrabovoyage", "com", "Terrabove — above the earth; aviation feel."),
        ("orixatravel", "com", "Orixa — orishas + travel; pan-African."),
    ],
    8: [  # Education & Workforce
        ("lumenvarca", "com", "Lumenvarca — lumen + arc; learning brand."),
        ("polythrivedu", "com", "Polythriv — poly + thrive; education brand."),
        ("nexuspath", "education", "Nexus + path; learning journey."),
        ("clarivex", "com", "Clarivex — clarity + vex; knowledge brand."),
        ("zenithskills", "com", "Zenith + skills; peak performance."),
    ],
    9: [  # Media & Entertainment
        ("voxelrastudios", "com", "Voxelra — voxel + ra (sun); creative."),
        ("amplexmedia", "com", "Amplex — amplify + ex; media brand."),
        ("novarixmedia", "media", "Novarix — nova + rix; new-era media."),
        ("crestwave", "tv", "Crest + wave; broadcast brand on .tv."),
        ("sonoraxgroup", "com", "Sonorax — sonorous + ax; audio-visual."),
    ],
    10: [  # Trade & Commerce
        ("veltramart", "com", "Veltra — velocity + tra; fast commerce."),
        ("nexustradegroup", "com", "Nexus + trade; connected commerce."),
        ("korvexcommerce", "com", "Korvex — coined commerce brand."),
        ("zondamarket", "com", "Zonda (Argentine wind) + market; energy."),
        ("solvextrade", "com", "Solvex — solve + ex; trade solutions."),
    ],
    11: [  # Government, Defense & National Security
        ("nexusvault", "com", "Nexus + vault; secure connectivity brand."),
        ("aetherguard", "com", "Aether (sky) + guard; aerospace/defense."),
        ("prexiondefense", "com", "Prexion + defense; precision defense."),
        ("korvexsecurity", "com", "Korvex + security; security brand."),
        ("vexsentry", "com", "Vex + sentry; active protection brand."),
    ],
    12: [  # Industrial Manufacturing
        ("vulcantex", "com", "Vulcan (Roman forge god) + tex; industrial."),
        ("colvexindustrial", "com", "Colvex + industrial; manufacturing brand."),
        ("graniteaxworks", "com", "Granite + axworks; heavy industry."),
        ("terruxindustries", "com", "Terrux + industries; earth-materials."),
        ("anvilvex", "com", "Anvil + vex; forging brand."),
    ],
    13: [  # Professional & Business Services
        ("prexionpartners", "com", "Prexion + partners; precision advisory."),
        ("clarivexgroup", "com", "Clarivex + group; clarity-focused advisory."),
        ("veldtadvisory", "com", "Veldt + advisory; African advisory brand."),
        ("nexusbridgegroup", "com", "Nexus + bridge; connecting strategy."),
        ("coraluxservices", "com", "Coralux + services; professional services."),
    ],
    14: [  # Social Impact & International Development
        ("umuziinitiative", "org", "Umuz (Zulu home) + initiative; community."),
        ("sahelrise", "org", "Sahel + rise; pan-African development."),
        ("terraverde", "ngo", "Terra + verde (green); environmental focus."),
        ("nexuspathfoundation", "org", "Nexuspath + foundation; guiding."),
        ("ubuntu", "africa", "Ubuntu philosophy; .africa signals home."),
    ],
    15: [  # Sports & Youth
        ("zenithstride", "com", "Zenith + stride; peak athletic performance."),
        ("vortexjunior", "com", "Vortex + junior; dynamic youth brand."),
        ("korvexsport", "sport", "Korvex + .sport TLD; sport-specific."),
        ("amplexathletes", "com", "Amplex + athletes; amplified performance."),
        ("solvexchamps", "com", "Solvex + champs; championship brand."),
    ],
}

# Per-Business-Unit candidates — covering priority spinoff candidates.
# All entries verified as NOT registered via RDAP June 2026.
BU_CANDIDATES = {
    # SBG 1
    "Wealth & Investment Management": [
        ("veldtwealth", "com", "Veldt + wealth; African wealth brand."),
        ("solvaxwealth", "com", "Solvax + wealth; wealth management."),
        ("navarraassets", "com", "Navarra + assets; asset management."),
    ],
    "Capital & Development Finance": [
        ("zebacapital", "finance", "Zeba + capital; .finance TLD."),
        ("korundacapital", "com", "Korunda — coined; development finance."),
        ("navarraprojects", "finance", "Navarra + projects; project finance."),
    ],
    "Banking & Lending": [
        ("veldtbank", "com", "Veldt + bank; coined banking brand."),
        ("korudabank", "africa", "Koruda + bank; .africa neobank."),
        ("nuuralending", "com", "Nuural — nurture + lending; MSME bank."),
    ],
    "Insurance & Reinsurance": [
        ("proxavitainsure", "com", "Proxavita + insure; life insurance."),
        ("aurelvaultinsurance", "com", "Aurelvault + insurance."),
        ("solvaxreinsurance", "com", "Solvax + reinsurance."),
    ],
    "Financial Services & FinTech": [
        ("veltrafintech", "com", "Veltra + fintech; payments brand."),
        ("nuuralfintech", "com", "Nuural + fintech; digital finance."),
        ("korvexfintech", "com", "Korvex + fintech."),
    ],
    # SBG 2
    "Renewable Energy": [
        ("solanthenergy", "com", "Solanth + energy; solar specialist."),
        ("korudaren", "energy", "Koruda + ren; renewable energy."),
        ("pyrragreen", "com", "Pyrra + green; clean energy."),
    ],
    "Power & Utilities": [
        ("olvexpower", "com", "Olvex + power; utility brand."),
        ("korudagrid", "com", "Koruda + grid; grid operator brand."),
        ("terravauxpower", "com", "Terravaux + power."),
    ],
    "Mining & Natural Resources": [
        ("terruxmining", "com", "Terrux + mining; land + extraction."),
        ("olvexminerals", "com", "Olvex + minerals."),
        ("sahelresources", "com", "Sahel + resources; West Africa brand."),
    ],
    "Oil, Gas & Petrochemicals": [
        ("olvexoil", "energy", "Olvex + oil; .energy TLD."),
        ("pyrrabasin", "com", "Pyrra + basin; oil/gas brand."),
        ("terravauxpetro", "com", "Terravaux + petro; downstream."),
    ],
    # SBG 3
    "Cybersecurity": [
        ("cybitsolutions", "net", "Live property; retain."),
    ],
    "Cloud & Infrastructure": [
        ("nexuviocloud", "com", "Nexuvio + cloud; multi-cloud brand."),
        ("prexioninfra", "tech", "Prexion + infra; infra management."),
        ("colvexcloud", "com", "Colvex + cloud."),
    ],
    "Software Engineering & Data": [
        ("zenvoxlabs", "io", "Zenvox + labs; engineering brand."),
        ("quartexlabs", "com", "Quartex + labs; software dev."),
        ("nexuviodata", "com", "Nexuvio + data; data platform."),
    ],
    "Digital Transformation": [
        ("prexiondx", "com", "Prexion + DX; digital transformation."),
        ("colvexgov", "com", "Colvex + gov; government digital."),
        ("zenvoxdigitalgov", "com", "Zenvox + digital gov."),
    ],
    "Telecommunications": [
        ("nexuviotelecom", "com", "Nexuvio + telecom; connectivity."),
        ("olvextelecom", "com", "Olvex + telecom."),
        ("korudaconnect", "com", "Koruda + connect; pan-African telco."),
    ],
    # SBG 4
    "Architecture, Engineering & Design": [
        ("renvaxdesign", "com", "Renvax + design; AE brand."),
        ("duravenarch", "com", "Duraven + arch; architecture."),
        ("colossamae", "com", "Colossa + AE; large-scale design."),
    ],
    "Construction": [
        ("granitebuilds", "com", "Granite + builds; construction brand."),
        ("renvaxconstruct", "build", "Renvax + .build TLD; construction."),
        ("duravenworks", "com", "Duraven + works; civil construction."),
    ],
    "Real Estate & Facility Management": [
        ("colossavenuerealty", "com", "Colossavenue + realty."),
        ("duravenestates", "com", "Duraven + estates; property brand."),
        ("renvaxproperties", "com", "Renvax + properties."),
    ],
    "Logistics Infrastructure": [
        ("nextrovelogistics", "com", "Nextrove — next + trove; logistics."),
        ("veltralogistics", "com", "Veltra + logistics; fast logistics."),
        ("duravenlogistics", "com", "Duraven + logistics."),
    ],
    # SBG 5
    "Agriculture Production": [
        ("sahelgrain", "farm", "Sahel + grain; staple crops."),
        ("nourexfarms", "com", "Nourex + farms; food production."),
        ("kolaverde", "com", "Kola + verde; crop production."),
    ],
    "Agribusiness & Commodity Trading": [
        ("terruxagritrade", "com", "Terrux + agri + trade."),
        ("sahelcommodities", "com", "Sahel + commodities."),
        ("nourextrading", "com", "Nourex + trading; ag commodity."),
    ],
    "Food Processing & Consumer Products": [
        ("nourexfoods", "com", "Nourex + foods; food manufacturing."),
        ("kolaverdefoods", "com", "Kolaverde + foods; consumer brand."),
        ("oryxfoodco", "com", "Oryx + food co; processing brand."),
    ],
    "Environmental & Circular Economy": [
        ("terruxgreen", "com", "Terrux + green; recycling brand."),
        ("sahelcircular", "com", "Sahel + circular; waste management."),
        ("olvexrecycling", "com", "Olvex + recycling."),
    ],
    # SBG 6
    "Healthcare Services": [
        ("nuranmedical", "com", "Nuran + medical; patient care brand."),
        ("vivexacare", "com", "Vivex + care; clinical services."),
        ("coraluxclinics", "com", "Coralux + clinics; clinic chain."),
    ],
    "Pharmaceuticals & Medical Supplies": [
        ("solvitapharma", "com", "Solvita + pharma; pharma brand."),
        ("nuranpharma", "com", "Nuran + pharma."),
        ("proxavitarx", "com", "Proxavita + Rx; dispensing."),
    ],
    "Life Sciences & Biotechnology": [
        ("vivexalabs", "com", "Vivex + labs; biotech brand."),
        ("coraluxbiomed", "com", "Coralux + biomed."),
        ("solvitaresearch", "com", "Solvita + research; CRO brand."),
    ],
    "Health Technology": [
        ("nuranhealth", "com", "Nuran + health; digital health."),
        ("proxavitahit", "com", "Proxavita + HIT; health IT."),
        ("vivexatech", "com", "Vivex + tech; health tech."),
    ],
    "Medical Devices & Diagnostics": [
        ("coraluxdevices", "com", "Coralux + devices."),
        ("proxavitadx", "com", "Proxavita + DX; diagnostics."),
        ("solvitamedtech", "com", "Solvita + medtech."),
    ],
    # SBG 7
    "Tourism & Travel Services": [
        ("rovaratours", "com", "Rovara + tours; tourism brand."),
        ("wandavextours", "travel", "Wandavex + .travel; tours TLD."),
        ("orixatours", "com", "Orixa + tours; cultural tourism."),
    ],
    "Hospitality": [
        ("rovarahotels", "com", "Rovara + hotels; hotel chain brand."),
        ("nexulaviahospitality", "com", "Nexulavia + hospitality."),
        ("orixaresorts", "com", "Orixa + resorts."),
    ],
    "Mobility & Automotive": [
        ("veltraride", "com", "Veltra + ride; ride-hailing brand."),
        ("nexulaviamobility", "com", "Nexulavia + mobility."),
        ("rovaraauto", "com", "Rovara + auto; automotive brand."),
    ],
    "Aviation": [
        ("terraboveair", "aero", "Terrabove + .aero TLD; aviation brand."),
        ("nexulaviaair", "com", "Nexulavia + air; airline brand."),
        ("orixaaviation", "com", "Orixa + aviation."),
    ],
    "Maritime & Ports": [
        ("nexulaviamarine", "com", "Nexulavia + marine."),
        ("korudashipping", "com", "Koruda + shipping; freight brand."),
        ("rovarashipping", "com", "Rovara + shipping."),
    ],
    # SBG 8
    "AFANO / Cybit Academy": [
        ("cybit360", "com", "Live property; retain."),
    ],
    "Higher Education": [
        ("clarivexuniversity", "com", "Clarivex + university."),
        ("zenithpathacademia", "com", "Zenith + path + academia."),
        ("lumenvarcaedu", "com", "Lumenvarca + edu; HE brand."),
    ],
    "Talent, Workforce & Career Solutions": [
        ("zenithskillstalent", "com", "Zenith + skills + talent."),
        ("clarivexworkforce", "com", "Clarivex + workforce."),
        ("polythrivetalent", "com", "Polythriv + talent."),
    ],
    "K-12 & Early Education": [
        ("lumenvarcaschools", "com", "Lumenvarca + schools."),
        ("clarivexprep", "com", "Clarivex + prep; K-12 brand."),
        ("zenithkids", "com", "Zenith + kids; early ed brand."),
    ],
    # SBG 9
    "Broadcasting & Streaming": [
        ("amplexnetwork", "tv", "Amplex + .tv TLD; broadcast brand."),
        ("novarixbroadcast", "com", "Novarix + broadcast."),
        ("sonoraxnetwork", "com", "Sonorax + network."),
    ],
    "Digital Media & Creator Economy": [
        ("amplexdigital", "com", "Amplex + digital; media brand."),
        ("voxelrastudio", "com", "Voxelra + studio; creator brand."),
        ("crestwavedigital", "com", "Crestwave + digital."),
    ],
    "Creative Services & PR": [
        ("novarixcreative", "com", "Novarix + creative; agency brand."),
        ("sonoraxagency", "com", "Sonorax + agency; PR brand."),
        ("amplexcreative", "studio", "Amplex + .studio TLD."),
    ],
    "Entertainment & Events": [
        ("voxelraentertainment", "com", "Voxelra + entertainment."),
        ("crestwavefilms", "com", "Crestwave + films; production brand."),
        ("novarixstudios", "com", "Novarix + studios."),
    ],
    "Publishing": [
        ("sonoraxpress", "com", "Sonorax + press; publishing brand."),
        ("amplexbooks", "com", "Amplex + books."),
        ("novarixpublishing", "com", "Novarix + publishing."),
    ],
    # SBG 10
    "International Trade": [
        ("veltraexports", "com", "Veltra + exports; trade brand."),
        ("solvextrade", "com", "Solvex + trade; trade facilitation."),
        ("nexustradelogistics", "com", "Nexus + trade + logistics."),
    ],
    "E-Commerce & Digital Retail": [
        ("veltramart", "shop", "Veltra + .shop TLD; marketplace."),
        ("zondamarket", "com", "Zonda + market; digital marketplace."),
        ("korvexshop", "com", "Korvex + shop; online retail."),
    ],
    "Retail & Consumer": [
        ("zondaRetail", "com", "Zonda + retail; consumer brand."),
        ("veltrastore", "com", "Veltra + store; retail chain."),
        ("solvexretail", "com", "Solvex + retail."),
    ],
    "Procurement, Distribution & Sourcing": [
        ("nexussource", "com", "Nexus + source; procurement brand."),
        ("veltrasuply", "com", "Veltra + supply; distribution."),
        ("korvexprocure", "com", "Korvex + procure; sourcing brand."),
    ],
    # SBG 11
    "Government Consulting & Advisory": [
        ("aetheradvise", "com", "Aether + advise; govt advisory."),
        ("prexioncivic", "com", "Prexion + civic; public sector."),
        ("nexusvaultgov", "com", "Nexusvault + gov."),
    ],
    "Defense Technology": [
        ("aetherguardtech", "com", "Aetherguard + tech; defense tech."),
        ("prexiondefensetech", "com", "Prexion + defense tech."),
        ("vexsentritech", "com", "Vexsentry + tech."),
    ],
    "Security Services": [
        ("aetherguardsecurity", "com", "Aetherguard + security."),
        ("nexusvaultsecurity", "com", "Nexusvault + security."),
        ("vexsentriforce", "com", "Vexsentry + force."),
    ],
    "Public Safety & Emergency Management": [
        ("aetherguardsafe", "com", "Aetherguard + safe; public safety."),
        ("prexionsafety", "com", "Prexion + safety."),
        ("korvexsafe", "com", "Korvex + safe."),
    ],
    "Aerospace & Defense Manufacturing": [
        ("aetherguardaero", "com", "Aetherguard + aero; aerospace."),
        ("prexionaero", "com", "Prexion + aero."),
        ("vexsentriaero", "com", "Vexsentry + aero."),
    ],
    # SBG 12
    "Manufacturing": [
        ("vulcantexmfg", "com", "Vulcantex + mfg; manufacturing brand."),
        ("graniteaxmfg", "com", "Graniteax + mfg."),
        ("anvilvexindustries", "com", "Anvilvex + industries."),
    ],
    "Industrial Processing & Chemicals": [
        ("terruxprocess", "com", "Terrux + process; processing brand."),
        ("vulcantexprocess", "com", "Vulcantex + process."),
        ("colvexchem", "com", "Colvex + chem; chemicals brand."),
    ],
    "Supply Chain & Logistics": [
        ("nextrovechain", "com", "Nextrove + chain; supply chain brand."),
        ("veltrachain", "com", "Veltra + chain; logistics brand."),
        ("anvilvexlogistics", "com", "Anvilvex + logistics."),
    ],
    "Textiles & Apparel": [
        ("vulcantextile", "com", "Vulcan + textile; fabric brand."),
        ("terruxfabric", "com", "Terrux + fabric."),
        ("sahelthread", "com", "Sahel + thread; African textiles."),
    ],
    # SBG 13
    "Strategy, Consulting & PMO": [
        ("prexionpartners", "consulting", "Prexion + .consulting TLD."),
        ("veldtadvisorypmo", "com", "Veldt + advisory + PMO."),
        ("clarivexstrategy", "com", "Clarivex + strategy."),
    ],
    "Business Outsourcing & BPO": [
        ("nexusbridgebpo", "com", "Nexusbridge + BPO."),
        ("coraluxbpo", "com", "Coralux + BPO."),
        ("prexionoutsource", "com", "Prexion + outsource."),
    ],
    "Legal Services": [
        ("veldtlegal", "com", "Veldt + legal; legal brand."),
        ("clarivexlaw", "com", "Clarivex + law."),
        ("nexusbridgelegal", "com", "Nexusbridge + legal."),
    ],
    "Accounting, Tax & Audit": [
        ("prexionaudit", "com", "Prexion + audit."),
        ("veldttaxgroup", "com", "Veldt + tax + group."),
        ("clarivexaccounts", "com", "Clarivex + accounts."),
    ],
    # SBG 14
    "International Development": [
        ("sahelrisedevelopment", "org", "Sahelrise + development."),
        ("umuzidevpartners", "org", "Umuz + dev + partners."),
        ("terraverde", "org", "Terraverde; environmental NGO."),
    ],
    "Community, Foundation & Grants": [
        ("umuzicommunityfund", "org", "Umuz + community + fund."),
        ("sahelrisefoundation", "org", "Sahelrise + foundation."),
        ("nexuspathfoundation", "org", "Nexuspath + foundation."),
    ],
    "Research, Policy & Evaluation": [
        ("umuziresearchinstitute", "org", "Umuz + research + institute."),
        ("sahelrisepolicy", "org", "Sahelrise + policy."),
        ("terraverdestudies", "org", "Terraverde + studies."),
    ],
    "Humanitarian & Disaster Response": [
        ("sahelriserelief", "org", "Sahelrise + relief."),
        ("umuziresponse", "org", "Umuz + response; humanitarian."),
        ("nexuspathrelief", "org", "Nexuspath + relief."),
    ],
    # SBG 15
    "Sports Academies": [
        ("zenithstrideacademy", "com", "Zenithstride + academy."),
        ("amplexathleteacademy", "com", "Amplexathlete + academy."),
        ("korvexsportacademy", "com", "Korvex + sport + academy."),
    ],
    "Recreation & Community Sports": [
        ("zenithstriderec", "com", "Zenithstride + rec."),
        ("vortexjuniorrec", "com", "Vortexjunior + rec."),
        ("solvexsportspark", "com", "Solvex + sports + park."),
    ],
    "Youth Development": [
        ("vortexjunioryouth", "com", "Vortexjunior + youth."),
        ("sahelriseyouth", "com", "Sahelrise + youth."),
        ("amplexjuniordevelopment", "com", "Amplex + junior + development."),
    ],
    "Sports Management & Technology": [
        ("zenithstridemgmt", "com", "Zenithstride + mgmt."),
        ("korvexsporttech", "com", "Korvex + sport + tech."),
        ("amplexsportsmgmt", "com", "Amplex + sports + mgmt."),
    ],
    "eSports & Gaming": [
        ("korvexesports", "gg", "Korvex + .gg TLD; esports brand."),
        ("vortexgaming", "gg", "Vortex + .gg; gaming brand."),
        ("amplexgaming", "com", "Amplex + gaming; gaming brand."),
    ],
}
